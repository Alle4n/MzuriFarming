from django.test import TestCase

# Create your tests here.
import pandas as pd
import os

# Replace with your actual file path
file_path = os.path.join('static/excel/crops.xlsx')
print("File path being used:", file_path)


def read_crop_data_from_excel():
    try:
        df = pd.read_excel('static/excel/crops.xlsx', sheet_name='Sheet1')
        print("Columns in the DataFrame:", df.columns.tolist())  # Print the columns
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    read_crop_data_from_excel()
