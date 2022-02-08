import mysql.connector
from os import getenv
import datetime

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123456789',
    database='s403025'
)


def add_city(city: str, province: str) -> bool:
    sql = "INSERT INTO cities(city, province) VALUES (%s, %s);"
    val = (city, province)
    cursor = db.cursor()

    try:
        cursor.execute(sql, val)
        db.commit()
    except:
        return False

    return cursor.rowcount == 1


def get_cities() -> list[str]:
    sql = 'SELECT city FROM cities;'
    cursor = db.cursor()
    cursor.execute(sql)
    return [x[0] for x in cursor.fetchall()]


def get_cid(city: str) -> int:
    sql = 'SELECT cid FROM cities WHERE city = %s;'
    val = (city,)
    cursor = db.cursor()
    cursor.execute(sql, val)
    return cursor.fetchone()[0]


def add_location(name: str, capacity: int, address: str, indoor: bool, city: str) -> bool:
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

    return cursor.rowcount == 1


def add_artist(name: str, genre: str, nationality: str, about: str) -> bool:
    sql = 'INSERT INTO artists(name, genre, nationality, about) VALUES (%s, %s, %s, %s);'
    val = (name, genre, nationality, about)
    cursor = db.cursor()

    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print(e)
        return False

    return cursor.rowcount == 1


def get_artists() -> list[str]:
    sql = 'SELECT name FROM artists;'
    cursor = db.cursor()
    cursor.execute(sql)
    return [x[0] for x in cursor.fetchall()]


def get_aid(name: str) -> int:
    sql = 'SELECT aid FROM artists WHERE name = %s;'
    val = (name,)
    cursor = db.cursor()
    cursor.execute(sql, val)
    return cursor.fetchone()[0]


def get_locations() -> list[str]:
    sql = 'SELECT name FROM locations;'
    cursor = db.cursor()
    cursor.execute(sql)
    return [x[0] for x in cursor.fetchall()]


def get_lid(name: str) -> int:
    sql = 'SELECT lid FROM locations WHERE name = %s;'
    val = (name,)
    cursor = db.cursor(buffered=True)
    cursor.execute(sql, val)
    return cursor.fetchone()[0]


def add_event(name: str, date: datetime, limit: int, location: str, artist: str) -> bool:
    sql = "INSERT INTO events(name, date, maxAmount, lid, artists_aid) VALUES (%s, %s, %s, %s, %s)"
    cursor = db.cursor()
    lid = get_lid(location)
    cursor.reset()
    aid = get_aid(artist)
    cursor.reset()
    val = (name, date, limit, lid, aid)
    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print(e)
        return False
    return cursor.rowcount == 1


def get_events(name: str):
    sql = "SELECT * FROM events WHERE name LIKE %s"
    val = ('%' + name + '%',)
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
    return res
