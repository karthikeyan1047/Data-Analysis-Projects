import pandas as pd
import os

# Sheet to Sheets

input_file = 'payments.xlsx'

excel_file = pd.ExcelFile(input_file, engine='openpyxl')

output_file = "Sheet_Sheets.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as output:
    for sht in excel_file.sheet_names:
        df = pd.read_excel(input_file, sheet_name=sht)
        for category in df["payment_method"].unique():
            newDf = df[df["payment_method"]==category]
            newDf.to_excel(output, sheet_name=category, index=False)



# Sheet to Files

input_file = 'payments.xlsx'

excel_file = pd.ExcelFile(input_file, engine='openpyxl')
cur_directory = os.getcwd()
output_folder = os.path.join(cur_directory, "Sheet_Files")

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for sht in excel_file.sheet_names:
    df = pd.read_excel(input_file, sheet_name=sht)
    for category in df["payment_method"].unique():
        newDf = df[df["payment_method"]==category]
        output_file = os.path.join(output_folder, f"{category}.xlsx")
        newDf.to_excel(output_file, sheet_name=category, index=False)



# Sheets to Sheet

input_file = "Sheet_Sheets.xlsx"
excel_file = pd.ExcelFile(input_file, engine='openpyxl')

datasets = [pd.read_excel(input_file, sheet_name=sht) for sht in excel_file.sheet_names]

output_data = pd.concat(datasets, ignore_index=True)

output_file = "Sheets_Sheet.xlsx"

output_data.to_excel(output_file, sheet_name="Data", index=False)




# Sheets to Files

input_file = "Sheet_Sheets.xlsx"
excel_file = pd.ExcelFile(input_file, engine='openpyxl')

cur_directory = os.getcwd()
output_folder = os.path.join(cur_directory, "Sheets_Files")

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for sht in excel_file.sheet_names:
    df = pd.read_excel(input_file, sheet_name=sht)
    output_file = os.path.join(output_folder, f"{sht}.xlsx")
    df.to_excel(output_file, sheet_name=sht, index=False)




# Files to Sheet
cur_directory = os.getcwd()
input_folder = os.path.join(cur_directory, "Sheets_Files")
output_file = "Files_Sheet.xlsx"
dfs = []
for file in os.listdir(input_folder):
    input_file = os.path.join(input_folder, file)
    excel_file = pd.ExcelFile(input_file, engine='openpyxl')
    for sht in excel_file.sheet_names:
        df = pd.read_excel(input_file, sheet_name=sht)
        if not dfs:
            print("n")
        dfs.append(df)

newDf = pd.concat(dfs, ignore_index=True)
print(newDf)

newDf.to_excel(output_file, sheet_name="Data", index=False)




# Files to Sheets
cur_directory = os.getcwd()
input_folder = os.path.join(cur_directory, "Sheets_Files")
output_file = "Files_Sheets.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as output:
    for file in os.listdir(input_folder):
        input_file = os.path.join(input_folder, file)
        excel_file = pd.ExcelFile(input_file, engine='openpyxl')
        for sht in excel_file.sheet_names:
            df = pd.read_excel(input_file, sheet_name=sht)
            df.to_excel(output, sheet_name=sht, index=False)