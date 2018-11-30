#!/usr/bin/env python
# encoding: utf-8

from shutil import copy

def cue_file_generator(tracks_path, file_name, track_list):
    copy('./docs/template_headers.cue', './tmp/' + file_name)
    # cue_file = open(tracks_path + file_name + '.cue', 'x')