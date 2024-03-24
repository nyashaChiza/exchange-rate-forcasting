import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split_data(data_path: str, data_dir='data'):
    # Read the data from CSV
    df = pd.read_csv(data_path)

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Define features (X) and target variable (y)
    X = df.drop(columns=['rate'])  # Features excluding the target variable
    y = df['rate']  # Target variable
    
    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create directories if they don't exist
    os.makedirs(os.path.join(data_dir, 'training-data'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'test-data'), exist_ok=True)
    
    # Save training and testing sets to CSV
    training_data_path = os.path.join(data_dir, 'training-data', 'training_data.csv')
    testing_data_path = os.path.join(data_dir, 'test-data', 'testing_data.csv')
    
    # Concatenate X_train/X_test with y_train/y_test to maintain consistency in indices
    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)
    
    # Save to CSV
    train_data.to_csv(training_data_path, index=False)
    test_data.to_csv(testing_data_path, index=False)
    
    print("Training and testing data saved successfully.")
