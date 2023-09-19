#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=2221
a=var_int//1000
b=var_int//100%10
c=var_int%100//10
d=var_int%10
#Print the number of odd digits in the variable "var_int".
a=a%2
b=b%2
c=c%2
d=d%2
print(a+b+c+d)