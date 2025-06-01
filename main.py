from flask import Flask, request, jsonify
import pickle
from utils import create_classifer

app = Flask(__name__) # Initialize Flask app

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Ajay's Flask App!"

@app.route("/training", methods=["POST"]) #<-- this is the controller
def get_square(): # <-- this is view function
    params = request.get_json()
    create_classifer(**params) # Call the function to create and train the classifier

    return jsonify({"msg":"Model trained and saved successfully!"})

@app.route("/get_model_params", methods=["GET"])
def get_model_params():
    """
    This function returns the parameters of the trained model.
    """
    with open("./models/my_model.pkl", "rb") as fileobj:
        iris_model = pickle.load(fileobj)  # Load the pre-trained model
    params = iris_model.get_params()
    return jsonify(params)

@app.route("/predict", methods=["POST"]) #<-- this is the controller
def iris_prediction(): # <-- this is view function
    with open("./models/my_model.pkl", "rb") as fileobj:
        iris_model = pickle.load(fileobj)  # Load the pre-trained model
    data = request.get_json()
    sepal_lenght = data.get("sl")
    petal_lenght = data.get("pl")
    sepal_width = data.get("sw")
    petal_width = data.get("pw")
    flower_type = iris_model.predict([[sepal_lenght, sepal_width, petal_lenght, petal_width]])
    return jsonify({"predcited_flower_type": flower_type[0]})


if __name__ == "__main__":
    app.run()  # Run the app in debug mode