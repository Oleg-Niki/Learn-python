# CIS-117 Lab 3
# This module reads a CSV file containing country information and splits it into separate files by region.
# Each output file contains only the countries from a specific region, e.g. Europe.csv, Asia.csv, etc
# 
# Lab 3 Partner 1: 
# David Deng (inital code with basic reading and writing)
# Oleg Nikitashin (improvement, testing, error handling, GIT submission)
# 

import csv

def split_countries_by_region(input_file):
    """
    Reads CSV file of country data and creates separate files for each region
    No error handling - will crash on file access problems
    """
    # Dictionary to hold countries grouped by region
    regions = {}
    
    # Read the input file, as csv dictionary
    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            region = row['region']

            # Empty region is defaulted to "Other"
            if not region:  
                region = "Other"
            
            # If there's no region in dictonary, create a new dictionary with region name 
            if region not in regions:
                regions[region] = []

            # Add a new item to dictionary, that contains the country name and region.
            regions[region].append((row['name'], region))
    
    # Write separate files for each region by looping through its key ("region") and value (list of countries with its corresponding name and region)
    for region, countries in regions.items():
        output_file = f"{region}.csv"
        
        with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Country', 'Region'])  # Write header, it's fixed to country's name and region order
            writer.writerows(countries) # Write the countries array as multiple rows, ie each ("country name", "region") is it own row
        # For debugging to show what file's created and how many countries written in this file. 
        print(f"Created file: {output_file} with {len(countries)} countries")

# Main execution
if __name__ == "__main__":
    input_filename = "country_full.csv"
    split_countries_by_region(input_filename)