#! python3
"""Requirements:
    1. Reads the data from the Excel spreadsheet.
    2. Coutns the number of census tracts in each county.
    3. Counts the total population of each county.
    4. Prints the results.
    ----
    The Code needs the following:
    1. Open and read the cells of an Excel document with the openpyxl module.
    2. Calculate all the tract and population data and store it in a data structure.
    3. Write the data structure to a text file with the .py extension using the pprint module.
"""
import os
import logging
import openpyxl as excel
import pprint

# Setup
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.chdir(os.path.dirname(os.path.realpath(__file__)))
logging.debug("--- Program starts! ---")


wb = excel.load_workbook('censuspopdata.xlsx')
sheet = wb.active
county_data = {}

# Fill in county_data with each county's population and tracts.
# Starting from Row 2...
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    population = sheet['D' + str(row)].value

    # make sure the key for this state exists.
    county_data.setdefault(state, {}) # Output: county_data { State {} }
    # Make sure the the key for this county in this state exists.
    # NOTE: setdefault will do nothing if the key exists, you can call it on every iteration without a problem.
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0}) # Output: county_data { State {'tract': 0, 'pop': 0} }
    # Each row represents one census tract, so increment by one.
    county_data[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    county_data[state][county]['pop'] += int(population)

# Open a new text file and write the contents of county_data to it.
print('Writing results...')
with open('census2010.py', 'w') as output_file:
    output_file.write('allData = ' + pprint.pformat(county_data))
print("Finished.")
logging.debug("--- Program finished! ---")
