import sqlite3

conn = sqlite3.connect("vulns.db", check_same_thread=False)

def sqlinovuln():
    return "This is just a simple response"


def sqlivuln(sqli):
    username = sqli.get("username", "noprovided")
    password = sqli.get("password", "noprovided")

    if username and password:
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT * FROM USERS WHERE USERNAME='{username}'")
            users = cur.fetchall()
        except Exception as e:
            return {"msg": f"{e}"}, 200
        return {"msg": f"Hello, {users}"}, 200
    else:
        return {"msg": f"Error"}, 400