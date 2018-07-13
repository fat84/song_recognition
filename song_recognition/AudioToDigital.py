def mp3_to_digital(local_song_path, song_name):
    """
    Parameters: song path, song name
                song path: the local path of the song (str)
                song name: the name of the song (str)
    --------
    Returns: name of song, numpy array of song, and time samples (tuple)
    """    
    import numpy as np
    import urllib
    import librosa
    import numpy as np
    from IPython.display import Audio
    
    samples, fs = librosa.load(local_song_path, sr=44100, mono=True)
    times = np.arange(len(samples)) * 44100
    if np.max(np.abs(samples)) == 1:
        samples = samples*(2**15)
    
    return (song_name, samples, times)

def mic_to_digital(listen_time=30):
    """Records for specified amount of time (in secs) and returns digitized audio and time samples as numpy arrays"""
    
    import numpy as np
    from IPython.display import Audio
    import microphone
    from microphone import record_audio
    
    frames, sample_rate = record_audio(listen_time)
    samples = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    times = np.arange(len(samples)) * sample_rate
    return (samples, times)