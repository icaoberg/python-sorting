from random import shuffle
from time import time
from copy import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from os import mkdir
from os.path import exists
from os import system

def piksrt(array, debug=False):
	'''
	Straight insertion. Based on Numerical Recipes in C.

	:param unsorted_list: a list of unsorted integers
    :type unsorted_list: list
    :rtype: list of sorted integers
    '''

	if _isvalid(array):
		if debug:
			steps = []
			times = []
		else:
			t = time()
		
		for j in enumerate( array, start=0 ):
			if debug:
			    t = time()
			
			a = array[j[0]]
			i=j[0]-1
			while i > -1 and array[i] > a:
			    array[i+1]=array[i]
			    i-=1
			array[i+1]=a

			if debug:
			    steps.append( copy(array) )
			    times.append( time()-t )
		    
		if debug:
			return [steps,times]
		else:
			t = time() - t
			return [array, t ]
	else:
		print "Invalid input argument"
		return []

def bubble(unsorted_list):
	'''
	Bubble sort

    :param unsorted_list: a list of unsorted integers
    :type unsorted_list: list
    :rtype: list of sorted integers
	'''
	# adapted from snippet found in 
	# http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php

	steps = []

	for passnum in range(len(unsorted_list)-1,0,-1):
		for i in range(passnum):
		    if unsorted_list[i]>unsorted_list[i+1]:
		        temp = unsorted_list[i]
		        unsorted_list[i] = unsorted_list[i+1]
		        unsorted_list[i+1] = temp
		        steps.append( copy(unsorted_list) )

	return steps

def merge(unsorted_list):
	'''
	Merge sort

    :param unsorted_list: a list of unsorted integers
    :type unsorted_list: list
    :rtype: list of sorted integers
	'''
	return None

def _isvalid(unsorted_list):
	'''
	Helper method that determines if list is valid

	:param unsorted_list: a list of integers
    :type unsorted_list: list
    :rtype: boolean
	'''

	if isinstance(unsorted_list, list) and all(isinstance(x,int) for x in unsorted_list):
		return True
	else:
		return False

def make_randomly_shuffled_list( length_of_shuffled_list ):
	'''
	Helper method that makes a list of shuffled integers

	:param length_of_shuffled_list: the length of the list
    :type length_of_shuffled_list: int
    :rtype: list
	'''

	list_of_integers = range( length_of_shuffled_list )

	for i in range(10):
		shuffle(list_of_integers)

	return list_of_integers

def animate_debug_results( results, output_directory='./' ):
	'''
	Helper function that animates the debug results.

	TODO: try to make matplotlib.animate work on macosx
	'''

	if not exists(output_directory):
		mkdir(output_directory)

	i = 1
	elapsed_time = 0
	for result in results:
		elapsed_time += t
		plt.plot( range( len(result), result, 'ob' )
		plt.xlabel("Step " + str(i))
		filename = output_directory + 'image' + str('%05d' % i) + '.png'
		print "Saving " + filename
		plt.savefig(filename)
		i=i+1
		plt.clf()
	plt.close()

	print "Attempting to make movie with ffmpeg"
	#system("ffmpeg -f image2 -r 1 -i " + output_directory + "image%05d.png -vcodec mpeg4 -y " + output_directory + "movie.mp4")
