import numpy 

#Empty list
rand_list = []

#Generate 25000 samples and add to our empty list
#Our mean is 0 and our standard deviation is 5 
for x in range(0, 25000):
    rand_list.append(numpy.random.normal(0,5))
    
#We now find the mean by adding up all the values in the list 
#And dividing it by the total size of the list
sum = 0
for x in range(len(rand_list)):
    sum = sum + rand_list[x]
mean = sum/len(rand_list)
print('Our mean is ' + str(mean))

#We now find the standard deviation of the values in the list
#Using the mean that we found above
sum = 0
for x in range(len(rand_list)):
    sum = sum + (mean - rand_list[x]) ** 2
variance = sum / len(rand_list)
standard_deviation = variance ** (1/2)
print('Our standard deviation is ' + str(standard_deviation))