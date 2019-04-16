#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: HungarianAlgorithm.py
@time: 2019/1/3/003 10:01
@desc: 匈牙利算法实现最大匹配问题
'''

M=[]
class HungarianAlgorithm():

    def __init__(self, nx, ny, edge, cx, cy, visited):
        self.nx, self.ny=nx, ny
        self.edge = edge
        self.cx, self.cy=cx,cy
        self.visited=visited

    def max_match(self):
        res=0
        for i in self.nx:
            if self.cx[i]==-1:
                for key in self.ny:         # 将visited置0表示未访问过
                    self.visited[key]=0
                res += self.path(i)
        return res

    def path(self, u):
        for v in self.ny:
            if self.edge[u][v] and (not self.visited[v]):
                self.visited[v]=1
                if self.cy[v]==-1:
                    self.cx[u] = v
                    self.cy[v] = u
                    M.append((u,v))
                    return 1
                else:
                    if M.__len__() != 0:
                        if M.__contains__(v):
                            M.remove((self.cy[v], v))
                    if self.path(self.cy[v]):
                        self.cx[u] = v
                        self.cy[v] = u
                        M.append((u, v))
                        return 1
        return 0


# if __name__ == '__main__':
#     nx, ny = ['A', 'B', 'A', 'D'], ['E', 'F', 'G']
#     edge = {'A': {'E': 1, 'F': 0, 'G': 0}, 'B': {'E': 0, 'F': 1, 'G': 0},
#             'A': {'E': 1, 'F': 0, 'G': 0}, 'D': {'E': 0, 'F': 0, 'G': 0}}  # 1 表示可以匹配， 0 表示不能匹配
#     cx, cy = {'A': -1, 'B': -1, 'A': -1,'D': -1}, {'E': -1, 'F': -1, 'G': -1}
#     visited = {'E': 0, 'F': 0, 'G': 0}
#
#     print(HungarianAlgorithm(nx, ny, edge, cx, cy, visited).max_match())