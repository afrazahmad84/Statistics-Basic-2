#!/usr/bin/env python
# coding: utf-8

# Q1. What are the three measures of central tendency?
# 
# Ans:-
# 
# 1.Mean
# 
# 2.median
# 
# 3.Mode

# In[ ]:





# Q2. What is the difference between the mean, median, and mode? How are they used to measure the
# 
# central tendency of a dataset?
# 
# Ans:-
# 
# 1.Mean:-it is used to find the average of total number.if we have given a list then first we will sum all the total number 
# 
# after then we will divide count of total numbers.
# 
# 2.median:- The median is the middle number.if the given number is descending order then first we will sort the number into 
# 
# the ascending then find the median if the number is even then first we will find average of both number after that 
# 
# it is called mediam.
# 
# 3.Mode:-The most frequent number—that is, the number that occurs the highest number of times. Example: The mode of {4 , 2, 4, 3, 2, 2}
# 
# 
# 
# 
# 

# In[ ]:





# In[52]:


from scipy import stats as st
import numpy as np
l=[178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

np.std(l)


# In[ ]:





# Q3. Measure the three measures of central tendency for the given height data:
#     
# [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
# 
# 
# Ans:-
# 
# 1.Mean:- 177.01875
# 
# 2.median:-177.0
# 
# 3.Mode:-177

# In[ ]:





# Q4. Find the standard deviation for the given data:
# 
# [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
# 
# Ans:-
# 
# standard deviation :- 1.7885814036548633
# 

# In[ ]:





# Q5. How are measures of dispersion such as range, variance, and standard deviation used to describe
# 
# the spread of a dataset? Provide an example.
# 
# Ans:-
# 
# Measures of dispersion describe the spread of the data. They include the range, interquartile range, standard deviation and
# 
# variance. The range is given as the smallest and largest observations. This is the simplest measure of variability.
# 

# In[ ]:





# Q6. What is a Venn diagram?
# 
# Ans:-A Venn diagram is a widely used diagram style that shows the logical relation between sets

# Q7. For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find.
# 
# (i) A ∩ B
# 
# (ii) A ⋃ B
# 
# (i)  {2, 6}
# 
# (ii) {0, 2, 3, 4, 5, 6, 7, 8, 10}
# 

# In[59]:


A = set((2,3,4,5,6,7))
B = set((0,2,6,8,10))

print(A.intersection(B))
print(A.union(B))


# 

# Q8. What do you understand about skewness in data?
# 
# Ans:-
# 
# Skewness is a measurement of the distortion of symmetrical distribution or asymmetry in a data set.

# In[ ]:





# Q9. If a data is right skewed then what will be the position of median with respect to mean?
# 
# Ans:-in right side more data will be there.
# 
# Mean>=median>=mode
# 

# In[ ]:





# Q10. Explain the difference between covariance and correlation. How are these measures used in
# 
# statistical analysis?
# 
# Covariance can take any value between negative infinity and positive infinity.
# 
# while correlation takes values between -1 and 1. 
# 
# A positive covariance indicates that both variables move in the same direction while a negative covariance indicates that they move in opposite directions.
# 
# Correlation is a standardized measure of covariance that ranges from -1 to 1.
# 
# A correlation of 0 indicates that there is no relationship between the two variables while a correlation of 1 indicates a
# 
# perfect positive relationship and a correlation of -1 indicates a perfect negative relationship2.

# In[ ]:





# Q11. What is the formula for calculating the sample mean? Provide an example calculation for a
# 
# dataset.
# 
# Ans:-
# 
# X̄ = (Σ xi) / n

# In[ ]:





# Q12. For a normal distribution data what is the relationship between its measure of central tendency?
# 
# Ans:-
#     
# In normal distribution the mean, median and mode all are perfectly at the center.
# 
# (mean = median = mode)

# In[ ]:





# Q13. How is covariance different from correlation?
# 
# Ans:-
#     
# Covariance:-Covariance can take any value between negative infinity and positive infinity. 
#     
# Correlation:- while correlation takes values between -1 and 1, And it check the relation between two values that how much 
#     
# strong correlation to each other.
# 
# 

# In[ ]:





# Q14. How do outliers affect measures of central tendency and dispersion? Provide an example.
# 
# Ans:-
# 
# When a outlier is present it can effect the shape of the graph, if we have outliers to the right of the graph.
# 
# These outliers are causing the mean to increase, but if we have outliers to the left of the graph these outliers are
# 
# dragging down the mean
# 

# In[ ]:




