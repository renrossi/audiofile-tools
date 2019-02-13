#!/usr/bin/env python
# encoding: utf-8

from lib import track_scanner,\
                track_converter,\
                track_joiner, \
                metadata_handler

import os


if __name__ == '__main__':

    tracks_path = '/media/storage/music/audiofile-tools-testdir/'

    track_list = track_scanner.scan_tracks(tracks_path)

    track_converter.batch_convert_track(tracks_path, './tmp/', track_list, 'wav')

    track_joiner.join_tracks(track_list)

    try:

        track_converter.convert_track('./tmp/', tracks_path, { 'title': 'output', 'format': '.wav' }, 'flac')

    except:

        print('error')

    else:

        os.remove('./tmp/output.wav')

        metadata_handler.read_metadata('flac', tracks_path, 'output.flac')
