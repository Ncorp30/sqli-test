from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    return "User ID: " + user_id

if __name__ == "__main__":
    app.run()
