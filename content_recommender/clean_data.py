
from zipfile import ZipFile
import os
import csv
import numpy as np
import collections

def unzipData(path):
    with ZipFile(path, 'r') as zipObj:
        zipObj.extractall()

def cleanupFile(path):
    if os.path.exists(path):
        os.remove(path)

ratingDict = collections.OrderedDict([
    ('Very High Rating (>9)',(9,4)),
    ('High Rating (8-9)',(8,3)),
    ('Average Rating (6-8)',(6,2)),
    ('Low Rating (4-6)',(4,1)),
    ('Very Low Rating (<4)',(0,0)),
])

lengthDict = collections.OrderedDict([
    ('Very Long (>3h)',(180,4)),
    ('Long (2-3h)',(120,3)),
    ('Average (1.5-2h)',(90,2)),
    ('Short (1-1.5h)',(60,1)),
    ('Very Short (0-1h)',(0,0)),
])

releaseDateDict = collections.OrderedDict([
    ('New Release (>2016)',(2016,2)),
    ('nostalgic (2008-2016)',(2008,1)),
    ('classic (<2008)',(0,0)),
])

ratingCountDict = collections.OrderedDict([
    ('Lots of Ratings (>100k)',(100000,2)),
    ('Some Ratings (10k-100k)',(10000,1)),
    ('Few Ratings (<10k)',(0,0)),
])

revenueDict = collections.OrderedDict([
    ('Blockbuster (>300m)',(300,4)),
    ('High Revenue (100-300m)',(100,3)),
    ('Average Revenue (50-100m)',(50,2)),
    ('Low Revenue (5-50m)',(5,1)),
    ('Epic Failure (0-5m)',(0,0)),
])

metaScoreDict = collections.OrderedDict([
    ('Very High (>90)',(90,4)),
    ('High (70-90)',(70,3)),
    ('Average (50-70)',(50,2)),
    ('Low (30-50)',(30,1)),
    ('Very Low (<30)',(0,0)),
])

genreDict = {}

# convert a value to its new ordinal value given the value and a data dictionary.
def convertValue(data, value):
    for v in data.values():
        if value >= v[0]:
            return v[1]
    
def selectionToInputVector(genres, release_date, length, rating, num_ratings, revenue, meta_score):
    rv = np.zeros(6+len(genreDict))

    # fill in genres...
    for genre in genres:
        rv[genreDict[genre]] = 1

    rv[len(genreDict)] = releaseDateDict[release_date][1]
    rv[len(genreDict)+1] = lengthDict[length][1]
    rv[len(genreDict)+2] = ratingDict[rating][1]
    rv[len(genreDict)+3] = ratingCountDict[num_ratings][1]
    rv[len(genreDict)+4] = revenueDict[revenue][1]
    rv[len(genreDict)+5] = metaScoreDict[meta_score][1]
    return rv

def loadData(path):
    row_count = 0
    Y = []

    with open(path, 'r') as f:
        data = csv.reader(f, skipinitialspace=True)
        # skip header
        next(data)

        # on our first pass we need to count the actors and genres and convert them to numbers.
        for row in data:    
            # Append the raw vector so we can look it up laters.
            Y.append(row)

            # keep track of number of rows so we can allocate data.
            row_count = row_count + 1
            # process the genres...
            row_genres = row[2].split(',')
            for g in row_genres:
                if g not in genreDict:
                    genreDict[g] = len(genreDict)

           
        # now we have the necessary meta data to create numeric arrays.
        X = np.zeros((row_count, 6 + len(genreDict)))

        # reset csv reader.
        f.seek(0)
        next(data)

        # calculate and cache offsets.
        genre_offset = 0
        year_offset = genre_offset + len(genreDict)
        runtime_offset = year_offset + 1
        rating_offset = runtime_offset + 1
        votes_offset = rating_offset + 1
        revenue_offset = votes_offset + 1
        metascore_offset = revenue_offset + 1

        # now actually load the data in a usable form.
        for i, row in enumerate(data):
            # process the genres into a vector of booleans
            for g in row[2].split(','):
                X[i,genre_offset+genreDict[g]] = 1

            # process the movie's year.
            X[i,year_offset] = convertValue(releaseDateDict, int(row[6]))

            # process the movie's runtime.
            X[i,runtime_offset] = convertValue(lengthDict ,int(row[7]))

            # the rest of the data is actually ordinal so we just use it as is.
            X[i, rating_offset] = convertValue(ratingDict, float(row[8]))
            X[i, votes_offset] = convertValue(ratingCountDict, float(row[9]))
            try:
                X[i, revenue_offset] = convertValue(revenueDict, float(row[10]))
            except:
                X[i, revenue_offset] = convertValue(revenueDict, 0)

            try:
                X[i, metascore_offset] = convertValue(metaScoreDict, float(row[11]))
            except:
                X[i, metascore_offset] = convertValue(metaScoreDict, 0)

    return (X,Y)

 
