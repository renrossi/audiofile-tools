#!/usr/bin/env python
# encoding: utf-8

def set_reader(format):
    if format == 'flac':
        from mutagen.flac import FLAC
        codec = FLAC
    elif format == 'ape':
        from mutagen.monkeysaudio import MonkeysAudio as APE
        codec = APE
    elif format == 'm4a':
        from mutagen.easymp4 import EasyMP4 as ALAC
        codec = ALAC

    return codec

def read_metadata(path, file_name, format):
    codec = set_reader(format)

    return codec(path + file_name + '.' + format)

#     print(metadata['title'])
#
# print(read_metadata('/media/data/music/audiofile-tools-testdir/', 'test2', 'ape'))

