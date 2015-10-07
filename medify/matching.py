from .models import *
import re

class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

    def insert(self, word):
        node = self
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()

            node = node.children[character]

        node.word = word


def loadTrie():
    illegalMeds = IllegalMedication.objects.all().values_list("product_name", "manufacturer")
    approvedMeds = ApprovedMedication.objects.all().values_list("product_name", "manufacturer", "active_ingredients")
    approvedDevices = ApprovedDevice.objects.all().values_list("device_name", "product_owner_name", "models_name")

    words = set()
    for l in (illegalMeds, approvedMeds, approvedDevices):
        for row in l:
            for col in row:
                words.update(re.split(r',|!|\?| |\.|\n|\(|\)|\+|/|\"|\'', col.lower()))

    trie = TrieNode()
    for word in words:
        trie.insert(word)

    return trie


def search(word, maxCost, trie):
    currentRow = range(len(word) + 1)

    results = []

    for character in trie.children:
        searchRecursive(trie.children[character], character, word, currentRow, results, maxCost)

    return results


def searchRecursive(node, character, word, previousRow, results, maxCost):
    columns = len(word) + 1
    currentRow = [previousRow[0] + 1]

    for column in range(1, columns):
        insertCost = currentRow[column - 1] + 1
        deleteCost = previousRow[column] + 1

        if word[column - 1] != character:
            replaceCost = previousRow[column - 1] + 1
        else:
            replaceCost = previousRow[column - 1]

        currentRow.append(min(insertCost, deleteCost, replaceCost))

    if currentRow[-1] <= maxCost and node.word is not None:
        results.append((node.word, currentRow[-1]))

    if min(currentRow) <= maxCost:
        for character in node.children:
            searchRecursive(node.children[character], character, word, currentRow, results, maxCost)
