from ..backpropagation.backpropagation import *
from ..backpropagation.buildInput import *
from ..twitter.generateTrainingData import *
from ..twitter.getWordList import *
from ..twitter.getAnnotation import *
import numpy as np
import math

M = 0.8
eta = 0.9
errorThresh = 10

wordList1 = getWordList("data/twitter/twitter_positive",
	"data/twitter/twitter_negative",
	"data/twitter/twitter_objective", 3)
[X, Y] = generateTrainingData("data/twitter/dataset1/train/twitter_positive",
	"data/twitter/twitter_objective",
	"data/twitter/dataset1/train/twitter_negative",
	wordList1, 3)
layer1 = np.array([X[0].shape[0], 2])

w1 = initializeW(layer1, 1)
print "Estimating weights..."
backpropagation(layer1, X, Y, w1, eta, M, errorThresh)

wordList2 = getWordList("data/twitter/twitter_positive",
	"data/twitter/twitter_objective",
	"", 2)
[X, Y] = generateTrainingData("data/twitter/dataset1/train/twitter_positive",
	"data/twitter/dataset1/train/twitter_negative",
	"",
	wordList2, 2)
layer2 = np.array([X[0].shape[0], 2])

w2 = initializeW(layer2, 1)
backpropagation(layer2, X, Y, w2, eta, M, errorThresh)

total = 0
correct = 0

for i in range(1, 7):
	correct_curr = 0
	total_curr = 0
	file_name = "data/twitter/twitter_data/group" + str(i)
	f = open(file_name, 'r')
	data = f.read()
	f.close()

	for line in data.split('\n'):
		total = total + 1
		total_curr = total_curr + 1

		temp = []
		temp.append(-1)
		[line, annotation] = getAnnotation(line)

		words = getWords(line)
		for w in wordList1:
			if w in words:
				temp.append(1)
			else:
				temp.append(0)
		X1 = np.array(temp)

		temp = []
		temp.append(-1)
		words = getWords(line)
		for w in wordList2:
			if w in words:
				temp.append(1)
			else:
				temp.append(0)
		X2 = np.array(temp)

		outputs = feedForward(w1, X1, layer1)

		
		if(outputs[outputs.shape[0] - 1][0] > 0.5):
			outputs = feedForward(w2, X2, layer2)
			if(outputs[outputs.shape[0] - 1][0] < 0.5):
				correct = correct + 1
				correct_curr = correct_curr + 1
	print "group ", i, " ", correct_curr, " ", total_curr, correct_curr/(total_curr * 1.0)
'''
#negative
f = open("data/twitter/dataset1/test/twitter_negative", 'r')
data = f.read()
f.close()

for line in data.split('\n'):
	total = total + 1
	temp = []
	temp.append(-1)
	words = getWords(line)
	for w in wordList1:
		if w in words:
			temp.append(1)
		else:
			temp.append(0)
	X = np.array(temp)
	outputs = feedForward(w1, X, layer1)
	if(outputs[outputs.shape[0] - 1][0] < 0.5):
		correct = correct + 1

#positive
f = open("data/twitter/dataset1/test/twitter_positive", 'r')
data = f.read()
f.close()

for line in data.split('\n'):
	total = total + 1

	temp = []
	temp.append(-1)
	words = getWords(line)
	for w in wordList1:
		if w in words:
			temp.append(1)
		else:
			temp.append(0)
	X1 = np.array(temp)

	temp = []
	temp.append(-1)
	words = getWords(line)
	for w in wordList2:
		if w in words:
			temp.append(1)
		else:
			temp.append(0)
	X2 = np.array(temp)

	outputs = feedForward(w1, X1, layer1)
	if(outputs[outputs.shape[0] - 1][0] > 0.5):
		outputs = feedForward(w2, X2, layer2)
		if(outputs[outputs.shape[0] - 1][0] > 0.5):
			correct = correct + 1

#objective
f = open("data/twitter/dataset1/test/twitter_objective", 'r')
data = f.read()
f.close()

for line in data.split('\n'):
	total = total + 1

	temp = []
	temp.append(-1)
	words = getWords(line)
	for w in wordList1:
		if w in words:
			temp.append(1)
		else:
			temp.append(0)
	X1 = np.array(temp)

	temp = []
	temp.append(-1)
	words = getWords(line)
	for w in wordList2:
		if w in words:
			temp.append(1)
		else:
			temp.append(0)
	X2 = np.array(temp)

	outputs = feedForward(w1, X1, layer1)
	if(outputs[outputs.shape[0] - 1][0] > 0.5):
		outputs = feedForward(w2, X2, layer2)
		if(outputs[outputs.shape[0] - 1][0] < 0.5):
			correct = correct + 1
'''
print correct, " ", total, correct/(total * 1.0)
