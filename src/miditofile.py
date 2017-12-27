#!/usr/bin/env python
import sys
import random
from mido import MidiFile

def writeFile(msg, flnm):
	with open(flnm,"w") as file:
		file.write(msg)

if __name__ == '__main__':	
	informat = ""
	mid = MidiFile(sys.argv[1])
	print(mid.length)
	for i, track in enumerate(mid.tracks):
		print('Track {}: {}'.format(i, track.name))
		for msg in track:
			if not msg.is_meta and msg.type == "note_on":
				informat += (str(msg.note) + " " + str(msg.time)) + '\n'

	writeFile(informat,"informat.txt")
