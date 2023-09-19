#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=1234
#Create a variable "sum_odd" and assign it 0.
sum_odd=0
a=var_int//1000
b=var_int//100%10
c=var_int%100//10
d=var_int%10
#Find the sum of the odd digits in the variable "var_int".
x=a%2
y=b%2
z=c%2
k=d%2
print(a*x+b*y+c*z+d*k)