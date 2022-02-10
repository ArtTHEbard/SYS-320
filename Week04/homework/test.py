import yaml

with open('searchbooks.yaml', 'r') as yf:
    keywords = yaml.safe_load_all(yf)

    for key in keywords:
        print(key)

