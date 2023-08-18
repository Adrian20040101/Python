# m = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]
#
# l=[]
# n = len(m)
# i=0
# j=0
#
# while i<n and j<n:
#         for j in range (n):
#                 if m[i][j] not in l:
#                         l.append(m[i][j])
#         j=i
#         for i in range (n):
#                 if m[i][j] not in l:
#                          l.append(m[i][j])
#         i=j
#
#         i+=1
#         j+=1
# print (l)
# n = int(input('n= '))
# a = 0
# for i in range (1,n):
#     a = a + pow(-1, i+1) * i * (i+1)
# print (a)
# from math import ceil
#
# m = [
# [12, 6, 3, 0],
# [13, 7, 4, 1],
# [14, 8, 5, 2],
# [15, 10, 11, 9]
# ]
#
# def ex2():
#     size = len(m)
#     start = 0
#     cicluri = ceil(size / 2)
#
#     for j in range (cicluri):
#         for i in range (start, size):
#             print (m[start][i], end = ' ')
#         for i in range (start+1, size):
#             print (m[i][size-1], end = ' ')
#         for i in range (size-1, start, -1):
#             print (m[size-1][i-1], end = ' ')
#         for i in range (size-2, start, -1):
#             print (m[i][start], end = ' ')
#         start+=1
#         size-=1
#
# ex2()

# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
#
# def ex_1a():
#     i = 0
#     j = 0
#     n = len(m)
#     l=[]
#     while i < n and j < n:
#         for j in range (n):
#             if m[i][j] not in l:
#                 l.append(m[i][j])
#         j=i
#         for i in range (n):
#             if m[i][j] not in l:
#                 l.append(m[i][j])
#         i=j
#         i+=1
#         j+=1
#     print (*l)
# ex_1a()
