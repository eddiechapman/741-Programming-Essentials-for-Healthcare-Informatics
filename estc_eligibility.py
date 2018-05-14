# estc_eligibility.py
# This program inspects library records for ESTC eligibilty.

import csv

# Creates dictionary of British empire with MARC country codes as keys, and
# tuples of year of aquisition and year of independence as values.
def british_empire():
    infile = open('british_empire.csv', 'r')
    reader = csv.reader(infile)  # Create CSV object from file. 
    empire = {}
    for row in reader:
        # Unpack values from CSV row.
        (name, country, year_in, year_out) = row
        # Add values to British empire dictionary .
        empire[country] = (year_in, year_out)
    infile.close()
    return empire


# Reads CSV of library holdings. Calls comparison function to assess each
# library item, and prints the results to a new CSV.
def inspect_library(infile, outfile, empire):
    infile = open(infile, 'r')   
    outfile = open(outfile, 'w')
    reader = csv.reader(infile)  # Create CSV object from file. 
    for row in reader:
        # Unpack values from CSV row.
        (unique_id, language, country, date) = row
        # Pass values to "compare" function. Returns ESTC status. 
        status = check_criteria(language, country, date, empire)
        # Print CSV values and ESTC status to new CSV file. 
        print(unique_id, ',', language, ',', country, ',', date, ',',
              status, file=outfile)       
    infile.close()
    outfile.close()


# Receives values from library CSV. Determines ESTC status based on criteria.
def check_criteria(language, country, date, empire):
    # Checks if item made in British territory was made during British rule.
    if country in empire:
        # Unpack year range from empire dictionary.
        (year_in, year_out) = empire.get(country)
        # Test library item's year against empire country's year range.
        if year_in <= date <= year_out:
            status = 'eligible'
        else:
            status = 'ineligible (date)'  # Reason for ineligiblity is included.
    # All English language items are eligible, regardless of time or place.
    elif language == 'eng':
        status = 'eligible'
    else:
        status = 'ineligible (country)' 
    return(status)


# Introduction, gets file names, calls functions, concludes program.
def main():
    print('This program sorts a list of library items for ESTC-eligibility')
    empire = british_empire()
    infile = input('Enter the name of the library holdings file: ')
    outfile = input('Enter the name of the output file: ')
    estc = inspect_library(infile, outfile, empire)
    print('Done')

main()
