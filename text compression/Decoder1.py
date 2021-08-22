import pickle    

class tree:
    def __init__(self, val, freq, left= None, right = None):
       self.freq = freq
       self.val = val
       self.left = left
       self.right = right
       self.code = ''

def get_code(file):  

    with open(file, 'rb') as f:
        binary = pickle.load(f)

    code = bin(binary)
    code = code.split("b")
    huffman = code[1][1:]
    
    return huffman

def get_tree(key):
    with open(key, 'rb') as t:
        root = pickle.load(t)
    return root


def Decode(root,code):
    text = ''
    current = root
    while len(code) > 0:
        print(current.val)
        if current.left == None or current.right == None:
            text += current.val
            current = root
        if code[0] == '0':
            current = current.left
        elif code[0] == '1':
            current = current.right
        code = code[1:]
    print(text)

file = 'test_compressed'
key = 'test_tree'

code = get_code(file)
root = get_tree(key)
Decode(root,code)
