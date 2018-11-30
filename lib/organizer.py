#!/usr/bin/env python
# encoding: utf-8

from os import scandir, rename

def file_name_formatter(file_path):
    for file in scandir(file_path):
        # if file.name.endswith(('.ape', '.flac', '.m4a')):
        rename(file_path + file.name, file_path + file.name.title().replace(' ', '_').strip())

file_name_formatter('/home/renrossi/documents/books/')