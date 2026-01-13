class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
            node.count += 1
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_end_of_word

    def unique_prefix(self, word):
        node = self.root
        prefix = []
        for letter in word:
            if letter not in node.children:
                break
            node = node.children[letter]
            prefix.append(letter)
            if node.count == 1:
                break
        return "".join(prefix)


if __name__ == "__main__":
    words = ["dog", "cat", "apple", "apricot", "fish"]
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        print(trie.unique_prefix(word))
