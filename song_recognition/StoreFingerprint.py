import pickle
import numpy as np


    


def addFingerprint(fn, fni, dT, t, songName, dictionary):
    """Welcome to adding fingerprint in dictionary.

    Args:
        (fn,fn+1,dT) : The fingerprint
        t : The time for the fingerprint
        songName : A string lol, im not really laughing tho

        dictionary : The dictionary

    """
    key = (fn,fni,dT)
    if key in dictionary:
        dictionary[key].append((songName, t))
    else:
        dictionary[key] = [(songName, t)]

def addFingerprints(fingerprints, songName):
    """Welcome to adding fingerprint in dictionary.

    Args:
        fingerprints : The fingerprints (size 4)
        
        dictionary : The dictionary

        songName : A string lol, im not really laughing tho
        
    AUTO UPDATES AND OPENS DICTIONARY

    """
    with open("dictionary.pkl", mode="rb") as opened_file:
        my_loaded_dictionary = pickle.load(opened_file)
    for i in fingerprints:
        addFingerprint(*i, songName, my_loaded_dictionary)
    with open("dictionary.pkl", mode="wb") as opened_file:
        pickle.dump(my_loaded_dictionary, opened_file)