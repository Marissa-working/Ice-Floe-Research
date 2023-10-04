#reference: https://jrtechs.net/data-science/implementing-a-quadtree-in-python
import time
import random
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import uuid
import pandas as pd
import numpy as np
from typing import NamedTuple
from collections import OrderedDict

class Node(NamedTuple):
    """Node class is a square in the quardtree with (x0, y0) as coordinates, w as width and height, 
    children as list of four children nodes parent as list of parent node, id as unique id (only be used in debugging)"""
    x0: int
    y0: int
    width: int
    children: list
    parent: list
    id: int
        
class QTree():
    """QTree class which can do the fracture, weld, and graph of quardtree"""
    def __init__(self):
        """initialize the whole ice floe size is 1000 x 10000, leave_list, parent_list, size_distribution"""
        self.root = Node(0, 0, 1000, [], None, uuid.uuid4().hex[:4])
        self.leaf_list = [self.root]
        self.parent_list = []
        self.size_dist = OrderedDict([(self.root.width*self.root.width, [self.root])])
        
    def subdivide(self, node):
        """ divide the given node into four parts """
        w_ = float(node.width/2)
        x1 = Node(node.x0, node.y0, w_,[], [node], uuid.uuid4().hex[:4])
        x2 = Node(node.x0, node.y0+w_, w_, [], [node], uuid.uuid4().hex[:4])
        x3 = Node(node.x0 + w_, node.y0, w_, [], [node], uuid.uuid4().hex[:4])
        x4 = Node(node.x0+w_, node.y0+w_, w_, [], [node], uuid.uuid4().hex[:4])
        #x1, x2, x3, x4 becomes the children of the node
        node.children.append(x1)
        node.children.append(x2)
        node.children.append(x3)
        node.children.append(x4)
        
        # update the leaf_list, parent_list, size_dist
        self.leaf_list.remove(node) # the original node is not leaf node any longer
        self.leaf_list.append(x1) # the generated four children nodes are added to the leaf list
        self.leaf_list.append(x2)
        self.leaf_list.append(x3)
        self.leaf_list.append(x4)
        if node.parent != None and node.parent[0] in self.parent_list:
            self.parent_list.remove(node.parent[0])  # if node's parent is in the parent list, remove node's parent
        self.parent_list.append(node) # the original node becomes the parent node
        ## the size distribution changes: node disappear, add four children nodes
        if len(self.size_dist[node.width*node.width]) == 1:
            del self.size_dist[node.width*node.width]
        else:
            self.size_dist[node.width*node.width].remove(node)
        size = x1.width * x1.width
        if size not in self.size_dist:
            self.size_dist[size] = [x1,x2,x3,x4]
        else:
            self.size_dist[size] += [x1,x2,x3,x4]
    
    def weld(self, node):
        """weld the node's four children into a complete node"""
        # the original node is not parent node any longer
        self.parent_list.remove(node)
        # all children nodes are removed from leaf list
        self.leaf_list.remove(node.children[0])
        self.leaf_list.remove(node.children[1])
        self.leaf_list.remove(node.children[2])
        self.leaf_list.remove(node.children[3])
        # the original node becomse the leaf node
        self.leaf_list.append(node)
        ## the size distribution changes: four children nodes disappear, the parent node back
        child_size = node.children[0].width*node.children[0].width
        if len(self.size_dist[child_size]) == 4:
            del self.size_dist[child_size]
        else:
            for child in node.children:
                self.size_dist[child_size].remove(child)
                
        size = node.width*node.width
        if size not in self.size_dist:
            self.size_dist[size] = [node]
        else:
            self.size_dist[size].append(node)
        node.children.clear()

    def get_leaves(self):
        return self.leaf_list
    
    def get_parent(self):
        return self.parent_list
    
    def plot_size_distribution(self):
        sizes = list(self.size_dist.keys())
        sizes.sort()
        counts = [len(self.size_dist[i]) for i in sizes]
        print("sizes: ", sizes)
        print("counts: ",counts)
        plt.plot(sizes, counts, marker='o', linestyle='-')
        plt.yscale('log')
        plt.xscale('log')
        plt.xlabel('Node Size')
        plt.ylabel('Probability')
        plt.title('Size Distribution of ice floes')
        plt.show()
    
    def binning_plot(self, binsize):
        bins = {}
        dictionary = self.size_dist
        for value in dictionary:
            floe_count = len(dictionary[value])
            # count which bins the value should be in
            if value % binsize == 0:
                bin_num = value//binsize  ## ex: 5%5=0 and 5 is under 1~5
            else:
                bin_num = value//binsize +1 ## ex: 3%5=3, 3//5 = 0 and 3 is under 1~5
            size = bin_num * binsize
            if size not in bins:
                bins[size] = floe_count
            else:
                bins[size] += floe_count
        sizes = list(bins.keys())
        sizes.sort()
        counts = [bins[i] for i in sizes]
        print("sizes: ", sizes)
        print("counts: ",counts)
        plt.plot(sizes, counts, marker='o', linestyle='-')
        plt.yscale('log')
        plt.xscale('log')
        plt.xlabel('Node Size')
        plt.ylabel('Probability')
        plt.title('Binned Size Distribution of ice floes')
        plt.show()
    
    def graph(self):
        """graph the quardtree plot"""
        fig, ax = plt.subplots(figsize=(8, 8))
        plt.title("Quadtree")
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        c = self.leaf_list
        print("Number of segments: %d" %len(c))
        areas = set()
        for el in c:
            areas.add(el.width*el.width)
        print("Minimum segment area: %.3f units" %min(areas))
        for n in c:
            #print((n.x0, n.y0), n.width, n.height)
            rect = patches.Rectangle((n.x0, n.y0), n.width, n.width, fill=False)
            ax.add_patch(rect)
        patches_list = ax.patches
        plt.show()
