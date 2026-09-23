"""
Simple ML Model Training
This trains a basic machine learning model to predict health risk
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle

def train_simple_model():
    """Train a simple decision tree model"""
    
    print("📚 Step 1: Loading data...")
    # Read the CSV file we created
    df = pd.read_csv('health_data.csv')
    
    print("🔢 Step 2: Preparing data...")
    # Features (input) - the things we measure
    X = df[['age', 'temperature', 'heart_rate', 'spo2', 'num_symptoms']]
    
    # Target (output) - what we want to predict
    y = df['risk']
    
    print("✂️ Step 3: Splitting data into training and testing...")
    # Use 80% for training, 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    
    print("\n🤖 Step 4: Training the AI model...")
    # Create a simple Decision Tree (like a flowchart)
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    
    # Train it!
    model.fit(X_train, y_train)
    
    print("✅ Training complete!")
    
    print("\n📊 Step 5: Testing accuracy...")
    # Check how well it works
    train_accuracy = model.score(X_train, y_train) * 100
    test_accuracy = model.score(X_test, y_test) * 100
    
    print(f"Training accuracy: {train_accuracy:.1f}%")
    print(f"Testing accuracy: {test_accuracy:.1f}%")
    
    print("\n💾 Step 6: Saving the model...")
    # Save the trained model
    with open('health_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("✅ Model saved as 'health_model.pkl'")
    print("\n🎉 All done! You can now use the model to make predictions!")
    
    return model

if __name__ == "__main__":
    train_simple_model()
