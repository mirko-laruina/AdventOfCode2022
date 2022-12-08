#!/bin/env python3

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.size = 0
        self.parent = None

    def __repr__(self):
        s = self.name + "\t" + str(self.size) + "\n"
        for child in self.children:
            s += child.__repr__()

        return s


def update_dir_tree(node, size):
    node.size += size
    if node.parent != None:
        update_dir_tree(node.parent, size)

def get_sum_size_under(limit_size, root_node):    
    sum = 0
    for child in root_node.children:
        sum += get_sum_size_under(limit_size, child)

    return sum + (root_node.size if root_node.size <= limit_size else 0)

def get_min_sized_over(limit_size, root_node):
    if root_node.size < limit_size:
        return None

    candidate = root_node
    for child in root_node.children:
        child_candidate = get_min_sized_over(limit_size, child)
        if child_candidate is None:
            continue

        if child_candidate.size < candidate.size:
            candidate = child_candidate

    return candidate
    

with open("input.txt") as f:
    lines = f.readlines()

root = Node("")
current_directory = root
for line in lines[1:]:
    line = line.strip()
    if line[0] == "$":
        # command cd
        if line[2:4] == "cd":
            if line[5:7] == "..":
                next_node = current_directory.parent
            else:
                folder_name = line[5:]
                matching_children = list(filter(lambda c: c == folder_name, current_directory.children))
                if len(matching_children) == 0:
                    next_node = Node(current_directory.name + "/" + folder_name)
                    next_node.parent = current_directory
                    current_directory.children.append(next_node)
                else:
                    next_node = matching_children[0]

            current_directory = next_node
    elif line[0:3] != "dir":
        size, filename = line.split(" ")
        size = int(size)
        update_dir_tree(current_directory, size)
    

print("Total sum of folder under 100k:", get_sum_size_under(100000, root))

## Part 2
TOTAL_SIZE = 70000000
MIN_FREE_SPACE = 30000000

current_free_space = TOTAL_SIZE - root.size
needed_space = MIN_FREE_SPACE - current_free_space
folder_to_delete = get_min_sized_over(needed_space, root)
print("Folder to be deleted:", folder_to_delete.size)

