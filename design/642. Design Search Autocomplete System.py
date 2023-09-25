from typing import List
import collections


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        for i, sentence in enumerate(sentences):
            node = self.trie
            for char in sentence:
                node = node.setdefault(char, {})
            node['#'] = times[i]
        
        self.node = self.trie
        self.predix = ''

    def input(self, c: str) -> List[str]:
        if c == '#':
            if '#' in self.node:
                self.node['#'] += 1
            else:
                self.node['#'] = 1
            self.node = self.trie
            self.predix = ''
            return []

        if c not in self.node:
            self.node[c] = {}
        self.node = self.node[c]
        self.predix += c

        ans = []

        def dfs(node, predix):
            for char in node:
                if char == '#':
                    ans.append((predix, node['#']))
                else:
                    dfs(node[char], predix + char)

        dfs(self.node, self.predix)
        ans.sort(key=lambda x: (-x[1], x[0]))
        return [sentence for sentence, _ in ans[:3]]