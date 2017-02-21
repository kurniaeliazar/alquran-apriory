import sys
import re

def main():
	dataset_list = open('dataset-list.txt', 'r')
	regex = re.compile(r'[\n\r\t]')

	for line in dataset_list:
		title = regex.sub('', line)
		dataset = open(title+'.txt','r')
		num = 0

		for line_dataset in dataset:
			# print line_dataset
			essay = open(sys.argv[1], 'r')
			for line_essay in essay:
				#print("essay", line_essay)
				lineA = regex.sub('', line_dataset)
				lineB = regex.sub('', line_essay)
				if (lineA == lineB):
					num+=1

		print("%s : %d" % (title, num))

if __name__ == '__main__':
    main()	