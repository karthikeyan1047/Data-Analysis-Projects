from tkinter import simpledialog
import numpy as np
import pandas as pd
import stat, shutil, os, time
from datetime import datetime

# --------------------------
# LIST
# --------------------------

# print one by one 
list = [1,2,3,4,5]

print('One by One')
for i in list:
    if i%2==0:
        print(i)

# print as a list 
list = [1,2,3,4,5]
even_list = [i for i in list if i%2==0]
print("As a List")
print(even_list)

# range for list
list = range(1, 6)
even_list = [i for i in list if i%2==0]
print(even_list)

# Enumerate - List
list = ['one', 'two', 'three', 'four', 'five']
list_with_index = [(idx, val) for idx, val in enumerate(list, start=1)]
print(list_with_index)


# List Merging
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

merged_list = list1 + list2

for i in merged_list:
    print(i)

# List Zipping
list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']

zipped_list = zip(list1, list2)

for a,b in zipped_list:
    print(f"{a} : {b}")

# --------------------------
# DICTIONARY
# --------------------------

# Dictionary Key Looping
dictionary = {
    "A" : "Apple",
    "B" : "Ball",
    "C" : "Cat",
}

# Dictionary Key Looping
for key in dictionary:
    print(key)

# Dictionary Value Looping
for key in dictionary:
    print(dictionary[key])

# Dictionary Key and Value Looping
for key, value in dictionary.items():
    print(f"{key} : {value}")

# Dictionary Key and Value Looping with Index
for idx, (key, value) in enumerate(dictionary.items(), start=1):
    print(f"{idx} : {key} : {value}")

# Mapping

extensions = {
    1: ".xlsx",
    2: ".xlsm",
    3: ".xlsb",
    4: ".xls",
    5: ".csv"
}
fl_format = simpledialog.askinteger("Extension", "Choose\n1. xlsx\n2. xlsm\n3. xlsb\n4. xls\n5. csv\n")
extention = extensions.get(fl_format, None)

print(extention)


# Print aging bin based on user input
def fxswitch(x):
    age_bin_dictionary  = {
        range(1, 26) : "1-25",
        range(26, 51) : "26-50",
        range(51, 101) : "51-100",

    }
    for a,b in age_bin_dictionary.items():
        if x in a:
            return b
    return None
age = simpledialog.askinteger("Age", "Type the age") 

print(fxswitch(age))


# ----------------
# DATA ANALYSIS
# ----------------

# Create a dataset using numpy

n_rows = 50
dates = np.arange(
    np.datetime64('2025-01-01'),
    np.datetime64('2025-01-01') + n_rows
)
categories = np.array([
    "Food", "Clothing", "Electronics", "Books", "Health",
    "Sports", "Travel", "Entertainment", "Home", "Other"
])

categories_col = np.random.choice(categories, size=n_rows)
amounts = np.round(np.random.uniform(150, 900, size=n_rows), 2)

df = pd.DataFrame({
    "Date": dates,
    "Category": categories_col,
    "Amount": amounts
})

df["Date"] = pd.to_datetime(df["Date"]).dt.date

df.to_excel("purchases.xlsx", index=False)
df.to_csv("purchases.csv", index=False)

# Load csv
df = pd.read_csv('purchases.csv')
print(df.to_string(index=False))

# Load Excel - First Sheet
df = pd.read_excel('purchases.xlsx')
print(df.to_string(index=False))

# Load Excel - Specified Sheet
df = pd.read_excel('purchases.xlsx', sheet_name="Data")
print(df.to_string(index=False))

# Load Excel - All Sheets
df = pd.read_excel('purchases.xlsx', sheet_name=None)
print(df["Sheet1"].to_string(index=False))
print("-"*30)
print(df["Data"].to_string(index=False))


# Append All Sheets
datasets = pd.read_excel('purchases.xlsx', sheet_name=None)
dataset = pd.concat(datasets, ignore_index=True)

print(dataset.to_string(index=False))

# Add a Column
dataset['Date'] = pd.to_datetime(dataset['Date'])
dataset['MonthNum'] = dataset['Date'].dt.month                      # 1 to 12
dataset['MonthName'] = dataset['Date'].dt.month_name()              # January to December
dataset['MonthName_Short'] = dataset['Date'].dt.strftime('%b')      # Jan to Dec
dataset['MonthPeriod'] = dataset['Date'].dt.to_period('M')          # 2026-01 to 2026-12


# Add a Conditional column
conditions = [
    (dataset['Experience'] >= 1) & (dataset['Experience'] <= 3),
    (dataset['Experience'] >= 4) & (dataset['Experience'] <= 7),
    (dataset['Experience'] >= 7) & (dataset['Experience'] <=15),
    (dataset['Experience'] > 15)
]

values1 = dataset['Name'] + ' is a Fresher'
values2 = dataset['Name'] + ' is an Experienced'
values3 = dataset['Name'] + ' is a Team Lead'
values4 = dataset['Name'] + ' is a Manager'

values = [values1, values2, values3, values4]

dataset['Description'] = np.select(conditions, values)

