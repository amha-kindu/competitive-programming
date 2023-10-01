#include <iostream>
#include <vector>

class TrieNode {
public:
    vector<TrieNode*> children;

    TrieNode() {
        children = vector<TrieNode*>(2, nullptr);
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    void insert(int num) {
        TrieNode* node = root;
        for (int i = 31; i > -1; --i) {
            int bit = (num >> i) & 1;
            if (!node->children[bit]) {
                node->children[bit] = new TrieNode();
            }
            node = node->children[bit];
        }
    }

    int findMaxXOR(int num) {
        int xorResult = 0;
        TrieNode* node = root;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            int complement = 1 - bit;

            if (node->children[complement]) {
                xorResult |= (1 << i);
                node = node->children[complement];
            } else {
                node = node->children[bit];
            }
        }
        return xorResult;
    }

private:
    TrieNode* root;
};

class Solution {
public:
    int findMaximumXOR(std::vector<int>& nums) {
        Trie trie;
        int max_xor = 0;
        for (int num : nums) {
            trie.insert(num);
            max_xor = max(max_xor, trie.findMaxXOR(num));
        }
        return max_xor;
    }
};