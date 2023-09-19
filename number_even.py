#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=2221
a=var_int//1000
b=var_int//100%10
c=var_int%100//10
d=var_int%10
#Print the number of even digits in the variable "var_int".
a=(a%2-1)*(-1)
b=(b%2-1)*(-1)
c=(c%2-1)*(-1)
d=(d%2-1)*(-1)
print(a+b+c+d)