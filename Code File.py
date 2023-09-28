
# ------------------- Problem 1 ------------------- #

def cummax(x):
	max_num_list = []   # Creating empty List
	max_num = x[0]
	max_num_list.append(x[0])   # Adding first element in the list
	for i in range (1,len(x)):   # For loop to find the max of two consecutive numbers and adding them in the list created above
		if x[i] > max_num:
			max_num = x[i]
		max_num_list.append(max_num)
	return max_num_list   # Printing the list



# ------------------- Problem 2 ------------------- #

def cumsum(x):
	sum_list = []   # Creating empty list
	sum_num = x[0]
	sum_list.append(x[0])   # Adding first element in the list
	for i in range(1, len(x)):   # For loop to get the addition of consecutive numbers and adding them into the list created above
		sum_num = x[i] + sum_num
		sum_list.append(sum_num)
	return sum_list   # Printing the final list



# ------------------- Problem 3 ------------------- #

import re   # Importing the regex library to use lower command
def lower_case(x):
	return x.lower()
	
def tokenize(x):
	lowered_list = lower_case(x)   # Converting the string into lowercase
	list_1 = re.sub(r'[\W+]', ' ', lowered_list)   # Replacing all non-alphanumeric characters with blanks
	sep_list = list_1.split()   # Spliting all words into separate strings
	return sep_list   # Pritning the final list



# ------------------- Problem 4 ------------------- #

# Using function 'lower_case' from above 

# Creating new function to create dictionary
def wordfreq_dic(li):   # Creating dictionary to use in the main function to count the number of words
    wordfreq_dic = {}
    for i in li:
        wordfreq_dic[i] = wordfreq_dic.get(i, 0) + 1
    return wordfreq_dic

def count_words(x):
	lowered_list = lower_case(x)
	list_1 = re.sub(r'[\W+]', ' ', lowered_list)
	sep_list = list_1.split()
	count_dic = wordfreq_dic(sep_list)
	return count_dic



# ------------------- Problem 5 ------------------- #

def ifelse(test,yes,no):
	res_list = []   # Creating empty list to add values
	for i in range(len(test)):   # checking the length of whole testcase to compare boolian values
		if test[i]:
			res_list.append(yes[i])
		else:
			res_list.append(no[i])
	return res_list   # Printing the resulting list
