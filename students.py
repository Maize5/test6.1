#!/usr/bin/env python3
#-*- coding:utf-8 -*-
n = int(input("Please enter the number of students: "))
data = {}   #用来存储数据的字典变量
Subjects = ('Physics', 'Math', 'history')  #所有科目
for i in range(0, n):
	name = input('Enter the name of the student {}:'.format(i + 1))  # 获得学生名字
	marks = []
	for x in Subjects:
		marks.append(int(input('Enter marks of {}:'.format(x))))  #获得每一科的分数
	data[name] = marks

print("-" * 20)
print(data)
print("-" * 20)


for x, y in data.items():    #items（）方法遍历字典
	total = sum(y)
	print("{}'s total marks {}".format(x, total))
	if total < 120:
		print(x, "failed :(")
	else:
		print(x, "passed :)")

