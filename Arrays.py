# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:41:31 2019

@author: harsh
"""


#tic tac toe desgin
class Board(object):
    def __init__(self):
        self.cells=[" "]*9
                   
    def display(self):
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
        print('------')
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('------')
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])
    
    def update(self, cell_num, player):
        if self.cells[cell_num-1] == " ":
            self.cells[cell_num-1] = player
            
        
        
board=Board()
board.display()
board.update()

        
def  display():
    cells=[" "]*9
    print(cells[0] + '|' + cells[1] + '|' + cells[2])
    print('------')
    print(cells[3] + '|' + cells[4] + '|' + cells[5])
    print('------')
    print(cells[6] + '|' + cells[7] + '|' + cells[8])
    
def player_input():
    marker=""
    while not(marker=='X' or marker=='O'):
        marker=input('Player 1: Do you want to be X or O?').upper()
    if marker=='X':
        return ("X","O")
    else:
        return ("O","X")

player_input()
        
        
    
display()



    
ord('a')+ord('f')

ord('b')+ord('e')


0+5//2
    










#Two sum
def twoSum(self, nums, target):
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            if(nums[i]+nums[j]==target and i!=j):
                return([i,j])


#2 stocks
class Solution(object):
    def maxProfit(self, prices):
        maximum=0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if(prices[j]-prices[i]>maximum):
                    maximum=prices[j]-prices[i]
                    print(prices[j],prices[i])
        return(maximum)
                    
            
        






#Max_Sub_Array
A=[-2,1,-3,4,-1,2,1,-5,4]

max_so_far=0
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        total=0
        for k in range(i,j):
            total=total+sum(A[i:j])
        if(total>max_so_far):
            max_so_far=total
            print(max_so_far,i,j)

print(max_so_far,i,j)        
            
        


#Word Search
word='SWE'
board=[['A','B','C'],
       ['B','E','D'],
       ['S','E','T'],
       ['W','E','T']
       ]
for i in range(0,len(board)):
    for j in range(0,len(board[0])):
        if word[j] in board[i][j]:
            board[i][j]='#'



#Move zeros
def zeros(nums):
        probe=0
        pivot=0
        while(probe<len(nums)):
            if(nums[probe]!=0):
                nums[probe],nums[pivot]=nums[pivot],nums[probe]
                pivot=pivot+1
            probe=probe+1
        return nums
zeros([1,0,11,0,0,4,0,5,0,12,0,4,4,4,0])


#Product of k-consecutive integers
#a=[1,2-4,-6,-2]
#k=3
#Expect=[-8,48,48]

s=[1,2-4,-6,-2]
k=3
for i in range(0,len(a)-k):
    if(i==0):
        s[i]=s[i]
        
    elif(i<=k):
        while(i>=1):
            s[i]=s[i]*s[i-1]
            i=i-1
    elif(i>k):
        count=k
        while(count>=0):
            count=count-1
            s[i]=s[i]*s[i-1]
            
        
        
#Bubble sort:
#Sort the elemenst in order to keep them in order:
            
a=[5,7,3,6,9,2,11]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)


#i=0
#j=0
#5>7- False
#a=[5,7,3,6,9,2,11]
#j=1
#7>3-True
#a=[5,3,7,6,9,2,11]
#j=2
#7>6-True
#a=[5,3,6,7,9,2,11]




#Merge Sort

nums=[1,3,5,7,8]
dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
for d in dic:
    print(d)
for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic


#Swap 2 3elements in array 1 and array 2 to make their
            
a=[4,1,2,1,1,2]


#Max volume that can be filled:
        max_vol=[]
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                max_vol.append((j-i)*(min(height[i],height[j])))
        return(max(max_vol))
        
        
#Contigious sum
        
array=[-4,4,-3,2,-7,9]

for i in range(1,len(array)):
    sum_maximum=max(array[i]+array[i-1],array[i-1])
    if(sum_maximum>current_maximum):
        current_maximum=array[i]
        
        
a=[1,5,2]
del(max(a))



    
    