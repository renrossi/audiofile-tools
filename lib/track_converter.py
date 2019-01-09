#!/usr/bin/env python
# encoding: utf-8

from subprocess import run, DEVNULL

def convert_track(src_path, dest_path, track, output_format):
    run(['ffmpeg', '-i', src_path + track['title'] + track['format'], dest_path + track['title'] + '.' + output_format], stdout=DEVNULL, stderr=DEVNULL)

def batch_convert_track(src_path, dest_path, track_list, output_format):
    for track in track_list:
        convert_track(src_path, dest_path, track, output_format)
