

#%% imports
from content_recommender import clean_data as cd

EXTRACTED_DATA_PATH = 'IMDB-Movie-Data.csv'
ZIPPED_DATA_PATH = 'content_recommender/data/imdb_data.zip'

#%% Clean Data
cd.unzipData(ZIPPED_DATA_PATH)
cd.loadData(EXTRACTED_DATA_PATH)

#%% Cleanup files
cd.cleanupFile(EXTRACTED_DATA_PATH)