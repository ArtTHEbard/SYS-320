import syslogCheck


# SSH authentication failures

def ssh_fail(filename, searchterms):
    # Call Syslog Check
    is_found = syslogCheck._syslog(filename, searchterms)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        # Split results
        sp_results = eachFound.split(" ")

        # Append split to found
        found.append(sp_results[8])


    print(found)
