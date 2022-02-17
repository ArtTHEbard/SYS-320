# Code by Sam Johnson
# Create an interface to search through syslog files.
# This is done by opening the file, storing the contents in a variable,
# and looping through the elements within that variable, sorting them based upon inputted keywords.
# Finally, the resutls are formatted into a sorted list and returned.

import re
import sys
import yaml
import csv


# Open the YAML file

def _logs(filename, listofKeywords):

    # Open a file
    with open(filename, 'r') as f:
        # Read contents of file into variable
        contents = csv.reader(f)

        # Loop through the list returned.
        for line in contents:
            # Loops through the keywords.
            for eachKeyword in listofKeywords:
                # If the 'line' contains the keyword then it will print.
                # Searches and returns results using a regular expression search.
                x = re.findall(r'' + eachKeyword + '', line[1])
                for found in x:
                    args = line[1]
                    host = line[2]
                    name = line[3]
                    path = line[4]
                    pid = line[5]
                    user = line[6]
                    print("""
        
Arguments: {}
Host: {}
Name: {}
Path: {}
PID: {}
User: {}
{}
""".format(args, host, name, path, pid, user, "*" * 60))
