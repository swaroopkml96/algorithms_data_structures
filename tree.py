class Node:
    def __init__(self, ch, healths, pos):
        self.ch = ch
        self.health = healths
        self.pos = pos
        self.children = []
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'Node {self.ch} {self.health} {self.pos}'

class Tree:
    def __init__(self, root_node):
        self.root_node = root_node

    def get_last_node(self, s):
        return self.get_last_node_recursive(s, self.root_node)

    def get_last_node_recursive(self, s, from_node):
        if len(s) == 0:
            return from_node, s
        else:
            found = False
            for child in from_node.children:
                if child.ch == s[0]:
                    return self.get_last_node_recursive(s[1:], child)
            if not found:
                return from_node, s
                
    def add_nodes(self, s, health, pos):
        leaf, substring = self.get_last_node(s)
        if len(substring) == 0:
            leaf.health.append(health)
            leaf.pos.append(pos)
        else:
            current_node = leaf
            for ch in substring:
                child_node = Node(ch, [], [])
                current_node.children.append(child_node)
                current_node = child_node
            child_node.health.append(health)
            child_node.pos.append(pos)

    def print_tree(self):
        self.print_tree_recursive(self.root_node, '')

    def print_tree_recursive(self, from_node, tabs):
        print(tabs + str(from_node))
        for child in from_node.children:
            self.print_tree_recursive(child, tabs+'\t')

root_node = Node('ROOT', [], [])
tree = Tree(root_node)

tree.add_nodes('a', 12, 0)
tree.add_nodes('b', 1, 2)
tree.add_nodes('abab', 1, 3)

tree.print_tree()
