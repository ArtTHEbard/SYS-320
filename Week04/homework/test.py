import yaml

with open('searchbooks.yaml', 'r') as yf:
    keywords = yaml.safe_load_all(yf)

    for doc in keywords:
        print(doc)
