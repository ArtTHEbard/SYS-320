# Code by Sam Johnson
# Create an interface to search through syslog files.
# This is done by opening the file, storing the contents in a variable,
# and looping through the elements within that variable, sorting them based upon inputted keywords.
# Finally, the resutls are formatted into a sorted list and returned.

import re
import sys
import yaml


# Open the YAML file

def _logs(filename, service):
    with open('searchbooks.yaml', 'r') as yf:
        keywords = yaml.safe_load_all(yf)

    # Query the yaml file for term or direction and
    # retrieve the strings to search on.

        listofKeywords = []
        for keyVal in keywords:
            for key, value in keyVal[service].items():
                listofKeywords.append(value)
        # Open a file
        with open(filename) as f:
            # Read contents of file into variable
            contents = f.readlines()

        # List to store results.
        results = []

        # Loop through the list returned.
        for line in contents:
            # Loops through the keywords.
            for eachKeyword in listofKeywords:

                # If the 'line' contains the keyword then it will print.
                # Searches and returns results using a regular expression search.
                x = re.findall(r'' + eachKeyword + '', line)
                for found in x:

                    # Append results to result list.
                    results.append(found)

        # Check to see if results exists.
        if len(results) == 0:
            print("No Results")
        # Sort List.
        results = sorted(results)

        return results
