#!/usr/bin/env python
# encoding: utf-8

from scipy.io import wavfile
from numpy import concatenate
from os import remove

def track_joiner(track_list):
    wav_tracks = ()

    for track in track_list:
        sample_rate, audio_data = wavfile.read('./tmp/' + track['title'] + '.wav')

        wav_tracks += (audio_data,)

    album = concatenate(wav_tracks)

    try:
        wavfile.write('./tmp/output.wav', sample_rate, album)
    except:
        print('error')
    else:
        for track in track_list:
            remove('./tmp/' + track['title'] + '.wav')
