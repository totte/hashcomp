#!/usr/bin/env python3

# TODO Add optional third argument - hasher. Default to sha512.
# TODO Print error message explaining which file wasn't found.
# TODO Use colour, columns... something to make the output more legible.

import sys
import hashlib

def hashfile(filename, hasher, blocksize=65536):
    filebuffer = filename.read(blocksize)
    while len(filebuffer) > 0:
        hasher.update(filebuffer)
        filebuffer = filename.read(blocksize)
    return hasher.hexdigest()

try:
    with open(sys.argv[1], 'rb') as f:
        file1 = hashfile(f, hashlib.sha512())

    with open(sys.argv[2], 'rb') as f:
        file2 = hashfile(f, hashlib.sha512())

    if file1 == file2:
        print(sys.argv[1] + ", " + sys.argv[2] + ": MATCH")
    else:
        print(sys.argv[1] + ", " + sys.argv[2] + ": MISS")
except IndexError:
    print("Usage: " + sys.argv[0] + " <file1> <file2>")
except IOError:
    print("File not found: ")

