import os
import argparse
import logCheck

parser = argparse.ArgumentParser(

    description="Traverses a directory and builds a forensic body file",
    epilog="Written by Sam Johnson"
)
# Add Argument
parser.add_argument("-d", "--directory", required=True, help="Directory that you want to traverse.")
parser.add_argument("-s", "--searcher", required=True, help="Define a Yaml Book that contains search terms")

# Parse the arguments
args = parser.parse_args()

rootdir = args.directory

# print(rootdir)

# Traverse Directory
# Check in arg is a directory
if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()

# List to save files
flist = []

# Crawl through provided directory
for directory, subfiles, entries in os.walk(rootdir):
    for e in entries:
        print(e)

