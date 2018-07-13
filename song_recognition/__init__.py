import pathlib
from pathlib import Path
from song_recognition import AudioToDigital
from song_recognition import PeakToFingerprint
from song_recognition import songStoreFingerprint
from song_recognition import MatchFingerprint
from song_recognition import DigitalToFingerprint

def store(localSongPath, songName):
    localSongPath = Path(localSongPath)

    songName, samples, times = AudioToDigital.mp3_to_digital(localSongPath, songName)

    spectrogram, freqs,times = DigitalToFingerprint.audio_to_spectrogram(samples)

    localPeaks = DigitalToFingerprint.spectrogram_to_peaks(spectrogram, freqs, times)

    fingerprints = PeakToFingerprint.peaksToFingerprints(localPeaks, songName=songName)

    StoreFingerprint.addFingerprints(fingerprints, songName)
    print("Finished storing song")

def match(time):

    samples,times = AudioToDigital.mic_to_digital(listen_time=time)

    spectrogram, freqs,times = DigitalToFingerprint.audio_to_spectrogram(samples)

    localPeaks = DigitalToFingerprint.spectrogram_to_peaks(spectrogram, freqs, times)

    fingerprints = PeakToFingerprint.peaksToFingerprints(localPeaks)

    counter = MatchFingerprint.fingerprintToCounter(fingerprints)

    songName, occurences = counter.most_common(1)

    print(songName)


