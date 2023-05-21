# M_M_M_V_S
#Mean_Median_Mode_Variance_StandardDeviation_ exercises
import math
#Complete the mean function to make it return the mean of a list of numbers
def mean(data):
    result =  0
    for i in data :
        result =  result + i
    me = result / len(data) 
    return me
  #Complete the median function to make it return the median of a list of numbers
def median(data):
    med = 0
    data.sort()
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        med = ( data[mid - 1] + data[mid] ) / 2
    else:
            med = data[mid]
    return med
  #Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]
def mode(data):
    datac = []
    for i in data:
        datac.append(data.count(i))
    datac.sort()
    n = datac[len(datac) -1]
    for j in data: 
        if data.count(j) == n:
          return j
        
#Complete the variance function to make it return the variance of a list of numbers
def variance(data):
    vari = 0
    for i in data: 
        vari = vari + (i - mean(data))**2
    return vari / len(data)   
  #Complete the stddev function to make it return the standard deviation 
#of a list of numbers
def stddev(data):
    var = variance(data)
    return  math.sqrt(var)
    
  

