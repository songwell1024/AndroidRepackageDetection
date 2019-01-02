#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: TreeGrah.py
@time: 2018/12/19/019 9:32
@desc:
'''

#把树映射成为图

def html_to_dom_tree(root):
  node_id = 1
  q = deque()
  graph = nx.Graph()

  q.appendleft({'element': root, "root_id": node_id})
  while len(q):
    node = q.pop()

    if node and node['element'].name == "body":
      graph.add_node(node_id, element=node['element'].name)
      node_id += 1

    root_id = node['root_id']
    labels[root_id] = node['element'].name

    for t in node['element'].contents:
      if t and t.name:
        graph.add_node(node_id, element=t.name)
        graph.add_edge(root_id, node_id)
        q.appendleft({"element": t, "root_id": node_id})
        node_id += 1

  return graph