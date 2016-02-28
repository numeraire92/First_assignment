# -*- coding: cp1252 -*-
import sys
import json

'''
	JSON: http://stackoverflow.com/questions/11026959/python-writing-dict-to-txt-file-and-reading-dict-from-txt-file
'''


input_file_name = ""
dictionary_file_name = ""
output_file_name = ""

def replace(orig_l, the_Key, the_Value):
	'''
		orig_l:	The original line in which the replacement should happen.
		the_Key:	They key from the dictionary. The text in the original_line
					to be replaced.
		the_Value:	The value the should be replaced with.
	'''
	out_l = ""
	if (orig_l.find(the_Key)-1 > 0):
		out_l = orig_l[0:orig_l.find(the_Key)-1] + the_Value + \
			orig_l[orig_l.find(the_Key)-1+len(the_Key):]
	else:
		out_l = orig_l[0:0] + the_Value + \
			orig_l[0+len(the_Key):]
	return out_l


def main():
	'''
		argv[1]:	The input html file that contains the additional MD codes to be
					replaced.
		argv[2]:	The txt file that holds the dictionary.
	'''

	if (len(sys.argv) == 3):
		input_file_name = str(sys.argv[1])
		dictionary_file_name = str(sys.argv[2])
		output_file_name = input_file_name[0:input_file_name.rindex('.')-1] + \
			"-parsed" + input_file_name[input_file_name.rindex('.'):]
	else:
		print "Problem with the number of arguments."

	if ((input_file_name!="") & (dictionary_file_name!="")):
		dictionary = json.load(open(dictionary_file_name))
		with open(output_file_name,'w') as output_f:
			with open(input_file_name,'r') as input_f:
				for line in input_f:
					output_line = line
					# This assumes that codes occurs one per line.
					for key in dictionary:
						if (line.find(key.encode('utf-8'))!=-1):
							output_line = replace(line, key.encode('utf-8'),
								dictionary[key].encode('utf-8'))
					# end of parsing the dictionary .find(key.encode('utf-8'))
					output_f.write(output_line)
				# end of parsing input_F
			# closing input_f
		# closing output_f



if __name__ == '__main__':
	main()
