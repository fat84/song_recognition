import pickle
import numpy as np
import collections

    
with open("dictionary.pkl", mode="rb") as opened_file:
    my_loaded_dictionary = pickle.load(opened_file)


def incrementCounter(fn, fni, dT, t, dictionary, counter):
    """Welcome to match fingerprint in dictionary.

    Args:
        (fn,fn+1,dT) : The fingerprint
        songName : A string lol, im not really laughing tho
        t : The time for the fingerprint
        dictionary : The dictionary
    Returns:
        counter : A count of all the keys (size 3)
    """
    key = (fn,fni,dT)
    if key in dictionary:
        for name, time in dictionary[key]:
            counter[(name,time-t)] += 1
def fingerprintToCounter(fingerprints):
    """Welcome to fingerprintToCounter.

    Args:
        fingerprints : the fingerprints (size 4)
        dictionary : the dictionary, opened only once
    Returns:
        counter : a counter object with (name, offset) -> count
    """
    with open("dictionary.pkl", mode="rb") as opened_file:
        my_loaded_dictionary = pickle.load(opened_file)
    counter =  collections.Counter()
    for element in fingerprints:
        incrementCounter(*element, my_loaded_dictionary, counter)
    return counter