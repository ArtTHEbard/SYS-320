# Code by Sam Johnson
# Create an interface to search through syslog files.
# This is done by opening the file, storing the contents in a variable,
# and looping through the elements within that variable, sorting them based upon inputted keywords.
# Finally, the resutls are formatted into a sorted list and returned.

import re
import sys
import yaml


def logs(filename, bookname):
    # Query the yaml file for term or direction and
    # retrieve the strings to search on.
    try:
        with open(bookname, 'r') as yf:
            keywords = yaml.safe_load(yf)
    except EnvironmentError as e:
        print(e.strerror)

    keywordlist = []

    for type in keywords:
        for value in type:
            keywordlist.append(value)
    # Open a file
    with open(filename) as f:
        # Read contents of file into variable
        contents = f.readlines()

    # List to store results.
    results = []

    # Loop through the list returned.
    for line in contents:

        # Loops through the keywords.
        for eachKeyword in keywordlist:

            # If the 'line' contains the keyword then it will print.
            # Searches and returns results using a regular expression search.
            x = re.findall(r'' + eachKeyword + '', line)

            for found in x:
                # Append results to result list.
                results.append(found)

    # Check to see if results exists.
    if len(results) == 0:
        print("No Results")
        sys.exit()
    # Sort List.
    results = sorted(results)

    return results
