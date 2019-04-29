'''
PCMtoPDM software written by the brilliant Stephan "Vegas Diamond" Tul.
If used, why not shoot him a few €€€?

HOW TO USE:
To run the code you need to have python 3.x (I used 3.3) installed. The program takes 2 arguments,
-i or --input, which is the path to the input file (a MONO .wav with arbitrary sample rate and bit
depth (not 32bit float)) and the output file -o or --output. Ex: python PCMtoPDM.py -i sample.wav -o output.txt.
'''

import wave
import argparse
import matplotlib.pyplot as plt

#Command line input functions.
parser = argparse.ArgumentParser(description="Process a PCM .wav file and turn it into a PDM file")
parser.add_argument('-i','--input', help='Inputfile of .wav format', required=True)
parser.add_argument('-o','--output', help='Outputfile in plain text, WARNING: will not check if file exists already', required=False)
args = vars(parser.parse_args())

#Creation of wavereader object using commandline.
try:
    sound = wave.open(args['input'], 'r')
except:
    print("Error interpreting WAV file, wrong input (is your wav file mono?)")
    exit()

#Getting and printing number of frames in file.
nframes = sound.getnframes()
print("Number of samples in Wav File: " + str(nframes))

#Getting and printing sample rate.
print("Sample rate: " + str(sound.getframerate()))

'''Converting the sampling width, which is returned in bytes,
to an integer representation and then dividing it by 2.
This division is to account for the way WAV is defined in the python wavereader.
WAV files in wavereader have an amplitude from 0.5*bitdepth to 0.5*bitdepth-1.
A 16-bit WAV file would have 32768 as an amplitude of -1 and 32677 as +1.
0 corresponds with an amplitude of 0.'''
halfbitdepth = 2**(8*sound.getsampwidth())/2

#defining values to be used in loop.
output = []
value = 0
error = 0.0

for x in range(nframes):

    #Read 1 frame, convert it to an integer representation.
    frame = int.from_bytes(sound.readframes(1),byteorder='little')

    #This if converts the integer representation to an amplitude value between -1 and 1.
    if frame < halfbitdepth:
        framevalue = frame/halfbitdepth
    else:
        framevalue = -1.0 + (frame - halfbitdepth) /halfbitdepth

    #Determining whether the pulse in PDM is 1 or 0 for the given frame.
    if framevalue >= error:
        value = 1
        output.append(value)
    else:
        value = -1
        output.append(value+1)


    #Error is changed based on the current frame.
    error = value - framevalue + error

#Writing the file.
with open(args['output'], 'w') as f:
    for x in output:
        f.write(str(x))
f.closed
print("succesfully written to " + args['output'])