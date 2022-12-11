# # multiplication table

# number = int(input('Enter the number to create multiplication tableL: '))
# for i in range(1, 11):
#     print(i*number)

# create dictionary
# list1 = []
# for i in range(1, 7):
#     list1.append(i)


# dic = {}

# for i in list1:
#     dic[i] = i**3
# print(dic) 

# # create dic and find sum
# dict = {}
# sum = 0
# for i in range(1,10):
#     dict[i] = i**2

#     sum += dict[i]
# print(sum)

# fibonacci
# term = int(input("Enter number of terms required: "))
# n1,n2 = 0,1

# if term <= 0:
#     print('Enter a valid positive number')
# elif term == 1:
#     print('fibonacci series is: ', n2)

# else:
#     count = 0
#     while count<term:
#         print(n1)
#         nth = n1+n2
        
#         n1 = n2
#         n2 = nth
        # count += 1
# armstrong
num = int(input('Enter number'))
sum  = 0
temp = num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp //= 10

if num == sum:
    print('its armstrong')
else:
    print('its not armstrong')

# reverse
num = int(input('enter a number'))
reversed_num = 0
while num != 0:
    digit = num%10
    reversed_num = reversed_num*10 + digit
    num //= 10

print(reversed_num)

