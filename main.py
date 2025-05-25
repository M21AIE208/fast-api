from flask import Flask, request, jsonify

app = Flask(__name__) # Initialize Flask app

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Ajay's Flask App!"



if __name__ == "__main__":
    app.run()  # Run the app in debug mode