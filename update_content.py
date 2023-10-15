#!/bin/python3

import os
from os.path import join


for root, dirs, files in os.walk('.'):
    with open(join(root,"CONTENT"), "w") as f:
        for d in dirs:
            if d != ".git":
                f.write(d + "\n")
        for file in files:
            if file != "CONTENT" and file != ".htaccess" and file != ".git":
                f.write(file+"\n")

