from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

def create_classifer(**params):
    """
    Function to create and train a Decision Tree classifier on the Iris dataset.
    The trained model is saved to a file for later use.
    """
    # Load the dataset
    df = pd.read_csv("./data/iris.csv")  # Load the dataset
    X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]  # Features
    Y = df["Species"]  # Target variable

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)  # Split the dataset

    iris_model = DecisionTreeClassifier(**params)  # Initialize the model
    iris_model.fit(X_train, Y_train)  # Train the model

    with open("./models/my_model.pkl", "wb") as fileobj:  # Save the model
        pickle.dump(iris_model, fileobj)

    return True

if __name__ == "__main__":
    # Example usage
    create_classifer(max_depth=3,criterion='entropy', random_state=42)
    print("Model trained and saved successfully.")