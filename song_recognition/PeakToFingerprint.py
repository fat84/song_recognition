import numpy as np
from mygrad import sliding_window_view

def peaksToFingerprints(local_peaks, fn=15, songName = "None"):
    """Welcome to peaksToFingerprints.

    Args:
        local_peaks : The list of local peaks (a boolean array)
        fn : 
    Returns:
        fingerprints : a np array with all fingerprints (size 4)
    """
    
    
    times, freqs = np.where(local_peaks.T)
    fp = []
    for t in times[:-fn-2]:
        for i in range (t + 1, t + fn+1):
            fp.append((freqs[t], freqs[i], times[i]-times[t], times[t]))
    print(times)
    print(freqs)
#f = sliding_window_view(freqs, window_shape=(len(freqs)-fn,), step = 1)
#t = sliding_window_view(freqs, window_shape=(len(times)-fn,), step = 1)
#    fp.extend(list(zip(np.tile(freqs[:-fn], fn),
#                      f[1:].flatten(),
#                      t[1::].flatten()-np.tile(times[np.newaxis, :-fn], fn),
#                      np.tile(times[:-fn], fn))))
    print(fp[0:100])
    return fp
