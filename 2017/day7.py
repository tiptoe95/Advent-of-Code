#!/bin/python3


import random
import statistics


def main():
    input_file = 'inputs/input_day7.txt'
    with open(input_file, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            try:
                node, children = line.split("->")
                children = [x.strip(",") for x in children.split()]
            except ValueError as e:
                node = line
                children = []
            name, weight = node.split()
            weight = int(weight.strip("()"))

            new_node = Node(name, weight, children)
    # PART 1
    part1()

    # PART 2
    part2()


def part1():
    print("populating parents.....", end='\r')
    Node.populate_parents()
    print("populating parents.....done")
    print(Node.root.name)


#todo:
def part2():
    Node.root.balance()


class Node():
    census = {}
    root = None

    def __init__(self, name, weight, children):
        self.name = name
        self.census[self.name] = self
        self.weight = weight
        self.totalweight = None
        self.children = children
        self.parent = None
        self.balanced = None

    def balance(self):
        #check amount of children
        if len(self.children) == 2:
            print("2 chit'lin, bruh")
        elif len(self.children) == 0:
            self.balanced = True
            self.totalweight = self.weight
            return

        #recursion
        for child in self.children:
            if not Node.census[child].balanced:
                Node.census[child].balance()
        #determine if disc is balanced
        mode = statistics.mode([Node.census[child].totalweight for child in self.children])
        for child in self.children:
            if Node.census[child].totalweight == mode:
                Node.census[child].balanced = True
            else:
                Node.census[child].balanced = False
                print(f"weight for '{Node.census[child].name}' should be {mode}")
        # sum up weights
        self.totalweight = sum(Node.census[child].totalweight for child in self.children)
        
    @classmethod
    def populate_parents(cls):
        for node in cls.census.values():
            for child in node.children:
                child_obj = cls.census[child]
                child_obj.parent = node
        if cls.root == None:
            cls.find_root()

    @classmethod
    def find_root(cls):
        random.seed()
        node = random.choice(list(cls.census.values()))
        while node.parent:
            node = node.parent
        cls.root = node


if __name__ == "__main__":
    main()
