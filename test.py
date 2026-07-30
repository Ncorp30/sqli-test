from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    if user_id is None or user_id == "":
        return jsonify({"error": "Missing required parameter: id"}), 400

    return jsonify({"message": f"User ID: {user_id}"})

if __name__ == "__main__":
    app.run()
