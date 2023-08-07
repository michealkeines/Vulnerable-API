
def novuln():
    return "This is just a simple response"


def reflected(xss):
    username = xss.get("username", "noprovided")

    if username:
        return {"msg": f"Hello, {username}"}, 200
    else:
        return {"msg": f"Error"}, 400