# Replacing values
replacement_map = {
    'A': 'Review',					
    'B': 'Pending',				
    'C': 'Approved'
}
df['Status'] = df['Agency'].map(replacement_map)            # map - change the value to new value if present in the dictionary otherwise it will be NaN
df['Status'] = df['Agency'].replace(replacement_map)        # replace - change the value to new value  if present in the dictionary otherwise it will be old value
print(df)


# Filtering Table
filtered_df = df[(df['Episodes'] > 15) & (df['Category'] == 'Series')] 
print(filtered_df)

filtered_df = df[(df['Genre'] == 'Comedy') | (df['Gender'] == 'Horror')] 
print(filtered_df)

lst = ['Comedy', 'Horror']
filtered_df = df[df['Genre'].isin(lst)] 
print(filtered_df)

filtered_df = df[df['Year'].between(2020, 2024)] 
print(filtered_df)

filtered_df = df[df['Genre'].str.contains('horrer', case=False)] 
print(filtered_df)

pattern = 'horror|comedy'
mask = dataset['Genre'].str.contains(pattern, case=False, na=False)
print(dataset[mask])


# Grouping Table
grouped_df = df.groupby('Product')['Price'].sum()
print(grouped_df)


mean_df = df.groupby('Department').first() 
print(mean_df)	


grouped_df = df.groupby(['Category', 'Sub-Category'])['Price'].sum()
print(grouped_df)


grouped_df = df.groupby(['Category', 'Sub-Category'])['Price'].agg(['sum', 'mean'])
print(grouped_df)


agg_result = df.groupby(['Category', 'Subcategory']).agg({
    'Value1': 'sum',        # Sum of Value1
    'Value2': 'mean'        # Mean of Value2
})

print(agg_result)


grouped = df.groupby(['Region', 'Category']).agg({
    'Sales': ['sum', 'mean', 'max']
})
print(grouped)


agg_df = df.groupby('Department').agg({
'Salary': ['mean', 'sum', 'max', 'min'], 
'Experience': ['mean', 'std'] 
}) 
print(agg_df)


# Group and Filter

grouped = df.groupby('Category')['Value'].sum()
filtered_groups = grouped[grouped > 50]
print(filtered_groups)


grouped = df.groupby(['Category', 'Region'])['Value'].sum()
filtered = grouped[(grouped > 50) & (grouped < 150)]
print(filtered)



# Pivot Table
pivot_table = pd.pivot_table(df, index='Date', columns='City', values='Temperature', aggfunc='mean')
pivot_table = pd.pivot_table(df, index='Date', columns='Product', values='Sales', aggfunc=['sum', 'mean'])
pivot_table = pd.pivot_table(df, index=['Category', 'Type'], values=['Value1', 'Value2'], aggfunc='sum')
pivot_table = pd.pivot_table(df, index=['Dates','Columns1'], values=['Values1','Values2'], aggfunc={'Values1':['sum','mean'], 'Values2':'mean'})


# Merge/Join tables
customers = pd.read_csv("customers.csv", parse_dates=["signup_date"])
regions = pd.read_csv("regions.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv", parse_dates=["order_date"])
order_items = pd.read_csv("order_items.csv")
payments = pd.read_csv("payments.csv", parse_dates=["payment_date"])


sales_df = (
    order_items
    .merge(orders, on="order_id", how="left")
    .merge(customers, on="customer_id", how="left")
    .merge(products, on="product_id", how="left")
    .merge(regions, on="region_id", how="left")
    .merge(payments, on="order_id", how="left")
)



# ----------------------
# EXCEL FILE HANDLING
# ----------------------


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



# keep only the latest n folder

main_folder = '___folderpath___'
keep_count = int(simpledialog.askstring("Folder", "Enter the number folders to keep"))

def wirte_access(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

flds_to_delete = [
    os.path.join(main_folder, fld) 
    for fld in os.listdir(main_folder) 
    if os.path.isdir(os.path.join(main_folder, fld))
]
flds_to_delete.sort(key=os.path.getmtime, reverse=True)     # reverse = False --- to keep n oldest folders
flds_to_delete = flds_to_delete[keep_count:]

for f in flds_to_delete:
    shutil.rmtree(f, onerror=wirte_access)



# keep only the latest n files

main_folder = "__folderpath___"
keep_count = int(simpledialog.askstring("Folder", "Enter the number files to keep"))
files_to_delete = [
    os.path.join(main_folder, file)
    for file in os.listdir(main_folder)
    if os.path.isfile(os.path.join(main_folder, file))
]
files_to_delete.sort(key=os.path.getmtime, reverse=True)     # reverse = False --- to keep n oldest files
files_to_delete = files_to_delete[keep_count:]
for file in files_to_delete:
        os.remove(file)



# Get Timestamp of Folder/ File

file_path = 'payments.xlsx'

creation_time = os.path.getctime(file_path)
modification_time = os.path.getmtime(file_path)
access_time = os.path.getatime(file_path)

print("Creation Time:", time.ctime(creation_time))
print("Modification Time:", time.ctime(modification_time))
print("Last Access Time:", time.ctime(access_time))


# Change Timestamp of Folder/ File

cur_directory = os.getcwd()
file_path = os.path.join(cur_directory, 'payments.xlsx')

new_time = datetime(2020, 1, 1, 12, 0, 0).timestamp()

os.utime(file_path, (new_time, new_time))