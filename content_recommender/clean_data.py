
from zipfile import ZipFile
from sklearn.preprocessing import scale
import os
import csv
import numpy as np

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

# this function and enum converts the rating into a number between 0 and 4
# this is an ordinal feature.
VERY_HIGH_RATING = 1.0
HIGH_RATING = 0.75
AVERAGE_RATING = 0.5
LOW_RATING = 0.25
VERY_LOW_RATING = 0.0
def convertRatingToEnum(rating):
    if(rating > 950):
        return VERY_LOW_RATING
    if(rating > 800):
        return LOW_RATING 
    if(rating < 50):
        return VERY_HIGH_RATING
    if(rating < 200):
        return HIGH_RATING
    return AVERAGE_RATING

# this function and enum converts the length of the movie into a number 
# between 0 and 4.
VERY_LONG_RUNTIME = 1.0
LONG_RUNTIME = 0.75
AVERAGE_RUNTIME = 0.5
SHORT_RUNTIME = 0.25
VERY_SHORT_RUNTIME = 0
def convertLengthToEnum(length):
    if(length > 180):
        return VERY_LONG_RUNTIME
    if(length > 160):
        return LONG_RUNTIME 
    if(length < 60):
        return VERY_SHORT_RUNTIME 
    if(length < 120):
        return SHORT_RUNTIME
    return AVERAGE_RUNTIME

# this function converts the year into an enum.
NEW_RELEASE = 1.0
NOSTALGIC = 0.5
CLASSIC = 0.0
def convertYearToEnum(year):
    if year > 2015:
        return NEW_RELEASE
    if year > 1990:
        return NOSTALGIC
    return CLASSIC

def loadData(path):
    genres = {}
    row_count = 0
    Y = []

    with open(path, 'r') as f:
        data = csv.reader(f, skipinitialspace=True)
        # skip header
        next(data)

        # on our first pass we need to count the actors and genres and convert them to numbers.
        for row in data:    
            # Append the movie name to the Y vector so we can look it up later.
            Y.append(row[1])

            # keep track of number of rows so we can allocate data.
            row_count = row_count + 1
            # process the genres...
            row_genres = row[2].split(',')
            for g in row_genres:
                if g not in genres:
                    genres[g] = len(genres)

           
        # now we have the necessary meta data to create numeric arrays.
        X = np.zeros((row_count, 7 + len(genres)))

        # reset csv reader.
        f.seek(0)
        next(data)

        # calculate and cache offsets.
        genre_offset = 1
        year_offset = genre_offset + len(genres)
        runtime_offset = year_offset + 1
        rating_offset = runtime_offset + 1
        votes_offset = rating_offset + 1
        revenue_offset = votes_offset + 1
        metascore_offset = revenue_offset + 1

        # now actually load the data in a usable form.
        for i, row in enumerate(data):
            X[i,0] = convertRatingToEnum(int(row[0]))

            # process the genres into a vector of booleans
            for g in row[2].split(','):
                X[i,genre_offset+genres[g]] = 1

            # process the movie's year.
            X[i,year_offset] = convertYearToEnum(int(row[6]))

            # process the movie's runtime.
            X[i,runtime_offset] = convertLengthToEnum(int(row[7]))

            # the rest of the data is actually ordinal so we just use it as is.
            X[i, rating_offset] = float(row[8])
            X[i, votes_offset] = float(row[9])
            try:
                X[i, revenue_offset] = float(row[10])
            except:
                X[i, revenue_offset] = 0

            try:
                X[i, metascore_offset] = float(row[11])
            except:
                X[i, metascore_offset] = 0
    # normalize ordinal data.
    #rv[:,rating_offset:] = scale(rv[:,rating_offset:], axis=0, with_mean=True, with_std=True)
    return (X,Y)

 
