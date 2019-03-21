class Node:
    def __init__(self, ch, health, pos):
        self.ch = ch
        self.health = health
        self.pos = pos
        self.children = []

class Tree:
    def __init__(self, root_node):
        self.root_node = root_node

    def get_last_node(self, s):
        return self.get_last_node_recursive(s, self.root_node)

    def get_last_node_recursive(self, s, from_node):
        pass