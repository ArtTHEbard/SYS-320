import re
import sys
import yaml


# Open the YAML file
def _logs(service):
    with open('searchbooks.yaml', 'r') as yf:
        keywords = yaml.safe_load_all(yf)

    # Query the yaml file for term or direction and
    # retrieve the strings to search on.

        for keyVal in keywords:
            for key, value in keyVal[service].items():
                print(value)


p = _logs('shell_attacks')
