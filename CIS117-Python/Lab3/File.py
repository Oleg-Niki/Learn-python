#!/usr/bin/env python3

"""
CIS-117 Lab3
Description: This module processes a CSV file containing country information, splits it by region,
and writes separate CSV files for each region. Each output file retains only the country name and region.
Author: [Your Name]
Group: [Your Group Number] – Partners: [Partner Names, if applicable]
Collaboration: Describe briefly how the work was divided (e.g., one partner handled file reading, the other handled writing).
"""

import csv

def read_csv(input_filename):
    """
    Reads the CSV file and groups country data by region.
    
    Args:
        input_filename (str): Name/path of the input CSV file.
        
    Returns:
        dict: A dictionary with regions as keys and a list of rows (each containing country info) as values.
    """
    # TODO: Implement file reading using 'with'
    # TODO: Use exception handling (try/except) for errors like FileNotFoundError, IOError, PermissionError
    # TODO: Read the header row and determine the indices for "Country Name" and "Region"
    # TODO: Loop through each row, extract the country and region, and group them accordingly
    pass

def write_region_files(region_data):
    """
    Writes separate CSV files for each region with the grouped country data.
    
    Args:
        region_data (dict): Dictionary where keys are regions and values are lists of corresponding rows.
    """
    # TODO: For each region in the dictionary:
    #       - Construct an output filename (e.g., "Europe.csv")
    #       - Open the file using 'with' in write mode
    #       - Write the header (if required) containing "Country Name" and "Region"
    #       - Write each row (only country name and region) to the file
    #       - Include try/except blocks to handle any file I/O errors
    pass

def main():
    # Define the input CSV file name (update the path if necessary)
    input_filename = "country_full.csv"
    
    # 1. Read the CSV and group data by region
    region_data = read_csv(input_filename)
    
    # 2. Write out each region's data into separate CSV files
    write_region_files(region_data)
    
    # Optional: Add any testing or log statements as needed (e.g., printing a success message)
    # print("Output files have been created successfully.")

if __name__ == '__main__':
    main()
