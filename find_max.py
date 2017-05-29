# coding: utf-8
# author: Eri Jonhson

def find_max(int_list):
	if int_list == []:
		return None
	max_number = int_list[0]
	for i in int_list:
		if max_number < i: 
			max_number = i
	return max_number

def find_min(int_list):
	if int_list == []:
		return None
	min_number = int_list[0]
	for i in int_list:
		if min_number > i: 
			min_number = i
	return min_number

assert None == find_min([])
assert 1 == find_min([1,2,3])
assert 4 == find_min([4,6,7])
assert -3 == find_min([-1,-2,-3])


assert None == find_max([])
assert 3 == find_max([1,2,3])
assert 7 == find_max([4,6,7])
assert -1 == find_max([-1,-2,-3])
