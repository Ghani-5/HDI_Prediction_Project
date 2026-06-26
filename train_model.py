import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Read dataset
df = pd.read_csv("dataset/hdi.csv")

# Select required columns
df = df[[
    "Life Expectancy at Birth (2021)",
    "Expected Years of Schooling (2021)",
    "Mean Years of Schooling (2021)",
    "Gross National Income Per Capita (2021)",
    "Human Development Groups"
]]

# Remove rows with missing values
df = df.dropna()

print("Shape after removing missing values:")
print(df.shape)

# Label Encoding
encoder = LabelEncoder()

df["Human Development Groups"] = encoder.fit_transform(
    df["Human Development Groups"]
)

print("\nClass Mapping:")
for i, label in enumerate(encoder.classes_):
    print(f"{label} --> {i}")

# Features and Target
X = df.drop("Human Development Groups", axis=1)
y = df["Human Development Groups"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Features Shape:", X_train.shape)
print("Testing Features Shape:", X_test.shape)

print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)
from sklearn.ensemble import RandomForestClassifier

# Create the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Predict
y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(y_pred)

print("\nActual Values:")
print(y_test.values)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
import joblib

joblib.dump(model, "model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("Model saved successfully!")
print("Encoder saved successfully!")