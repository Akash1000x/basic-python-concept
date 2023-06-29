#1

# def my_function():
#     print("My first function")

# my_function()

#2


# def my_function(name):
#     print("My name is",name)

# my_function("Akash Kumawat")

#3


# def my_function(fname,lname):
#     print("My last name is",lname)

# my_function("Akash",lname="kumawat")

#4

# def my_function(*brother):
#     print("My elder brother name is",brother[2])

# my_function("Akash","ashok","hitesh","vikash")

#5


# def my_function(bros):
#     for i in range(len(bros)):
#         print(bros[i])


# bhai = ("Akash","ashok","hitesh","vikash")
# my_function(bhai)

#6

# def My_function(number1,number2):
#     # print("result is",number1*number2)
#     result = number1*number2
#     return result

# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))

# answer = My_function(a,b)
# print(answer)


#recursion

# def recursion(k):
#     if (k==0):
#         return 1
#     else:
#         return k + recursion(k-1)
    
# print(recursion(6))

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)




# def factorial(n):
#     if n ==0 | n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))


# def number(n):
#     if n>=0:
#         number(n-1)
#         print(n)
#     else :
#         return
    
# number(10)

#____________________

def myfunction(n):
    return lambda a: a*n

mydoubler = myfunction(2)
tripluer = myfunction(3)

print(mydoubler(10))
print(tripluer(10))