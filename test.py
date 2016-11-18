from plib import _Getch
from plib import switch

# name = input('Please input your name: ',)
# print('hello,',name)

#print('%s ,your asked rate:%d%%' % ('Sir',5))

'''s = 'Python-Chinese'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
'''

#List,Tuple
'''L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])'''

'''
height = float(input('your height(m):'))
weight = float(input('your weight(kg):'))
BMI = weight / (pow(height,2))
print'Result:',
if BMI < 18.5:
	print('light')
elif 18.5 < BMI <25:
	print('normal')
elif 25 < BMI <28:
	print('weighty')
elif 28 < BMI <32:
	print('fat')
else:
    print('serious fat')
print('BMI:%f'% BMI)
'''

'''
i = ['Boyce','Clare','Alex']
for x in i:
    getch()
    print 'hello, ' + x + '\r',
'''

'''
a = 255
print(hex(a)) #convert int to hex string
'''

'''
import math

def quadratic(a,b,c):
    if not isinstance(a,(int, float)) and isinstance(b,(int, float)) and isinstance(c,(int, float)):
        raise TypeError('Bad operand type')
    if (pow(b,2)-4*a*c) < 0:
        print('No Result')
        return None
    deta = math.sqrt(pow(b,2)-4*a*c)
    x1 = (-b + deta)/(2*a)
    x2 = (-b - deta)/(2*a)
    return x1,x2

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if(quadratic(a,b,c) != None):
    #tow method
    #x1,x2 = quadratic(a,b,c)
    #print('x1 = %f, x2 = %f\n' % (x1,x2))
    r = quadratic(a,b,c)
    print('x1 = %f, x2 = %f\n' % r)
else:
    print('Maybe you shulde input another set number.')
'''

'''
# tail recursion to avoid over stack
def fact(num,product = 1):
    if num == 1:
        return product
    return fact(num - 1,num * product)

# normal but over stack
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

a = fact(float(input('input a number to ask the data = n!')))
print('data = %f' % a)
'''

'''
i = 0
def hanoi(n,x,y,z):
    if n == 1:
        global i
        i += 1
        print(x,' ---> ',z)
    else:
        hanoi(n-1,x,z,y)
        hanoi(1,x,y,z)
        hanoi(n-1,y,x,z)
    return i    
n = int(input('Please input the layers of the Hanoi: '))
number = hanoi(n,'x','y','z')
print('Complete the Hanoi task need %d steps' % number)
'''

'''
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b, a+b
		n = n + 1
	return 'done'
n = int(input('Please input the layers of the Fib: '))
print(fib(n))
'''

'''
i = 0
quitflag = False

getch = _Getch()
while True:
    ch = getch()
    if ch == '\r':
        print("\nEnter keys('esc') to quit: ")
        i = 0
    else:
        for case in switch(ch):
            if case('e'): pass # only necessary if the rest of the suite is empty
            if case('E'): 
                if(i == 0):
                    i += 1
                    break
            if case('s'): pass # only necessary if the rest of the suite is empty
            if case('S'): 
                if(i == 1):
                    i += 1
                    break
            if case('c'): pass # only necessary if the rest of the suite is empty
            if case('C'): 
                if(i == 2):
                    quitflag = True
                    break        
            if case(): 
                i = 0;
    
    if(quitflag):
        print ("\nBye.")
        break
'''

'''
from functools import reduce
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
	    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))

print(str2int('569358614')+1)
'''

'''
def normalize(name):
	i = 0
	strlen = len(name)
	EndName = ''
	while(i < strlen):
		if(i == 0 and ord(name[i]) < 122 and ord(name[i]) >= 97):
			EndName += chr(ord(name[i]) - 32)
		elif(ord(name[i]) >= 65 and ord(name[i]) < 90):
			EndName += chr(ord(name[i]) + 32)
		else:
			EndName += name[i]
		i += 1
	return EndName
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''

'''
from functools import reduce

def prod(L):
	def multiply(x,y):
		return x*y
	return reduce(multiply,L)

print('3 * 5 * 7 * 9 = ',prod([3,5,7,9]))
'''

'''
from functools import reduce
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point          # nonlocal means the var in upper function but not global variable.
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
'''

