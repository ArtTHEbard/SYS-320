# File to traverse a given directory and retrieve files.

import os
import argparse
import stat

parser = argparse.ArgumentParser(

    description="Traverses a directory and builds a forensic body file"
)
# Add Argument
parser.add_argument("-d", "--directory", required=True, help="Directory that you want to traverse.")

# PArse the arguments
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
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        filelist = root + "/" + f
        flist.append(filelist)


def statFile(toStat):
    # i is going to be the variable used for each of the metadata elements
    i = os.stat(toStat, follow_symlinks=False)

    # mode
    mode = i[0]

    # inode
    inode = i[1]

    # uid
    uid = i[4]

    # gid
    gid = i[5]

    # file size
    fsize = i[6]

    # access time
    atime = i[7]

    # mod time
    mtime = i[8]

    # ctime
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))


for eachFile in flist:
    statFile(eachFile)
