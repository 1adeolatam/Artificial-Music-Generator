#!/usr/bin/env python
import sys
import random

def makeChain(src, chain = {}):
	words = src.split('\n')
	index = 1# start from second entry and use first entry as key
	for word in words[index:]:
		key = words[index - 1]#the previous word
		if key in chain:
			chain[key].append(word)
		else:
			chain[key] = [word]
		index += 1
	return  chain

def readFile(flnm):
	with open(flnm,"r") as file:
		src = file.read()
	return src

def generateMsg(chain, wordcount = 20):
	word1 = random.choice(list(chain.keys()))
	msg = word1
	
	while len(msg.split('\n')) < wordcount :
		word2 = random.choice(chain[word1])
		word1 = word2
		msg += '\n' + word2

	return msg
		

if __name__ == '__main__':
	readFile("infromat.txt")
