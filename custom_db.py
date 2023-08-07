import sqlite3

def setup_db():
    conn = sqlite3.connect("vulns.db", check_same_thread=False)

    vulns = [
        "xss, 1",
        "lfi, 2",
        "rfi, 3",
        "hhi, 4",
        "sqli, 5",
        "ssti, 6",
    ]

    table ="""CREATE TABLE USERS(USERNAME VARCHAR(255), PASSWORD VARCHAR(255));"""
    conn.execute(table)

    table ="""CREATE TABLE vulns(NAME VARCHAR(255), ID VARCHAR(255));"""
    conn.execute(table)

    for vuln in vulns:
        ins = f"INSERT INTO vulns VALUES ({vuln})"
        conn.execute(ins)

    ins = f"INSERT INTO USERS VALUES (mike, kaines)"
    conn.execute(ins)

    ins = f"INSERT INTO USERS VALUES (admin, admin)"
    conn.execute(ins)

    conn.commit()