import sqlite3
import hashlib

from utils import hash_password


def connection():
    return sqlite3.connect('../dbt.db')


def create_table_user():
    con = connection()
    cur = con.cursor()
    cur.execute("""
        create table if not exists user(
                id integer not null primary key autoincrement,
                first_name varchar(30),
                last_name varchar(30),
                birth_day date,
                email varchar(50),
                username varchar(50),
                password varchar(150)
        )
    """)
    con.commit()
    con.close()


def insert_user(data: dict):
    con = connection()
    cur = con.cursor()
    hashed_password = hash_password(data['password'])
    data['password'] = hashed_password
    query = """
        insert into user(
        first_name,
        last_name,
        birth_day,
        email,
        username,
        password
        ) values
        (?, ?, ?, ?, ?, ?)
    """
    values = tuple(data.values())
    cur.execute(query, values)
    con.commit()
    con.close()


def login(username: str, password: str):
    con = connection()
    cur = con.cursor()
    hashed_password = hash_password(password)
    query = """
        select * from user
        where username=? and password=?
    """
    value = (username, hashed_password)
    cur.execute(query, value)
    return bool(cur.fetchone())


def user_is_exist(field, value):
    query = f"""
        select count(id) from user
        where {field}=?
    """
    value = (value,)
    con = connection()
    cur = con.cursor()
    cur.execute(query, value)
    return cur.fetchone()[0]