import syslogCheck
import importlib

importlib.reload(syslogCheck)


# SSH authentication failures

def klog_fail(filename, searchterms):
    # Call Syslog Check
    is_found = syslogCheck._syslog(filename, searchterms)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:
        # Split results
        sp_results = eachFound.split(" ")

        # Append split to found
        found.append(sp_results[4])

    # Remove duplicates
    # and convert the list to a set.
    hosts = set(found)

    for eachHost in hosts:

        print(eachHost)
