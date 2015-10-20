#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
探索対象として二分木構造を考える
目的データを見つけた場合、経路を返す
"""

import sys
import random

class Node:
	def __init__(self,data):
		self.data = data
		self.edges = list()
	def __str__(self):
		output = "{data:" + str(self.data) + ",edge_num:" + str(len(self.edges)) + ",edge:"
		for i,c in enumerate(self.edges):
			output = output + "[" +str(i) +"]"+str(c.data)
		output = output + "}"

		return output

def chk_goal(node):
	if node.data == 88:
		return True
	else:
		return False

def make_b_tree(n):
	graph = list()
	root = Node(0)
	graph.append(root)
	for i in range(1,n):
		node = Node(i)
		for j in range(0,i):
			if len(graph[j].edges) >= 2:
				continue
			else:
				graph[j].edges.append(node)
				break
		graph.append(node)
	return graph

def dfs(graph,node):
	if chk_goal(node):
		return [node.data]
	else:
		for child in node.edges:
			if child in checked:
				return []
			d = dfs(graph,child)
			if len(d) > 0:
				a = list(d)
				a.append(node.data)
				return a
	checked.append(node)
	return []

checked = list()
graph = make_b_tree(100)
route = dfs(graph,graph[0])
print(route)
					
