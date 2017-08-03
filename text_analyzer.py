import operator
import re
from collections import Counter
from os import walk


textFiles = []
passage = ""

for (dirpath, dirnames, filenames) in walk('test docs'):							# Getting all the file names from the 'test docs' folder.
    textFiles.extend(filenames)
    break

for files in textFiles:

	with open('test docs/' + files,'r') as f:										# Getting all the text file contents in a string 'passage'.
	    passage = passage + ". " + f.read()

passage = passage.replace("\n"," ")													# Replacing all new lines with a blank space.

words = re.findall(r'\w+', passage)													# List of all words in passage.

low_words = [word.lower() for word in words]										# Converting all the words into lower case.

word_counts = Counter(low_words)													# Counter gives us count(occurrence) of all the words.

word_counts = dict(word_counts)														# Convert into dictionary, with words as keys and their count(occurrence) as values.

sorted_words = sorted(word_counts.items(), key = operator.itemgetter(1), reverse = True)		# Sorting the dictionary by descending order of the values.

sentences = passage.split('. ')														# Splitting our passage into sentences.

low_sentences = [sentence.lower() for sentence in sentences]						# Converting all the sentences into lower case.

for i in range(len(low_sentences)):
	low_sentences[i] = re.findall(r'\w+', low_sentences[i])							# List of words in list of sentences.

file = open('100_most_occurring.txt', 'w')											# Writing new text document for our output.



for i in range(0,100):

	file.write(" \n")
	file.write(" \n")
	file.write(str(i + 1) + "] Word: ")
	file.write("'" + sorted_words[i][0] + "' \n")

	documents = ""
	for files in textFiles:
		if sorted_words[i][0] in open('test docs/' + files).read():
			documents = documents + files + " , "

	file.write("Documents: " + documents + "\n")
	file.write("Occurences: " + str(sorted_words[i][1]) + "\n")
	file.write("Sentences: \n")

	for j in range(len(low_sentences)):
		for k in range(len(low_sentences[j])):
			if(sorted_words[i][0] == low_sentences[j][k]):
				file.write(" \n")
				file.write(sentences[j] + ".\n")
				break

