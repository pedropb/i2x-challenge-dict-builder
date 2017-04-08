from zipfile import ZipFile
import os, sys
from shutil import rmtree 
from numpy import random

FILENAME = "Word-lists-in-csv.zip"
PATH = "Word lists in csv/"
WORDS_FILE = "words.txt"

def extract_zip(filename):
    if os.path.exists(PATH):
        rmtree(PATH)

    z = ZipFile(filename)
    z.extractall()
    z.close()

def concatenate_files(dir_path, output_file):
    files = [os.path.join(dir_path, f) 
        for f in os.listdir(os.path.join(".", dir_path))
        if os.path.isfile(os.path.join(dir_path, f))
    ]

    with open(output_file, 'w') as out:
        for f in files:
            print("Reading " + f)
            with open(f, 'r') as inp:
                out.write(inp.read())

def load_dictionary(words_file):
    dictionary = set()
    with open(words_file, 'r') as words:
        for word in words:
            dictionary.add(word.strip().lower())

    return list(dictionary)

extract_zip(FILENAME)
concatenate_files(PATH, WORDS_FILE)
dictionary = load_dictionary(WORDS_FILE)

print("Printing 30 random words")
print(random.choice(dictionary, 30))


