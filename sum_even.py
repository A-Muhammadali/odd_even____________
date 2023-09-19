#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=4563
#Create a variable "sum_even" and assign it 0.s
a=var_int//1000
b=var_int//100%10
c=var_int%100//10
d=var_int%10
#Find the sum of the even digits in the variable "var_int".
x=(a%2-1)*(-1)
y=(b%2-1)*(-1)
z=(c%2-1)*(-1)
k=(d%2-1)*(-1)
print(a*x+b*y+c*z+d*k)
