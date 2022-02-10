import re
import sys
import yaml


# Open the YAML file
def _logs(service):
    with open('searchbooks.yaml', 'r') as yf:
        keywords = yaml.load(yf, Loader=yaml.FullLoader)


    # Query the yaml file for term or direction and
    # retrieve the strings to search on.

        terms = []
        for entry in keywords:
            terms.append(keywords[entry])
            for term in terms:
                for key, value in term.items():
                    print(value)


p = _logs('shell_attacks')
