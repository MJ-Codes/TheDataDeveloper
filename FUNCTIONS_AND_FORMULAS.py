# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:48:32 2020

@author: crein
"""



'''






import sympy
sympy.init_printing()


QUADRATIC EQUATION

a, b, c, x = sympy.symbols(('a', 'b', 'c', 'x'))
quadratic_equation = sympy.Eq(a*x**2+b*x+c, 0)
sympy.solve(quadratic_equation,x)



BENOMIAL THEOREM

(A+X)n = nC0AnX0 + nC1An-1X1 + nC2An-2X2 +….+ nCnA0Xn



# function to calculate factorial  
# of a number 
def factorial(n): 
  
    f = 1
    for i in range(2, n+1): 
        f *= i  
          
    return f 
  
# Function to print the series 
def series(A, X, n): 
      
    # calculating the value of n! 
    nFact = factorial(n) 
  
    # loop to display the series 
    for i in range(0, n + 1):  
          
        # For calculating the  
        # value of nCr 
        niFact = factorial(n - i) 
        iFact = factorial(i) 
  
        # calculating the value of  
        # A to the power k and X to 
        # the power k 
        aPow = pow(A, n - i) 
        xPow = pow(X, i) 
  
        # display the series 
        print (int((nFact * aPow * xPow) /
                   (niFact * iFact)), end = " ") 





ECDF

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


PEARSON CORRELATION COEFFICIENT


def pearson_r(x,y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y)

    # Return entry [0,1]
    return corr_mat[0,1]




BERNOULLI TRIALS


def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success  so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success




SUCCESSIVE POISSON DISTRIBUTIONS

def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size=size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size=size)

    return t1 + t2






draws a bootstrap replicate

def bootstrap_replicate_1d(data, func):
    """Generate bootstrap replicate of 1D data."""
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)





draws many bootstrap replicates

def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates





PAIRS BOOTSTRAP FOR A SINGLE STATISTIC

def draw_bs_pairs(x, y, func, size=1):
    """Perform pairs bootstrap for a single statistic."""

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_replicates[i] = func(bs_x, bs_y)

    return bs_replicates




PAIRS BOOTSTRAP FOR LINEAR REGRESSION

def draw_bs_pairs_linreg(x, y, size=1):
    """Perform pairs bootstrap for linear regression."""

    # Set up array of indices to sample from: inds
    inds = np.arange(0,len(x))

    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
       
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)

    return bs_slope_reps, bs_intercept_reps




GENERATING A PERMUTATION SAMPLE

def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate((data1, data2))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]

    return perm_sample_1, perm_sample_2




GENERATING PERMUTATION REPLICATES

def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)

        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates

'''



TRANSLATION OF A ONE-SAMPLE BOOTSTRAP HYPOTHESIS TEST

translated_force_a = force_a - np.mean(force_a)  + np.mean(force_b)



TRANSLATION OF A TWO-SAMPLE BOOTSTRAP HYPOTHESIS TEST

# Compute mean of all forces: mean_force
mean_force = np.mean(forces_concat)

# Generate shifted arrays
force_a_shifted = force_a - np.mean(force_a) + mean_force
force_b_shifted = force_b - np.mean(force_b) + mean_force




PRIME NUMBER GENERATOR

def prnum_checker(num):
# prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number")
       
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")





SORTING FUNCTION


SELECTION SORT

def sortie(to_be_sorted):
       
    
    for i in range(len(to_be_sorted)):
        smallest = to_be_sorted[i]
        index = smallest + 1
        if index < smallest:
            smallest = index
    return smallest





MERGE SORT

def merge_sort(arr, begin, end):
    if end - begin > 1:
        middle = (begin + end)//2
        merge_sort(arr, begin, middle)
        merge_sort(arr, middle, end)
        merge_list(arr, begin, middle, end)
 
def merge_list(arr, begin, middle, end):
    left = arr[begin:middle]
    right = arr[middle:end]
    k = begin
    i = 0
    j = 0
    while (begin + i < middle and middle + j < end):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    if begin + i < middle:
        while k < end:
            arr[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            arr[k] = right[j]
            j = j + 1
            k = k + 1
 
 
arr = input('Enter the list of numbers: ').split()
arr = [int(x) for x in arr]
merge_sort(arr, 0, len(arr))
print('Sorted list: ', end='')
print(arr)




BUBBLE SORT

def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)




INSERTION SORT

def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


# Verify it works
random_list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)





  