## Task 1
minutes_in_week = 60*24*7

## Task 2
remainder_without_mod =2304811-((2304811//47)*47)

## Task 3
divisible_by_3 = ((673 % 3 == 0) and (909%3==0))

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { x**2 for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 1, 2, 4 }
Y1 = { 6, 7, 8 }

## Task 8: enter in the two new sets
X2 = { 0, 1, 2 }
Y2 = { 5, 10, 20 }

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {(x*(base**2) + y*(base**1) +z*(base**0)) for x in digits for y in digits for z in digits}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = {x for x in S if x in T}

## Task 11
L_average = (20+10+15+75)/4 # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum =sum({sum(x) for x in LofL})

## Task 13
cartesian_product = [[letter,number] for letter in ['A','B','C'] for number in [1,2,3]]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if(i+j+k)==0] 

## Task 15
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if(i+j+k)==0 and (i,j,k)!=(0,0,0)]

## Task 16
first_of_tuples_list = [(i,j,k) for i in S for j in S for k in S if(i+j+k)==0 and (i,j,k)!=(0,0,0)][0]

## Task 17
L1 =[0, 1, 0, 1] # <-- want len(L1) != len(list(set(L1)))
L2 = [2,3,1,0] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = [...]

## Task 19
L = ['A','B','C','D','E']
range_and_zip = ...

## Task 20
list_sum_zip = [...]

## Task 21
U = [6, 2, 10, 20, 6]
V = [12, 0, 1, 2, 4, 10, 90]
list_sum_enumerate = [...]

## Task 22
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [...]

## Task 23
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [...] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [...] # <-- as you do here

## Task 24
square_dict = {...}

## Task 25
D = {'red','white','blue'}
identity_dict = {...}

## Task 26
base = 10
digits = set(range(10))
representation_dict = {...}

## Task 27
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { ... }

## Task 28
def nextInts(L): [ ... ]

## Task 29
def cubes(L): [ ... ] 

## Task 30
def dict2list(dct, keylist): [ ... ]

## Task 31
def list2dict(L, keylist): { ... } 

