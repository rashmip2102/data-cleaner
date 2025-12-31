# data-cleaner
## Overview
The data-cleaner script is a Python-based utility designed to streamline the preliminary steps of data preprocessing. It utilizes the pandas and numpy libraries to identify data issues and perform cleaning operations through a mix of automated logic and user input.
### Key Features
- **Dataset Inspection:** Automatically displays df.info() and df.describe() to provide an immediate overview of data types and statistical distributions.
- **Duplicate Removal:** Detects and removes exact duplicate rows.
- **Missing Value Handling:** Fills empty cells with the string "Unknown".
   - Normalizes common placeholder strings (like "nan" or empty strings) to standard np.nan objects.
   - Uses Regex to identify and remove common special character noise (e.g., !@#$%^&*). 

- **Interactive Type Casting:** Prompts the user to convert specific columns to Numeric or Datetime formats if they were incorrectly loaded as strings.
## Prerequisites
Before running the script, ensure you have the following libraries installed:
```bash
pip install pandas numpy
```
## How to Use
1. Run the Script: Execute the Python file.
2. Provide File Path: When prompted, enter the full path to your .csv file (e.g., C:/Users/Documents/data.csv).
3. Review Statistics: The script will output the structural summary of your data.
4. Interactive Conversions:
   - Numeric: If you have columns that look like numbers but are stored as text, enter the count and provide the column names.
   - Dates: If you have date/time columns stored as text, enter the count and provide the column names for conversion.
5. Output: The script prints the final cleaned DataFrame to the console.
## Code Logic Highlights
The script follows a systematic pipeline to transform raw data into a clean, usable format. Below is the step-by-step logic breakdown:
### 1. Data Loading & Path Handling
The script prompts the user for a file path and uses `.strip(' "')` to ensure that even if the path is copied with quotes, the system reads it correctly.
### 2. Cleaning Pipeline
The table below describes the sequential logic applied to the DataFrame:
| Step | Action | Logic / Implementation |
| :--- | :--- | :--- |
| **1** | **Loading** | Reads the `.csv` file into a Pandas DataFrame. |
| **2** | **Deduplication** | Runs `df.duplicated().sum()` to identify redundancy and drops identical rows. |
| **3** | **Standardization** | Normalizes "fake" nulls by replacing empty strings `''` and text strings `'nan'` with true `np.nan` objects. |
| **4** | **Regex Cleaning** | Uses Regular Expressions to strip out special character noise (like `!@#$%^&*`) that often corrupts text data. |
| **5** | **Type Coercion** | Converts "Object" columns to **Numeric** or **Datetime** based on user input, using `errors='coerce'` to handle unparseable values safely. |
### 3. Missing Value Strategy
Instead of leaving gaps, the script implements an "Unknown" fill strategy for initial processing:
* **Primary Fill:** `df.fillna('Unknown')` ensures that categorical analysis doesn't break due to null values.
* **Secondary Refinement:** Subsequent replacements ensure that technical noise is converted to a consistent `NaN` format for easier filtering later.
---
**Note:** This script modifies data in-memory. To save the results, you should add df.to_csv('cleaned_data.csv') at the end of the function.
