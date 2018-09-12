print(1,2,3)
count=0
while count<10:
	print('num::',count)
	if count==5:
		break
	count=count+1
def sayHello(name,num):
	print("hello function",name,num)
sayHello('pavan kumar',123)

def sayHi(name='pavan kumar'):
	print("Hi function",name)
sayHi()

def getSum(n1,n2):
	sum=n1+n2
	return sum

sum=getSum(10,20)
print('Total sum is :',sum)

def lst(lt):
	lt.append(4)
	print('inside function',lt)

lt=[1,2,3]
lst=lst(lt)
print(lt)
print("out side function",lt)
# string functions
str="Hello World"
print(str.capitalize())
print(str.swapcase())
print(str.replace('World',"Everyone"))
print("Character count inside:",str.count('o'))
print(str.startswith("H"))
print(str.split())
print("World position starts at :",str.find('World'))
print("index gives error if not availbale :",str.index('W'))
print(str.isnumeric())