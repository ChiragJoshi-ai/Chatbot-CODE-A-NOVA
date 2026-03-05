from flask import Flask, render_template, request
from memory import update_user, generate_reply

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    reply = None

    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]

        update_user(username, message)
        reply = generate_reply(username, message)

    return render_template("index.html", reply=reply)


if __name__ == "__main__":
    app.run(debug=True)