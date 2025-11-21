# ===============================================================
# 1. WHAT IS PANDAS?
# ---------------------------------------------------------------
# Pandas is a Python library designed for DATA ANALYSIS and DATA HANDLING.
#
# What does data analysis mean at a basic level?
# - Loading data into Python
# - Checking how it looks
# - Cleaning incorrect or missing values
# - Selecting parts you want to use
# - Saving the processed data back into a file
#
# The name "Pandas" comes from:
#   PANel DAta = data tables (like spreadsheets)
#
# It is one of the most common tools for:
#   - Data science
#   - Database replacement for small projects
#   - Business analytics
#   - Automation of Excel tasks
#
# To use Pandas, we must install it (run one time):
#   pip install pandas
#
# ===============================================================


# ===============================================================
# 2. IMPORTING PANDAS
# ---------------------------------------------------------------
# It is a Python convention that Pandas is imported with the alias `pd`
# to make commands shorter and more readable.
# ===============================================================
import pandas as pd


# ===============================================================
# 3. PANDAS MAIN DATA STRUCTURES
# ---------------------------------------------------------------
# Pandas provides TWO major data structures:
#
# (A) SERIES
#     - A one-dimensional list
#     - Similar to one column in a spreadsheet
#     - Has both:
#         * values
#         * index (row labels)
#
# (B) DATAFRAME
#     - A two-dimensional table
#     - Looks like data in Excel or SQL
#     - Consists of multiple Series side by side as columns
#
# You will mostly work with DataFrames.
# ===============================================================


# ===============================================================
# 4. CREATING A SERIES
# ---------------------------------------------------------------
# Normally used when your data is only one column.
# ===============================================================
data = [100,102,103]
another_data = [100.1,102.3,103.5]
non_number = ["A","B","C"]
what_about_this = [True,False,True]
my_series = pd.Series(what_about_this)

print("=== Example Series ===")
print(my_series)
print()

print("=== Custom Index Series ===")
my_series = pd.Series(data,index=["a","b","c"])
so_we_can_do_this = pd.Series(data,index=["Apartment #1","Apartment #2","Apartment #3"])
print(my_series)
print()

print("=== location Series ===")
print(my_series.loc["a"])
print()
print("Change It")
my_series.loc["c"] = 200
print(my_series)
print()

print("Then There iloc")
print(my_series.iloc[1])

data = [100,102,104,200,202]

print("You must also take care of the label if there more value")
my_series = pd.Series(data,index=["a","b","c","d","e"])

print(my_series)
print()

print("=== Logic Indexing Series  ===")
print(my_series[my_series >= 200])
print()

print("=== Now What About Dictionary Series  ===")
calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700,
}

series = pd.Series(calories)
print(series)
print("Using LOC")
print(series.loc["Day 2"])
print()

print("Lets add")
series.loc["Day 3"] += 500

print("Now We can do checking!")
print("in what day does im not following my diet?")
print(series[series >= 2000])
print("in what day does im follow my diet plan")
print(series[series < 2000])
