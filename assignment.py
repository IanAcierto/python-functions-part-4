numList = [5,8,10]
num_min = 0
num_max = 10
num_num = 5
string = 'i took the woooook to polaaand'

def max_num(n): #find the maximum of three numbers
  print(max(n))  
max_num(numList)

def multi_list(n):#multiply all the numbers in a list
  product = 1
  for i in n:
    product = product * i
  return product
multi_list(numList)

def rev_string(t):#reverse a string
  print(t[::-1])
rev_string(string)

def num_within(min, max, num):#check whether or not a number falls within a given range
  if(min<num<max): return print('in range')
  else:return print('not in range')
num_within(num_min, num_max, num_num)

def pascal(n):#do that
  
  for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    
    C = 1
    for j in range(1, i+1):
 
        print(' ', C, sep='', end='')
 
        C = C * (i - j) // j
    print()
pascal(1234)
  
