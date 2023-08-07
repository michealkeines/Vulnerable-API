def fetchfile(name):
    try:
        file = open(name).read()
    except:
        file = ""
    return file

def lfinovuln():
    return f"This is just a simple response {fetchfile('req.txt')}"


def lfivuln(lfi):
    filename = lfi.get("filename", "readme.txt")

    if filename:
        return {"msg": f"response, {fetchfile(filename)}" }, 200
    else:
        return {"msg": f"Error"} , 400
