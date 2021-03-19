print("enter your name")
x=input()     #syntax to take input from user
print("entered name is",x)


print("enter a number")
x=input()       #the input take is in the form of str(), so we have typecasted to int() below.
print("entered number is",int(x))
print("enter a number u wanna add to the previous")
y=input()
print("sum of both is",int(x)+int(y))   #typecasting used

#String Slicing and functions
mystring="terna engineering college"
print(len(mystring))
print(mystring[4])
print(mystring[0:5])        #string slicing
print(mystring[:70])
print(mystring[4:15])
print(mystring[0:25:2])      #advanced slicing
#2 will skip 1 character alternately
print(mystring[0:25:2])
#   0  1   2   3   4  5  6  7  8  9  10 11
#    a  y   u   s   h     p  a  r  a  t  e
# -12 -11 -10 -9 -8  -7 -6 -5 -4 -3 -2  -1  #indexing
print(mystring[-8:-3])
print(mystring[::-1])   #makes the order of the string opposite( string ko ulta karta hai
print(mystring[::-2])   #string ulta karke alternate characters print karta hai

print(mystring.endswith("ege"))
print(mystring.count("e"))
print(mystring.capitalize())
print(mystring.find("engi"))
print(mystring.upper())
print(mystring.replace("engineering","dental"))
