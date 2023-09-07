from flask import Flask, request
from sound import Audio
from markupsafe import escape

def return_dict(status, message):
    return {"status": status, "message": message}

app = Flask(__name__)
audio = Audio()

@app.route("/")
def test():
    return "<h1>Work in progress</h1>"

@app.route("/reset")
def reset_volume():
    audio.reset()
    return return_dict("OK", "Volume has been reset")

@app.route("/volume")
def change_volume():
    arg = request.args.get("turn")
    stat = "OK"
    if arg == "up":
        audio.increase_volume()
        msg = "Volume has been increased"
    elif arg == "down":
        audio.reduce_volume()
        msg = "Volume has been decreased"
    else:
        stat = "not OK"
        msg = "Bad or no parameter \"turn\""
    return return_dict(stat, msg)
app.run(debug=False, host="0.0.0.0")
