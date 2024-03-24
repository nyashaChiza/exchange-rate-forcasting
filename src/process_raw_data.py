import os
from datetime import datetime
import pandas as pd

def process_and_save_data(excel_file):
    # Load the Excel file
    df = pd.read_excel(excel_file)

    # Transpose the DataFrame so that months are rows and years are columns
    df = df.transpose()
    df.reset_index(inplace=True)
    df.columns = ['period','rate']
    df['date'] = pd.to_datetime(df['period'].str.split().str[0], format='%YM%m') 
    df.drop(columns=['period'], inplace=True)

    
    # Create directory if it doesn't exist
    output_dir = "data/processed-data"
    os.makedirs(output_dir, exist_ok=True)

    # Generate file name using current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    csv_file = os.path.join(output_dir, f"processed_data_{current_date}.csv")

    # Save the processed DataFrame to CSV
    df.to_csv(csv_file, index=False)

    print(f"Processed data saved to {csv_file}")

# Example usage:
# excel_file = "exchange_rate_data.xlsx"  # Replace with the path to your Excel file
# process_and_save_data(excel_file)
