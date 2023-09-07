from flask import Flask, request
from sound import Audio
from markupsafe import escape

def return_dict(status, message):
    return {"status": status, "message": message}

app = Flask(__name__, static_url_path="/static")
audio = Audio()

@app.route("/")
def index():
    return app.send_static_file("index.html")

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

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
