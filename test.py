from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    if user_id is None:
        abort(400, description="Missing id query parameter")
    try:
        user_id = int(user_id)
    except (TypeError, ValueError):
        abort(400, description="Invalid id query parameter")

    return "User ID: " + str(user_id)

if __name__ == "__main__":
    app.run(debug=False)
