# Create an interface to search through syslog files.
import re


def _syslog(filename, listofKeywords):
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

            # If the 'line' contains the keyword then it will print
            # Searches and returns results using a regular expression search.
            x = re.findall(r''+eachKeyword+'', line)

            for found in x:
                # Append results to result list.
                results.append(found)

    return results
