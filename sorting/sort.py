from random import shuffle

def bubble(unsorted_list):
	'''
	Bubble sort

    :param unsorted_list: a list of unsorted integers
    :type unsorted_list: list
    :rtype: list of sorted integers
	'''

	return None

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

def _shuffle_list( length_of_shuffled_list ):
	'''
	Helper method that makes a list of shuffled integers

	:param length_of_shuffled_list: the length of the list
    :type length_of_shuffled_list: int
    :rtype: list
	'''

	list_of_integers = range( length_of_shuffled_list )
	shuffle(list_of_integers)

	return list_of_integers
