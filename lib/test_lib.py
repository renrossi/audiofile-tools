#!/usr/bin/env python

import readline
import glob
import subprocess


# chdir('/media/storage/music/Genesis-1977-Spot_The_Pigeon/test')

# track_converter('wav')

# input_format = input('Enter the format of the original file(s) (e.g. flac, ape, wav, etc.): ')

# for entry in os.scandir(directory, files = ""):
#     if entry.name.endswith(('.ape', '.flac')):
#         files % entry.name

# def file_scanner(path):
#     files = ''
#     for entry in os.scandir(path):
#         if entry.name.endswith(('.ape', '.flac')):
#             files += entry.name.replace(' ', '\ ') + ' '
#
#     return files


# comm = 'sox' + file_scanner(directory) + ' output-sox.flac'
# subprocess.run('ls | egrep "\.mp4$|\.mp3$|\.ape$|\.flac$|\.wv$|\.wav$"', cwd=directory, shell=True)


#
# print('Please choose one the options below:\n')
#
# print('01. Convert')
# print('02. Join\n')

# choice = int(input('> '))

# if choice == 1:

    # output_format = input('Enter the desired format for the destination file(s) (e.g. flac, ape, wav, etc.): ')

    # for entry in os.scandir(directory):
    #     if entry.name.endswith('.%s' % input_format):
    #         print(entry.name)

# do ffmpeg -i "$f" "${f%.<INPUT_FORMAT>}.<OUTPUT_FORMAT>";
# done
#
# sox input1.<OUTPUT_FORMAT> input2.<OUTPUT_FORMAT> input3.<OUTPUT_FORMAT> output-sox.<OUTPUT_FORMAT>


# replacements = {'CREATE TABLE ':'CREATE TABLE data_profiling.applicants.'}
# lines = []
# with open('/home/renrossi/applicants.sql') as infile:
#     for line in infile:
#         for src, target in replacements.items():
#             line = line.replace(src, target)
#         lines.append(line)
# with open('/home/renrossi/applicants.sql', 'w') as outfile:
#     for line in lines:
#         outfile.write(line)



# from scan import track_scanner
# from convert import single_track_converter, multi_track_converter
# from join import track_joiner
# from metadata_handler import read_metadata
# from os import remove

# tracks_path = '/media/storage/music/audiofile-tools-testdir/'

# track_list = track_scanner(tracks_path)
#
# multi_track_converter(tracks_path, './tmp/', track_list, 'wav')
#
# track_joiner(track_list)
#
# try:
#     single_track_converter('./tmp/', tracks_path, {'title': 'output', 'format': '.wav'}, 'flac')
# except:
#     print('error')
# else:
#     remove('./tmp/output.wav')

# read_metadata('flac', tracks_path, 'output.flac')
