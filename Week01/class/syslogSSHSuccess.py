# Code by Sam Johnson
# This code utilized the syslogCheck function to sort for users who succesfully
# authenticated with SSH. This is done by selecting a defined split target, and appending the
# split information to a formatted list, which is turned into a set before it is returned.
import syslogCheck
import importlib

importlib.reload(syslogCheck)


# SSH authentication successes

def ssh_success(filename, searchterms):
    # Call Syslog Check
    is_found = syslogCheck._syslog(filename, searchterms)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:
        # Split results
        sp_results = eachFound.split(" ")

        # Append split to found
        found.append(sp_results[5])

    # Remove duplicates
    # and convert the list to a set.
    hosts = set(found)

    for eachHost in hosts:

        print(eachHost)
