class Node:
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None

def build_prefix_tree(prefix_dict): #建立樹
    root = Node()
    for prefix, char in prefix_dict.items():
        current_node = root
        for bit in prefix:
            if bit == '0':
                if current_node.left is None:
                    current_node.left = Node()
                current_node = current_node.left
            elif bit == '1':
                if current_node.right is None:
                    current_node.right = Node()
                current_node = current_node.right
        current_node.char = char
    return root

def decode_prefix_code(code, root): #解碼
    decoded_string = ""
    current_node = root
    
    for bit in code:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right
        
        if current_node.char:
            decoded_string += current_node.char
            current_node = root
    
    return decoded_string

# prefix_dict = {
#     "10": "m",
#     "00": "i",
#     "11": "s",
#     "01": "p"
# }

prefix_dict = {
    "10": "t",
    "00": "e",
    "11": "n",
    "01": "s"
}

#mississipi
#code = "10001111001111000100"
#tennessee
code = "100011110001010000"

prefix_tree = build_prefix_tree(prefix_dict)
decoded_message = decode_prefix_code(code, prefix_tree)
print("Decoded message:", decoded_message)