class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):

        def _delete(node, word, depth): # Auxiliary.
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]

            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete(self.root, word, 0)
            
    def list_words(self):
        
        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words

    def suggestions_rec(self, node, word):
        if node.is_end_of_word:
            print(word)
        for a, n in node.children.items():
            self.suggestions_rec(n, word + a)
    
    def print_auto_suggestions(self, key):
        node = self.root

        for a in key:
            if not node.children.get(a):
                return 0
            node = node.children[a]
            
        if not node.children:
            return -1

        self.suggestions_rec(node, key)
        return 1

trie = Trie()
trie.insert("casa")
trie.insert("casamento")
trie.insert("casulo")
trie.insert("cachorro")

print(trie.list_words())

print(trie.search("casa"))

trie.print_auto_suggestions("cas")

trie.delete("casa")

print(trie.list_words())

trie.print_auto_suggestions("cas")