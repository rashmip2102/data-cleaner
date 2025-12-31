# data-cleaner
## Overview
The data_cleaner script is a Python-based utility designed to streamline the preliminary steps of data preprocessing. It utilizes the pandas and numpy libraries to identify data issues and perform cleaning operations through a mix of automated logic and user input.
### Key Features
**Dataset Inspection:** Automatically displays df.info() and df.describe() to provide an immediate overview of data types and statistical distributions.
**Duplicate Removal:** Detects and removes exact duplicate rows.
1. **Missing Value Handling:** Fills empty cells with the string "Unknown".
   - Normalizes common placeholder strings (like "nan" or empty strings) to standard np.nan objects.
   - Uses Regex to identify and remove common special character noise (e.g., !@#$%^&*). 

**Interactive Type Casting:** Prompts the user to convert specific columns to Numeric or Datetime formats if they were incorrectly loaded as strings.
