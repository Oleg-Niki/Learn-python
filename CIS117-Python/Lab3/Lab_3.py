# CIS-117 Lab 3
# This module reads a CSV file containing country information and splits it into separate files by region.
# Each output file contains only the countries from a specific region, e.g. Europe.csv, Asia.csv, etc
# 
# Lab 3 Partner 1: 
# David Deng (inital code with basic reading and writing)
# Oleg Nikitashin (improvement, testing, error handling, GIT submission)
# 

import os
import csv

def split_countries_by_region(input_file):
    """
    Reads a CSV file containing country data and creates separate CSV files 
    for each region (e.g., Europe.csv, Asia.csv, etc.). 
    Includes improvements for error handling and testing.
    
    Parameters:
        input_file (str): The path to the CSV file containing country information.
    """
    # Dictionary for grouping countries by region.
    regions = {}

    # Attempt to open and read the CSV file.
    try:
        with open(input_file, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Process each row in the CSV file.
            for row in reader:
                try:
                    # Retrieve the region and use "Other" if empty.
                    region = row.get('region', '').strip()
                    if not region:
                        region = "Other"
                    
                    # Create a new list for this region if not already present.
                    if region not in regions:
                        regions[region] = []
                    
                    # Append a tuple containing the country name and region.
                    regions[region].append((row['name'], region))
                except KeyError as e:
                    print(f"Error: Missing expected column in the CSV file: {e}")
                    continue
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except IOError:
        print(f"Error: Could not read file '{input_file}'.")
        return
    
    input_directory = os.path.dirname(os.path.abspath(input_file))
    # Write separate CSV files for each region.
    for region, countries in regions.items():
        output_file = os.path.join(input_directory, f"{region}.csv")
        try:
            with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['Country', 'Region'])  # Write header.
                writer.writerows(countries)             # Write country data rows.
            print(f"Created file: {output_file} with {len(countries)} countries")
        except IOError as e:
            print(f"Error writing to file '{output_file}': {e}")

if __name__ == "__main__":
    # Update the input filename with the absolute path if needed.
    input_filename = "c:/Users/nikit/Learn-python/Learn-python-16/CIS117-Python/Lab3/country_full.csv"
    split_countries_by_region(input_filename)
