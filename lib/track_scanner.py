#!/usr/bin/env python
# encoding: utf-8

from os import scandir
from metadata_handler import read_metadata

def scan_tracks(path):

    track_list = []

    for file in scandir(path):

        if file.name.endswith(('.ape', '.flac', '.m4a')):

            # tracks += track.name.replace(' ', '\ ') + ' '

            audio_file = file.name.split('.')

            metadata = read_metadata(path, audio_file[0], audio_file[1])

            track = {
                'track_file': {
                    'name': audio_file[0],
                    'format': '.' + audio_file[1]
                },
                'track_metadata': {
                    'title': metadata['title'][0],
                    'album': metadata['album'][0],
                    'artist': metadata['artist'][0]
                }
            }

            track_list.append(track)

    return track_list


print(scan_tracks('/media/storage/music/audiofile-tools-testdir/'))

