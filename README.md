# Python challenges 

mean_median_calculator - Python code to calculate median and mode from a given list.

**_Median:_**
The median of a list of values is the value which lies in the middle when we sort the data either in ascending or descending order.

Steps to find a median:
1. Sort the given values in ascending order.
2. Evaluate whether number of elements in the list are odd or even.
   For even number of elements calculate the average of middle two numbers.
   For odd number of elements pick the middle element by dividing the length by 2.


**Mode:**
The mode is the most frequent value in a given list.

Steps to find a mode:
1. Sort the given values in ascending order.
2. Compare two consecutive elements and increment the current_count when they are same.
3. Compare max_count with current_count.
   When the current_count is greater than max_count then update it to latest current_count.