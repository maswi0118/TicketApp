import datetime
from typing import List

import mysql.connector

PAG_SIZE = 6


def connect():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
        database='s403025'
    )


def add_city(city: str, province: str) -> bool:
    db = connect()
    db.autocommit
    sql = "INSERT INTO cities(city, province) VALUES (%s, %s);"
    val = (city, province)
    cursor = db.cursor()
    try:
        cursor.execute(sql, val)
    except:
        cursor.close()
        db.close()
        return False
    db.commit()
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return res


def get_cities(province: str = None) -> List[str]:
    db = connect()
    cursor = db.cursor()
    if province:
        sql = 'SELECT city FROM cities WHERE province = %s'
        val = (province,)
        cursor.execute(sql, val)
    else:
        sql = 'SELECT city FROM cities;'
        cursor.execute(sql)
    res = [x[0] for x in cursor.fetchall()]
    cursor.close()
    db.close()
    return res


def get_cid(city: str) -> int:
    db = connect()
    sql = 'SELECT cid FROM cities WHERE city = %s;'
    val = (city,)
    cursor = db.cursor(buffered=True)
    cursor.execute(sql, val)
    res = cursor.fetchone()[0]
    cursor.close()
    db.close()
    return res


def add_location(name: str, capacity: int, address: str, indoor: bool, city: str) -> bool:
    db = connect()
    cid = get_cid(city)
    sql = 'INSERT INTO locations(name, capacity, address, indoor, cid) VALUES (%s, %s, %s, %s, %s);'
    val = (name, capacity, address, indoor, cid)
    cursor = db.cursor()

    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        cursor.close()
        db.close()
        print(e)
        return False
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return res


def add_artist(name: str, genre: str, nationality: str, about: str) -> bool:
    db = connect()
    sql = 'INSERT INTO artists(name, genre, nationality, about) VALUES (%s, %s, %s, %s);'
    val = (name, genre, nationality, about)
    cursor = db.cursor()

    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        cursor.close()
        db.close()
        print(e)
        return False
    res = cursor.lastrowid
    cursor.close()
    db.close()
    return res


def get_artists(aid: int = None) -> List[str]:
    db = connect()
    cursor = db.cursor(buffered=True)
    if aid:
        sql = 'SELECT name FROM artists WHERE aid = %s'
        val = (aid,)
        cursor.execute(sql, val)
        res = cursor.fetchone()[0]
    else:
        sql = 'SELECT name FROM artists;'
        cursor.execute(sql)
        res = [x[0] for x in cursor.fetchall()]
    cursor.close()
    db.close()
    return res


def get_aid(name: str) -> int:
    db = connect()
    print(name)
    sql = 'SELECT aid FROM artists WHERE name = %s'
    val = (name,)
    cursor = db.cursor(buffered=True)
    cursor.execute(sql, val)
    res = cursor.fetchone()
    cursor.close()
    db.close()
    return res[0]


def get_locations(cid: int = None) -> List[str]:
    db = connect()
    cursor = db.cursor()
    if cid:
        sql = 'SELECT name FROM locations WHERE cid = %s'
        val = (cid,)
        cursor.execute(sql, val)
    else:
        sql = 'SELECT name FROM locations;'
        cursor.execute(sql)
    res = [x[0] for x in cursor.fetchall()]
    cursor.close()
    db.close()
    return res


def get_lid(name: str) -> int:
    db = connect()
    sql = 'SELECT lid FROM locations WHERE name = %s;'
    val = (name,)
    cursor = db.cursor(buffered=True)
    cursor.execute(sql, val)
    res = cursor.fetchone()[0]
    cursor.close()
    db.close()
    return res


def add_event(name: str, date: datetime, price: int, location: str, artist: str) -> bool:
    db = connect()
    sql = "INSERT INTO events(name, date, maxAmount, price, lid, artists_aid) VALUES (%s, %s, %s, %s, %s, %s)"
    lid = get_lid(location)
    aid = get_aid(artist)
    max_amount = get_maxAmount(lid)
    cursor = db.cursor()
    val = (name, date, max_amount, price, lid, aid)
    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        cursor.close()
        db.close()
        print(e)
        return False
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return res


