
from zipfile import ZipFile
import os
import csv

def unzipData(path):
    with ZipFile(path, 'r') as zipObj:
        zipObj.extractall()

def cleanupFile(path):
    if os.path.exists(path):
        os.remove(path)

def findAllGenres(path):
    # store genres in a set
    all_genres = set([])

    # load csv data.
    with open(path, 'r') as f:
        data = csv.reader(f.readlines(), skipinitialspace=True)
    # skip csv header.
    next(data)

    # for each row of data.
    for row in data:
        # get a list of the genres.
        genres = row[2].split(',')
        [all_genres.add(x) for x in genres]

    print(all_genres)