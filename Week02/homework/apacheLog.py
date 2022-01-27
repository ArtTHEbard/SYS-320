# Code by Sam Johnson
# This code utilized the syslogCheck function to sort for domains that failed to authenticate with SSH.
# This is done by selecting a defined split target, and appending the
# split information to a formatted list, which is turned into a set before it is returned.
import logCheck
import importlib
importlib.reload(logCheck)


# SSH authentication failures

def apache_event(filename, service, term):
    # Call log Check
    is_found = logCheck._logs(filename, service, term)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:
        # Split results
        sp_results = eachFound.split(" ")

        # Append split to found
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + sp_results[7])

    # Remove duplicates
    # and convert the list to a set.
    getValues = set(found)

    for eachValue in getValues:

        print(eachValue)
