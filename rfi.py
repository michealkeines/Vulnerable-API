import requests

def fetchimage(name):
    try:
        file = requests.get(url=name, timeout=2, verify=False).text
    except:
        file = ""
    return file

def rfinovuln():
    return f"This is just a simple image"


def rfivuln(rfi):
    filename = rfi.get("imagelink", "http://google.com")

    if filename:
        return {"msg": f"response, {fetchimage(filename)}"}, 200
    else:
        return {"msg": f"Error"}, 400
