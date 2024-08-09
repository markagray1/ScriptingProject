# ScriptingProject

## Overview

This script automates the processing of complaint files in CSV and JSON formats. It is designed to:

- Unpack ZIP files containing complaint data.
- Parse and store relevant complaint information into a master CSV file.
- Remove duplicate records from the master file.
- Generate reports based on specific products, showing related complaints and companies involved.

## Features

- **Setup and Initialization**: Automatically sets up a directory structure for managing complaint files.
- **File Unpacking**: Extracts complaint data from ZIP archives and processes JSON files.
- **Data Cleaning**: Removes duplicate complaint records from the master CSV file.
- **Reporting**: Generates product-based reports showing the number of complaints, involved companies, and specific issues.

## CRUD Operations

### Create

- **Setup (`setup` function)**: The script creates a directory structure and initializes a master CSV file to store complaint data.
- **Unpacking (`unpacking` function)**: New complaint records are parsed from JSON files and appended to the master CSV file.

### Read

- **Reporting (`report` function)**: The script reads the master CSV file to generate reports based on user input. It allows the user to select a product and view related complaints, including the number of companies involved and specific issues.

### Update

- **Cleanup (`cleanup` function)**: The script updates the master CSV file by removing duplicate records, ensuring that only unique complaint records are stored.

### Delete

- **Cleanup (`cleanup` function)**: After removing duplicates, the script deletes the old master CSV file and replaces it with a new one containing only unique records.
