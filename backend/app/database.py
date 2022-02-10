import mysql.connector
from os import getenv
import datetime
from collections import defaultdict

from typing import List

PAG_SIZE = 6


def connect():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='macius',
        password='siema',
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
    sql = 'SELECT aid FROM artists WHERE name = %s;'
    val = (name,)
    cursor = db.cursor(buffered=True)
    cursor.execute(sql, val)
    res = cursor.fetchone()[0]
    cursor.close()
    db.close()
    return res


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
              WHERE e.artists_aid = a.aid AND (e.name LIKE %s OR a.name LIKE %s) ORDER BY e.date"""
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
                      WHERE e.artists_aid = a.aid ORDER BY e.date"""
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
            return False
    items = cursor.fetchall()
    res = [[] for i in range(ceil(len(items)/PAG_SIZE))]
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
        return False
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return str(res).lower()


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
        return "false"
    cursor.close()
    db.close()
    return str(password == db_password)


def add_ticket(uid: str, eid: str):
    db = connect()
    sql = "INSERT INTO tickets(uid, eid) VALUES (%s, %s)"
    sql2 = "UPDATE events SET sold = sold + 1 WHERE eid = %s"
    cursor = db.cursor()
    val = (uid, eid)
    val2 = (eid,)
    try:
        cursor.execute(sql2, val2)
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
    db = connect()
    cursor = db.cursor()
    sql = """SELECT e.eid, e.name, e.date, e.maxAmount, e.sold, e.lid, e.income, e.soldout,
                     e.isOver, e.artists_aid, a.name, a.genre, a.photolink FROM events e, artists a, tickets t 
                     WHERE e.artists_aid = a.aid AND t.eid = e.eid AND t.uid = %s ORDER BY e.date"""
    val = (uid,)
    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
        return False
    res = defaultdict()
    i = 0
    for row in cursor.fetchall():
        if i // PAG_SIZE not in res.keys():
            res[i // PAG_SIZE] = []
        res[i // PAG_SIZE].append(
            {'eid': row[0], 'name': row[1], 'date': row[2].strftime("%Y/%m/%d"), 'maxAmount': row[3],
             'sold': row[4], 'lid': row[5], 'income': row[6], 'soldout': row[7], 'isOver': row[8],
             'aid': row[9], 'artistName': row[10], 'genre': row[11], 'url': row[12]})
        i += 1
    cursor.close()
    db.close()
    return {'page': res}


def get_admin(login: str):
    db = connect()
    cursor = db.cursor()
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
