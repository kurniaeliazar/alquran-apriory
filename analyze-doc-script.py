import sys
import re

def main():

	dataset_list = open('./tema/tema_list.txt', 'r')
	regex = re.compile(r'[\n\r\t]')

	print("itemset-result")
	print("=====================================================")

	for line in dataset_list:
		title = regex.sub('', line)

		try:
		    fp = dataset = open('itemset-result/'+title+'-itemset.txt','r')	
		except IOError, e:
		    print ("file %s-itemset tidak ditemukan" %(title))
		    continue
		
		num = 0

		for line_dataset in dataset:
			# print line_dataset
			essay = open('itemset-result/'+sys.argv[1]+'-itemset.txt', 'r')
			for line_essay in essay:
				#print("essay", line_essay)
				lineA = regex.sub('', line_dataset)
				lineB = regex.sub('', line_essay)
				if (lineA == lineB):
					num+=1

		print("%s : %d" % (title, num))

	dataset_list.close()
	dataset_list = open('./tema/tema_list.txt', 'r')	

	print("\n\nrules-result")
	print("=====================================================")

	for line in dataset_list:
		title = regex.sub('', line)

		try:
		    fp = dataset = open('rules-result/'+title+'-rules.txt','r')	
		except IOError, e:
		    print ("file %s-rules tidak ditemukan" %(title))
		    continue
		
		num = 0

		for line_dataset in dataset:
			# print line_dataset
			essay = open('rules-result/'+sys.argv[1]+'-rules.txt', 'r')
			for line_essay in essay:
				#print("essay", line_essay)
				lineA = regex.sub('', line_dataset)
				lineB = regex.sub('', line_essay)
				if (lineA == lineB):
					num+=1

		print("%s : %d" % (title, num))

if __name__ == '__main__':
    main()	