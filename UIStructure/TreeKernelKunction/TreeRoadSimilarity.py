#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: TreeRoadSimilarity.py
@time: 2018/12/19/019 9:31
@desc:
'''

#基于路径的相似性比较

subpath_track = {}

def generate_subpaths(path, l):
  if l == len(path):
    if tuple(path) not in subpath_track:
      subpath_track[tuple(path)] = 1
    else:
      subpath_track[tuple(path)] += 1
  else:
    index = 0
    while l+index-1 < len(path):
      if tuple(path[index: l+index]) not in subpath_track:
        subpath_track[tuple(path[index: l+index])] = 1
      else:
        subpath_track[tuple(path[index: l+index])] += 1
      index += 1

    generate_subpaths(path, l+1)


def get_subpaths(graph, root, track, path):
  track[root] = True

  if graph.degree(root) == 1:
    generate_subpaths(path, 1)
  else:
    for node in graph.neighbors(root):
      if node not in track:
        get_subpaths(graph, node, track, path + [node, ])


def kernel_subpath(t1, t2, common_track):
  kernel_v = 0
  for p in subpath_track:
    kernel_v += common_track[t1][p]*common_track[t2][p]

  return kernel_v