def get_events(name: str = None):
    from math import ceil
    db = connect()
    cursor = db.cursor()
    if name:
        sql = """SELECT e.eid, e.name, e.date, e.maxAmount, e.sold, e.lid, e.income, e.soldout,
              e.isOver, e.artists_aid, a.name, a.genre, a.photolink, e.price FROM events e, artists a 
              WHERE e.artists_aid = a.aid AND (e.name LIKE %s OR a.name LIKE %s) AND isOver == 0 ORDER BY e.date"""
        val = (f'%{name}%', f'%{name}%')
        try:
            cursor.execute(sql, val)
        except Exception as e:
            cursor.close()
            db.close()
            print(e)
            return False
    else:
        sql = """SELECT e.eid, e.name, e.date, e.maxAmount, e.sold, e.lid, e.income, e.soldout,
                      e.isOver, e.artists_aid, a.name, a.genre, a.photolink, e.price FROM events e, artists a 
                      WHERE e.artists_aid = a.aid AND isOver == 0 ORDER BY e.date"""
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
            return False
    items = cursor.fetchall()
    res = [[] for i in range(ceil(len(items) / PAG_SIZE))]
    i = 0
    for row in items:
        res[i // PAG_SIZE].append(
            {'eid': row[0], 'name': row[1], 'date': row[2].strftime("%Y/%m/%d"), 'maxAmount': row[3],
             'sold': row[4], 'lid': row[5], 'income': row[6], 'soldout': row[7], 'isOver': row[8],
             'aid': row[9], 'artistName': row[10], 'genre': row[11], 'url': row[12],
             'price': row[13]})
        i += 1
    cursor.close()
    db.close()
    return {'page': res}


def get_districts():
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT DISTINCT province FROM cities'
    cursor.execute(sql)
    res = [x[0] for x in cursor.fetchall()]
    cursor.close()
    db.close()
    return res


def get_maxAmount(lid: int) -> int:
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = "SELECT capacity FROM locations WHERE lid = %s "
    val = (lid,)
    cursor.execute(sql, val)
    res = cursor.fetchone()[0]
    cursor.close()
    db.close()
    return res


def set_image(aid: int, src: str):
    db = connect()
    cursor = db.cursor()
    if src == '../static/images/noImage.png':
        src = '../images/noImage.png'
    sql = 'UPDATE artists SET photolink = %s WHERE aid = %s'
    val = (src, aid)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()


def add_user(username: str, password: str, email: str, firstname: str, lastname: str, phone_number: str) -> bool:
    db = connect()
    sql = "INSERT INTO users(username, password, email, firstname, lastname, phone_number) " \
          "VALUES (%s, %s, %s, %s, %s, %s)"
    cursor = db.cursor()
    val = (username, password, email, firstname, lastname, phone_number)
    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print(e)
        cursor.close()
        db.close()
        return {'response': str(False)}
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return {'response': str(res)}


def login_user(username: str, password: str) -> bool:
    db = connect()
    sql = 'SELECT password FROM users WHERE username = %s'
    val = (username,)
    cursor = db.cursor(buffered=True)
    try:
        cursor.execute(sql, val)
        db_password, = cursor.fetchone()
    except Exception as e:
        print(e)
        cursor.close()
        db.close()
        return str(False)
    cursor.close()
    db.close()
    return str(password == db_password)


def is_soldout(eid: str) -> bool:
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = "SELECT isOver FROM events WHERE eid = %s"
    try:
        cursor.execute(sql, (eid,))
    except Exception as e:
        print(e)
        cursor.close()
        db.close()
        return False
    res = bool(cursor.fetchone()[0])
    cursor.close()
    db.close()
    return res


def add_ticket(uid: str, eid: str):
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = "SELECT balance FROM users WHERE id = %s"
    try:
        cursor.execute(sql, (uid,))
    except Exception as e:
        print(e)
        cursor.close()
        db.close()
        return False
    balance = cursor.fetchone()[0]
    sql = "SELECT price FROM events WHERE eid = %s"
    try:
        cursor.execute(sql, (eid,))
    except Exception as e:
        print(e)
        cursor.close()
        db.close()
        return False
    price = cursor.fetchone()[0]
    if balance < price or is_soldout(eid):
        return False
    else:
        sql = "INSERT INTO tickets(uid, eid) VALUES (%s, %s)"
        sql2 = "UPDATE events SET sold = sold + 1 WHERE eid = %s"
        sql3 = "UPDATE users SET balance = balance - (SELECT price FROM events WHERE eid = %s) WHERE id = %s"
        val = (uid, eid)
        val2 = (eid,)
        val3 = (eid, uid)
        try:
            cursor.execute(sql2, val2)
            cursor.execute(sql3, val3)
            cursor.execute(sql, val)
            db.commit()
        except Exception as e:
            print(e)
            cursor.close()
            db.close()
            return False
        res = cursor.lastrowid
        cursor.close()
        db.close()
        return res


