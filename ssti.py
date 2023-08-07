from flask import request
from jinja2 import Template

def sstinovuln():
    return f"This is ssti no vuln, 49"


def sstivuln(ssti):
    exp = ssti.get("mathexp", "test")
    test = Template("my temp: " + exp)
    if exp:
        return {"msg": test.render()}, 200
    else:
        return {"msg": f"Error"}, 400
