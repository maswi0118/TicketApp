import mysql.connector
from os import getenv
import datetime


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
        return False
    db.commit()
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return res


def get_cities(province: str = None) -> list[str]:
    db = connect()
    cursor = db.cursor()
    if province:
        sql = 'SELECT city FROM cities WHERE province = %s'
        val = (province, )
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
        print(e)
        return False
    res = cursor.lastrowid
    cursor.close()
    db.close()
    return res


def get_artists(aid: int = None) -> list[str]:
    db = connect()
    cursor = db.cursor(buffered=True)
    if aid:
        sql = 'SELECT name FROM artists WHERE aid = %s'
        val = (aid, )
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


def get_locations(cid: int = None) -> list[str]:
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
        print(e)
        return False
    res = cursor.rowcount == 1
    cursor.close()
    db.close()
    return res


def get_events(name: str):
    db = connect()
    sql = "SELECT * FROM events WHERE name LIKE %s ORDER BY date"
    val = (f'%{name}%',)
    cursor = db.cursor()
    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
        return False
    res = []
    for row in cursor.fetchall():
        res.append({'eid': row[0], 'name': row[1], 'date': row[2].strftime("%Y/%m/%d"), 'maxAmount': row[3],
                    'sold': row[4], 'lid': row[5], 'income': row[6], 'soldout': row[7], 'isOver': row[8],
                    'aid': row[9]})
    response = {}
    n = len(res)
    for i in range(n//5):
        response[i] = res[i*5:i*5+5]
    cursor.close()
    db.close()
    return {'page': [response]}

# def get_artists(name: str = ''):
#     db = connect()
#     cursor = db.cursor()
#     if name:
#         sql = 'SELECT * FROM artists WHERE name LIKE %s'
#         val = (f'%{name}%',)
#     else:
#         sql = 'SELECT * FROM artists'
#         val =''
#     try:
#         cursor.execute(sql, val)
#     except Exception as e:
#         print(e)
#         return False
#     res = []
#     for row in cursor.fetchall():
#         res.append({'eid': row[0], 'name': row[1], 'date': row[2].strftime("%Y/%m/%d"), 'maxAmount': row[3],
#                     'sold': row[4], 'lid': row[5], 'income': row[6], 'soldout': row[7], 'isOver': row[8],
#                     'aid': row[9]})

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
    sql = 'UPDATE artists SET photolink = %s WHERE aid = %s'
    val = (src, aid)
    cursor.execute(sql, val)
    cursor.close()
    db.close()
