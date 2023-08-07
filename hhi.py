from flask import request

def hhinovuln():
    return f"This is hhi no vuln"


def hhivuln(hhi):
    headerss = request.headers
    print(f"headers: {headerss}")
    
    try:
        h  = headerss["Host"]
    except Exception as e:
        print(f"failed: {e}")
        h = "temo.com"

    if headerss:
        return {"msg": f"response, <a href='{h}'>"}, 200
    else:
        return {"msg": f"failed"}, 400
