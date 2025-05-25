from flask import Flask, request, jsonify

app = Flask(__name__) # Initialize Flask app

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Ajay's Flask App!"

@app.route("/get_sqaure", methods=["POST"])
def get_square():
    data = request.get_json()
    number = data.get("number")
    return jsonify({"square": number ** 2})



if __name__ == "__main__":
    app.run()  # Run the app in debug mode