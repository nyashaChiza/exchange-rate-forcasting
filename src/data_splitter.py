import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split_data(data_path:str , data_dir='data'):
    # Convert 'date' column to datetime
    df = pd.read_csv(data_path)
    df['date'] = pd.to_datetime(df['date'])
    
    # Split data into features (X) and target variable (y)
    X = df['date'].values.reshape(-1, 1)  # Reshape to 2D array for compatibility
    y = df['rate']
    
    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create directories if they don't exist
    os.makedirs(os.path.join(data_dir, 'training-data'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'test-data'), exist_ok=True)
    
    # Save training and testing sets to CSV
    training_data_path = os.path.join(data_dir, 'training-data', 'training_data.csv')
    testing_data_path = os.path.join(data_dir, 'test-data', 'testing_data.csv')
    
    pd.DataFrame({'date': X_train.flatten(), 'rate': y_train}).to_csv(training_data_path, index=False)
    pd.DataFrame({'date': X_test.flatten(), 'rate': y_test}).to_csv(testing_data_path, index=False)
    
    print("Training and testing data saved successfully.")


