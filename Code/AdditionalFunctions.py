
# --- Import dependencies ---
import numpy as np 
import pandas as pd 
import os 

# --- Specify paths ---
pathData = '../Data/MortalityCollections/'
# pathData = 'C:/Users/rakrpe/OneDrive - Roskilde Universitet/Pandemix/AncestryKode/Data/Collections/AmtCollections2023_burial/'
dfRel = pd.read_csv('../SupplementaryTable_RelationalTable_ParishCounty.csv')
# SupplementaryTable_RelationalTable_ParishCounty.csv
# ------
# --- Helper functions for receiving relevant dataframes ---
# ------
def getAmtName(amtID):
    # Gets the name of a given county from the ID
    return dfRel[dfRel.AmtID == amtID].AmtName.values[0]

def getAmtCollections(amtID):
    # Function for getting all data-collections for a specific county, as well as the periods for which the county exists.

    # Get the name of all files in "collections" directory
    allCollections = np.array(os.listdir(pathData))

    # Get the ones relevant to the current amt
    curCollectionsFilenames = allCollections[[int(x.split('_')[0]) == amtID for x in allCollections]]

    # Extract start and end dates
    allStarts = [x.split('_')[2] for x in curCollectionsFilenames]
    allEnds = [x.split('_')[3].split('.')[0] for x in curCollectionsFilenames]

    # Make a list of all dataframes
    alldfs = []
    for filename in curCollectionsFilenames:
        # Read the next file
        curdf = pd.read_csv(pathData + filename)
        # Append to list
        alldfs.append(curdf)
    
    return alldfs,allStarts,allEnds

    