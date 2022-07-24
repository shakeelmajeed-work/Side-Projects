n = int(input())
numbers = [int(i) for i in input().split()]
needed_sum = n*(n+1)//2
actual_sum = sum(numbers)
print(needed_sum-actual_sum)



'''Below code works but is too slow'''

# n = int(input())
# numbers = [int(i) for i in input().split()]

# guess = 1 
# found = False
# flag = 1
# while found==False:
#     if flag==0: 
#         found = True
#     for i in range(0,n-1):
#         flag = 0
#         if numbers[i] == guess:
#             guess+=1
#             flag = 1
#             break
    
# print(guess)

'''Works as well'''
# n = int(input())
# numbers = [int(i) for i in input().split()]

# for i in range(1,n):
#     if i not in numbers:
#         print(i)