def get_tickets(uid: str):
    from math import ceil
    db = connect()
    cursor = db.cursor()
    sql = """SELECT e.eid, e.name, e.date, e.maxAmount, e.sold, e.lid, e.income, e.soldout,
                     e.isOver, e.artists_aid, a.name, a.genre, a.photolink, t.tid FROM events e, artists a, tickets t 
                     WHERE e.artists_aid = a.aid AND t.eid = e.eid AND t.uid = %s ORDER BY e.date"""
    val = (uid,)
    try:
        cursor.execute(sql, val)
    except Exception as e:
        cursor.close()
        db.close()
        print(e)
        return False
    items = cursor.fetchall()
    res = [[] for i in range(ceil(len(items) / PAG_SIZE))]
    i = 0
    for row in items:
        res[i // PAG_SIZE].append(
            {'eid': row[0], 'name': row[1], 'date': row[2].strftime("%Y/%m/%d"), 'maxAmount': row[3],
             'sold': row[4], 'lid': row[5], 'income': row[6], 'soldout': row[7], 'isOver': row[8],
             'aid': row[9], 'artistName': row[10], 'genre': row[11], 'url': row[12], 'tid': row[13]})
        i += 1
    cursor.close()
    db.close()
    return {'page': res}


def get_admin(login: str) -> tuple:
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = "SELECT * FROM admins WHERE login = %s"
    val = (login,)
    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
        return False
    res = cursor.fetchone()
    cursor.close()
    db.close()
    return res


def add_admin(login: str, password: str):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO admins(login, password) VALUES (%s, %s)"
    val = (login, password)
    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
        return False
    db.commit()
    cursor.close()
    db.close()


def get_uid(username: str) -> str:
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = "SELECT id FROM users WHERE username = %s"
    val = (username,)
    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
        return False
    res = cursor.fetchone()
    cursor.close()
    db.close()
    return res[0]


def add_money(username: str, amount: float):
    db = connect()
    cursor = db.cursor()
    sql = 'UPDATE users SET balance = balance + %s WHERE username = %s'
    val = (amount, username)
    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
        cursor.close()
        db.close()
        return False
    db.commit()
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return res


def delete_event(eid: str):
    refund(eid)
    db = connect()
    cursor = db.cursor()
    sql = 'DELETE FROM events WHERE eid = %s'
    val = (eid,)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()


def refund(eid: str):
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = 'SELECT uid FROM tickets WHERE eid = %s'
    sql2 = 'UPDATE users SET balance = balance + (SELECT price FROM events WHERE eid = %s) WHERE id = %s'
    sql3 = 'DELETE FROM tickets WHERE eid = %s'
    val = (eid,)
    cursor.execute(sql, val)
    uids = [x[0] for x in cursor.fetchall()]
    cursor.execute(sql3, val)
    for uid in uids:
        val2 = (eid, uid)
        cursor.execute(sql2, val2)
    db.commit()
    db.close()
    cursor.close()


def get_events_names():
    db = connect()
    cursor = db.cursor()
    sql = "SELECT name FROM events ORDER BY date"
    cursor.execute(sql)
    res = [x[0] for x in cursor.fetchall()]
    db.close()
    cursor.close()
    return res


def get_eid(name: str) -> str:
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = "SELECT eid FROM events WHERE name = %s"
    val = (name,)
    cursor.execute(sql, val)
    res = cursor.fetchone()
    db.close()
    cursor.close()
    return res[0]


def delete_artist(name: str):
    db = connect()
    cursor = db.cursor()
    aid = get_aid(name)
    sql = "SELECT eid FROM events WHERE artists_aid = %s"
    val = (aid,)
    cursor.execute(sql, val)
    eids = [x[0] for x in cursor.fetchall()]
    for eid in eids:
        delete_event(eid)
    sql = 'DELETE FROM artists WHERE name = %s'
    val = (name,)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()


def check_if_is_over():
    db = connect()
    cursor = db.cursor()
    sql = "SELECT eid FROM events WHERE date < %s AND isOver = 0"
    val = (datetime.datetime.now(), )
    cursor.execute(sql, val)
    eids = [x[0] for x in cursor.fetchall()]
    print(eids)
    sql = 'UPDATE events SET isOver = 1 WHERE eid = %s'
    for eid in eids:
        val = (eid, )
        cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
