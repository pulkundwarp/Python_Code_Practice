# Pranav Pulkundwar 

# ------------------- Problem ------------------- #

def rle_encode(x):
    if not x:
        return [], []
    
    item = []    #declaring empty lists
    count = []

    cur_count = 1    #declaring initial count and character
    cur_item = x[0]

    for i in range(1, len(x)):    #If a char is equal to the previous character then it will add 1 in the counter
        if x[i] == cur_item:
            cur_count = cur_count + 1
        else:    #if the char is not equal to previous char then adding it to the list
            item.append(cur_item)
            count.append(cur_count)
            cur_item = x[i]
            cur_count = 1
    item.append(cur_item)
    count.append(cur_count)
    return (item, count)    #printing the tuple of lists



# ------------------- Problem ------------------- #

def rle_decode(items, count):
    res = []
    for i,j in zip(items, count):
        cur_list = []
        cur_list.append(i)
        cur_list = cur_list*j
        res.extend(cur_list)
    return res



# ------------------- Problem ------------------- #

class Rle:
    def __init__(self, values, lengths = None):
        if lengths is None:    #Checking if length is provided in the input, otheriwse encoding it using 'encode_rle' function
            self.values, self.lengths = self.encode_rle(values)
        else:
            self.values = values
            self.lengths = lengths

    @staticmethod
    def encode_rle(x):
        if not x:
            return [], []

        values = []    #declaring empty lists
        lengths = []

        cur_item = 1    #declaring initial count and character
        cur_count = x[0]

        for i in range(1, len(x)):    #If a char is equal to the previous character then it will add 1 in the counter
            if x[i] == cur_count:
                cur_item += 1
            else:    #if the char is not equal to previous char then adding it to the list
                values.append(cur_count)
                lengths.append(cur_item)
                cur_count = x[i]
                cur_item = 1
        values.append(cur_count)
        lengths.append(cur_item)
        return (values, lengths)    #printing the tuple of lists
    
    def __getitem__(self, i):
        res = rle_decode(self.values,self.lengths)
        return res[i]

    def append(self, values):
        if len(self.values) == 0 or self.values[-1] != values:
            self.values.append(values)
            self.lengths.append(1)
        else:
            self.lengths[-1] += 1

# ------------------- Problem ------------------- #

import math

def median(x):
    xS = sorted(x)    #Sorting the given list x
    n = len(xS)    #Calculating the length of x    
    if n % 2 == 1:    #if odd numbered list then returns middle element
        return xS[n // 2]
    else:
        val1 = xS[n // 2 - 1]
        val2 = xS[n // 2]
        return (val1 + val2) / 2    #If even numbered list, returns the average of the two middle elements

# Second solution to the same problem

def median2(x):
    if len(x) < 1:
        return None

    xS = sorted(x)    #Sorting the given list x
    n = len(xS)    #Calculating the length of x 
    i1 = math.floor((n - 1) / 2)
    i2 = math.ceil((n - 1) / 2)
    
    if n % 2 == 0:
        return (xS[i1] + xS[i2]) / 2    #If even numbered list, returns the average of the two middle elements
    else:
        return xS[i1]     #if odd numbered list then returns middle element



# ------------------- Problem ------------------- #

#Using above median function as a helper function to calculate median of the list

def iqr(x):
    xsort = sorted(x)    #Sorting the given list x  
    if len(xsort) <= 1:    #checking the size of the list
        return 0.0
    if len(xsort) % 2 == 0:
        lhalf = xsort[:len(xsort) // 2]    #spliting even numbered list in two parts
        uhalf = xsort[len(xsort) // 2:]
    else:
        lhalf = xsort[:len(xsort) // 2 + 1]
        uhalf = xsort[len(xsort) // 2:]
    q1 = median(lhalf)    #Calculating q1 using median function
    q3 = median(uhalf)    #Calculating q2 using median function
    return float(q3 - q1)



# ------------------- Problem ------------------- #

#Using above median function as a helper function to calculate median of the list

def quartiles(x):    #creating similar function as above to get the q1 and q2
    asort = sorted(x)
    if len(x) % 2 == 0:
        lhalf = asort[:len(x) // 2]
        uhalf = asort[len(x) // 2:]
    else:
        lhalf = asort[:len(x) // 2 + 1]
        uhalf = asort[len(x) // 2:]
    Q1 = median(lhalf)
    Q3 = median(uhalf)
    return {'q1': Q1, 'q3': Q3}

def fivenum(a):   #combining and printing all the data in one list
    x = list(a)
    x.sort()  
    xmin = min(x)
    quartile_result = quartiles(x)
    q1 = quartile_result['q1']
    median_x = median(x)
    q3 = quartile_result['q3']
    xmax = max(x)
    return [xmin, q1, median_x, q3, xmax]



# ------------------- Problem ------------------- #

def order(x):
    x_ind = list(enumerate(x))    #pairing indices with the elements
    ele_sort = sorted(x_ind, key=lambda pair: pair[1])    #Sorting by element in ascending order
    ind_sort = [pair[0] for pair in ele_sort]    #getting the original indices
    return ind_sort



# ------------------- Problem ------------------- #

def rank(x):
    y = list(x)
    output = [0] * len(y)
    for i, j in enumerate(sorted(range(len(y)), key=lambda z: y[z])):
        output[j] = i + 1
    return output



# ------------------- Problem ------------------- #

def cummax(x):
	max_num_list = []   # Creating empty List
	max_num = x[0]
	max_num_list.append(x[0])   # Adding first element in the list
	for i in range (1,len(x)):   # For loop to find the max of two consecutive numbers and adding them in the list created above
		if x[i] > max_num:
			max_num = x[i]
		max_num_list.append(max_num)
	return max_num_list   # Printing the list



# ------------------- Problem ------------------- #

def cumsum(x):
	sum_list = []   # Creating empty list
	sum_num = x[0]
	sum_list.append(x[0])   # Adding first element in the list
	for i in range(1, len(x)):   # For loop to get the addition of consecutive numbers and adding them into the list created above
		sum_num = x[i] + sum_num
		sum_list.append(sum_num)
	return sum_list   # Printing the final list



# ------------------- Problem ------------------- #

import re   # Importing the regex library to use lower command
def lower_case(x):
	return x.lower()
	
def tokenize(x):
	lowered_list = lower_case(x)   # Converting the string into lowercase
	list_1 = re.sub(r'[\W+]', ' ', lowered_list)   # Replacing all non-alphanumeric characters with blanks
	sep_list = list_1.split()   # Spliting all words into separate strings
	return sep_list   # Pritning the final list



# ------------------- Problem ------------------- #

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



# ------------------- Problem ------------------- #

def ifelse(test,yes,no):
	res_list = []   # Creating empty list to add values
	for i in range(len(test)):   # checking the length of whole testcase to compare boolian values
		if test[i]:
			res_list.append(yes[i])
		else:
			res_list.append(no[i])
	return res_list   # Printing the resulting list

