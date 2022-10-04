# 1

my_int = 3020640106802000
result = str(my_int)
print(result.count('0'))

# 2

my_int = 230054030000
count = 0
while my_int % 10 == 0:
    count += 1
    my_int //= 10
print(count)

# 3

my_list_1 = ['hello', 'norms', 'good', 'bad']
my_list_2 = ['bye', 'very', 'name', 'happy']
my_result = result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

# 4

my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:] + [my_list[0]]
print(new_list)

# 5

my_list = [1, 2, 3, 4, 5]
my_list.pop(0)
my_list.append(1)
print(my_list)

# 6

line = '153 плюс 27 минус 93 умножить 61'
new_list = line.split()
num_list = []
for i in new_list:
    if i.isdigit():
        num_list.append(int(i))
print(sum(num_list))

# 8

my_str = 'abcde'
new_list = []
line = len(my_str)
for i in range(0, line, 2):
    if i < line - 1:
        new_list.append(my_str[i] + my_str[i + 1])
    else:
        new_list.append(my_str[i] + '_')
print(new_list)

# 9

my_str = [2, 4, 1, 5, 3, 9, 0, 7]
number = 0
for i in range(1, len(my_str) - 2):
    if my_str[i - 1] < my_str[i] and my_str[i] > my_str[i + 1]:
        number += 1
print(number)

# 10

my_list = [1, 3, 'hello', 54, 'good', 4, 72, 'vasa']
new_list = [i for i in my_list if type(i) == str]
print(new_list)

# 11

my_str = '1, 8, 3, vasa, 3, 52, 7, 8, 49, piton, vasa'
my_set = set(my_str)
my_list = []
for i in my_set:
    if my_str.count(i) == 1:
        my_list.append(i)
print(my_list)

# 12

my_str1 = '1, 82, 3, vasa, 3, 52, 8, 49, piton, vasa'
my_str2 = '33, 8, 3, parom, 3, 52, 7, 90, piton, vasa'
my_list = list(set(my_str1) & set(my_str2))
print(my_list)

# 13
