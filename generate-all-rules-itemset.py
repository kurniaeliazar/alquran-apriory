import sys
import obo
import string
import re
import os

# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from string import digits

regex = re.compile(r'[\n\r\t]')
regexnumber = re.compile(r'[0-9]')
factory = StemmerFactory()
stemmer = factory.create_stemmer()


tema_list = open('./tema/tema_list.txt', 'r')
for line in tema_list:
	title = regex.sub('', line)
	dataset = open('./tema/'+title+'.txt','r')
	stemmout = open('stemm-result/'+title+'-steem.txt','w')
	indexout = open('index-result/'+title+'-index.csv','w')
	datasetnumber = open('dataset-result/'+title+'-dataset.csv','w') 

	print("Proses file %s start ..." % title)
	
	for line in dataset:
		stopwords = open('stopwords.txt','r')
		line = stemmer.stem(line)
		for word in stopwords:
			stopword = regex.sub('', word)
			linewords = line.split()
			resultwords  = [word1 for word1 in linewords if word1 not in stopword]
			result = ' '.join(resultwords)
			#line = line.lower().replace(stopword, "")
			line = regexnumber.sub('',result)
		stopwords.close()
		stemmout.write(result+'\n')
	
	stemmout.close()
	dataset.close()	

	dataset = open('stemm-result/'+title+'-steem.txt','r')	

	fullwordlist = obo.stripNonAlphaNum(dataset.read().lower())
	wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
	dictionary = obo.wordListToFreqDict(wordlist)
	sorteddict = obo.sortFreqDict(dictionary)

	dataset.close()
	dataset = open('stemm-result/'+title+'-steem.txt','r')	

	lines = []
	regex = re.compile(r'[\n\r\t]')

	for sentence in dataset:
		line = regex.sub('', sentence)
		lines.append(str(line))

	i = 0
	for s in sorteddict:
		chars_to_remove = [' ', '(', ')','\'',',']
		rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
		indexword = re.sub(rx, '', str(s))
		res = indexword.translate(None, digits)
		
		k=0
		for line in lines:
			line2 = str.replace(line, '-', ' ')
			line2 = str.replace(line2, str(res), str(i))
			lines[k] = line2.replace(' ', ',')	
			k+=1

		indexout.write(str(i)+','+res+','+str(i)+'\n')
		i+=1

	all=string.maketrans('','')
	nodigs=all.translate(all, string.digits)
	nodigs = re.sub(',','', nodigs)

	for line in lines:
		res = str(line)
		res = res.translate(all, nodigs)
		if ( res <> "" ):
			datasetnumber.write(res+'\n')

	print("Proses file %s sukses" % title)
	
	dataset.close()	
	indexout.close()

	os.system("python apriori.py index-result/%s-index.csv dataset-result/%s-dataset.csv 0.02 0.3 %s" % (title, title, title))
