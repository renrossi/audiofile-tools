#!/usr/bin/env python
# encoding: utf-8

import os

from . import metadata_handler


def scan_tracks(path):

    track_list = []

    for file in os.scandir(path):

        if file.name.endswith(('.ape', '.flac', '.m4a')):

            audio_file = file.name.split('.')

            metadata = metadata_handler.read_metadata(path, audio_file[0], audio_file[1])

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
