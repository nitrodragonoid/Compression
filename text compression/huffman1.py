import pickle
from typing import Literal

# Defining a class for a tree
class tree:
    def __init__(self, val, freq, left= None, right = None):
       self.freq = freq
       self.val = val
       self.left = left
       self.right = right
       self.code = ''

# Defining Queue
class Queue():
    def __init__(self):
        self.lst = []
    
    def enqueue(self,element,priority):
        insert = False
        for i in self.lst:
            if i[1] >= priority:
                insert = True
                self.lst.insert(self.lst.index(i),(element,priority))
                break
        if insert == False:
            self.lst.append((element,priority))
    
    def is_empty(self):
        if len(self.lst) == 0:
            return True
        return False

    def dequeue(self):
        if len(self.lst) == 0:
            return False
        else:
            top = self.lst[0]
            self.lst.remove(top)
            return top

    def front(self):
        if len(self.lst) == 0:
            return False
        else:
            return self.lst[0][0]
        
    def display(self):
        print(self.lst)

# Function that creates a tree for huffman code
def huffman_tree(text):

    # Computing the frequencies
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Sorting them with a priority queue
    priority_Queue = Queue()
    for j in freq:
        priority_Queue.enqueue(tree(j,freq[j]),freq[j])


    while len(priority_Queue.lst) > 1:
        
        left = priority_Queue.lst[0][0]
        right = priority_Queue.lst[1][0]

        left.code = 0
        right.code = 1

        if len(left.val) > 1 or len(right.val) > 1:
            parent = tree('', left.freq + right.freq, left, right)
        else:
            parent = tree(left.val + right.val, left.freq + right.freq, left, right)

        priority_Queue.dequeue()
        priority_Queue.dequeue()

        priority_Queue.enqueue(parent,parent.freq)
    
    print(priority_Queue.lst[0][0].freq)
    return priority_Queue.lst[0][0]
        
# Function that extracts huffman code from a given tree
def huffman_code(root, codes_dict,code = ''):

    code += str(root.code)

    if root.left != None:
        huffman_code(root.left, codes_dict, code)
    if root.right != None:
        huffman_code(root.right, codes_dict, code)
 
    if root.left == None and root.right == None:
        codes_dict[root.val] = code
 
# Function that takes a txt file and compress it in huffman code
def compress_text(filename):
    
    # Open and read text file
    with open(filename,'r') as f:
        text = f.read()
        f.close()

    # Gets huffman code for the file    
    codes_dict = {}
    huff_tree = huffman_tree(text)

    huffman_code(huff_tree, codes_dict, code = '')
    
    # Making a code for the text
    encoded = ''
    for i in text:
        encoded += codes_dict[i]

    return (huff_tree,encoded)


def compressed_file(codes, newfile):
    
    # Saving the code
    codetext = "1" + codes[1]

    literal = str(codetext)
    binary = int(literal,2)

    with open(newfile+"_compressed", 'wb') as z:
        pickle.dump(binary, z)
 
    # Saving the key
    with open(newfile+"_tree", 'wb') as b:
        pickle.dump(codes[0], b)
 

# Runnning the code
file_to_be_compressed = 'test.txt'
file_to_compress_to = 'test'

compressed_file(compress_text(file_to_be_compressed), file_to_compress_to)