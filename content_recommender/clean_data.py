
from zipfile import ZipFile
import os
import csv
import numpy as np

GENRES = {'Musical', 'Crime', 'Comedy', 
          'Adventure', 'War', 'Animation', 
          'Thriller', 'Drama', 'Western', 
          'Family', 'Fantasy', 'Music', 'Action', 
          'Biography', 'Sci-Fi', 'History', 'Sport', 
          'Horror', 'Mystery', 'Romance'}

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

def loadData(path):
    genres = {}
    directors = {}
    actors = {}
    row_count = 0

    with open(path, 'r') as f:
        data = csv.reader(f.readlines(), skipinitialspace=True)
    # skip header
    next(data)

    # on our first pass we need to count the actors and genres and convert them to numbers.
    for row in data:    
        # keep track of number of rows so we can allocate data.
        row_count = row_count + 1
        # process the genres...
        row_genres = row[2].split(',')
        for g in row_genres:
            if g not in genres:
                genres[g] = len(genres)
        
        # process the director.
        if row[4] not in directors:
            directors[row[4]] = len(directors)

        # process actors.
        row_actors = row[5].split(',')
        for a in row_actors:
            if a not in actors:
                actors[a] = len(actors)

    # now we have the necessary meta data to create numeric arrays.
    rv = np.zeros((row_count, 7 + len(genres) + len(directors) + len(actors)))
    print(rv.shape)