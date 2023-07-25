# 1. Trie Data structure to store data of text file
# used Trie since it can store a large amount of strings and The pattern matching can be done efficiently using tries
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# 2. Spelling checker class to search tree and add words to it.
class SpellingChecker:
    def __init__(self):
        self.root = TrieNode()

    # Time complexity: O(N), where N is the length of the word
    # Space complexity: O(N), as we store the word character by character in the trie
    def add_word(self, word):
        node = self.root # root of the trie that represents empty string
        for char in word:
            if char not in node.children: # if character not a child of current node 
                node.children[char] = TrieNode() # create new trie node 
            node = node.children[char] # move to the next node
        node.is_end_of_word = True # mark the last node as the end of the word

    # Time complexity: O(N + M), where N is the length of the word, and M is the number of similar words found (4 in this case)
    # Space complexity: O(1), as we only return a list of 4 words.
    def find_nearest_words(self, word):
        # function to find nearest words
        def find_words_from_node(node, current_prefix, result):
            # if 4 near words found or no near characters found return 
            if len(result) == 4 or not node:
                return
            # if node is final node then append word to result
            if node.is_end_of_word: 
                result.append(current_prefix)

            # for characters sorted in lexicographic order call the function recursively 
            for char in sorted(node.children.keys()):
                find_words_from_node(node.children[char], current_prefix + char, result)

        
        #starting from root search for characters of word until either character not found or word ends 
        node = self.root
        for char in word:
            if char not in node.children:
                return []

            node = node.children[char]

        nearest_words = []
        find_words_from_node(node, word, nearest_words)
        # return nearest words
        return nearest_words


#initialize a spelling checker object
spell_checker = SpellingChecker()
# read text file and if any error occurs replace the charcater having the error with a placeholder and add all words to the tree
with open('dictionary.txt','r',encoding='utf-8',errors='replace') as f: 
    for line in f:
        spell_checker.add_word(line.strip()) # .strip to eliminate white space and newline characters.

# Test the spell checker
input_word = "abac"
nearest_words = spell_checker.find_nearest_words(input_word)
print("Nearest words to 'abac':", nearest_words)

# Add a new word to the dictionary
new_word = "aamar"
spell_checker.add_word(new_word)
