#!/usr/bin/env python
# encoding: utf-8

def set_format(format):

    if format == 'flac':

        from mutagen.flac import FLAC as codec

    elif format == 'ape':

        from mutagen.monkeysaudio import MonkeysAudio as codec

    elif format == 'm4a':

        from mutagen.easymp4 import EasyMP4 as codec

    return codec


def read_metadata(path, file_name, format):

    codec = set_format(format)

    return codec(path + file_name + '.' + format)
