import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define file path
file_path = r"C:\Users\Apon\Desktop\Homework2\CSI300_CSI500_2021.xlsx"

# Load the Excel file and print sheet names
excel_data = pd.ExcelFile(file_path)
print("Available Sheets:", excel_data.sheet_names)

# Read individual sheets into DataFrames
df_csi300_july   = pd.read_excel(file_path, sheet_name="CSI300_July")
df_csi300_augsep = pd.read_excel(file_path, sheet_name="CSI300_AugSep")
df_csi500_july   = pd.read_excel(file_path, sheet_name="CSI500_July")
df_csi500_augsep = pd.read_excel(file_path, sheet_name="CSI500_AugSep")

# Concatenate Q3 data for both indices
df_csi300_q3 = pd.concat([df_csi300_july, df_csi300_augsep], ignore_index=True)
df_csi500_q3 = pd.concat([df_csi500_july, df_csi500_augsep], ignore_index=True)

# Ensure 'Date' column exists, convert to datetime, and set it as the index
for data_frame in [df_csi300_q3, df_csi500_q3]:
    data_frame['Date'] = pd.to_datetime(data_frame['Date'])
    data_frame.set_index('Date', inplace=True)

# Print column names of the CSI300 Q3 DataFrame
print(df_csi300_q3.columns)
