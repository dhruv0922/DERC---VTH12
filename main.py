from preprocessing import load_and_preprocess_data
from model import build_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
#main file used to train the data
def main():
    # Load and preprocess the data
    X, y = load_and_preprocess_data()

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build and train the model
    model = build_model(input_shape=(X_train.shape[1], 1))
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

    # Test the model
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Plot the actual vs predicted values
    plt.plot(y_test, label='Actual Prices')
    plt.plot(y_pred, label='Predicted Prices')
    plt.legend()
    plt.title('Actual vs Predicted Housing Prices')
    plt.show()

if __name__ == "__main__":
    main()
