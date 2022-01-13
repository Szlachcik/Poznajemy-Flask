from flask import Flask, render_template

app = Flask(__name__)

@app.route("/mypage/me")
def me():
    return render_template("me.html")

if __name__ == "__main__":
    app.run()
