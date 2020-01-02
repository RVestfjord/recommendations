#!/usr/bin/env python3

import os
from sys import argv
from time import sleep
MAIL_DIR = "./recommendations"
OUTPUT = "recommendations.csv"

if len(argv) == 2:
    MAIL_DIR = argv[1]
elif len(argv) == 3:
    OUTPUT = argv[2]

print("Processing emails in directory: {}".format(MAIL_DIR))
print("Writing putput to file: {}".format(OUTPUT))

with open(OUTPUT, "w") as out:
    for root, dirs, files in os.walk(MAIL_DIR):
        for file_count, name in enumerate(files):

            print("Processed files: {}".format(file_count), end="\r")
            sleep(0.5)

            with open(os.path.join(root, name)) as f:
                lines = list(f)

            start = 0
            for count, line in enumerate(lines):
                if line.startswith("==="):
                    start = count+5
                lines[count] = line.rstrip()
            out.write(" ".join(lines[start:]))
            out.write("\n")

        print("")