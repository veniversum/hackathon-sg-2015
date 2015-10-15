from .models import *
import re

class TrieNode:
    def __init__(self):
        self.word = None
        self.modelIds = None 
        self.children = {}

    def insert(self, row, model):
        node = self
        id = row[0]
        fields = row[1:]
        
        for field in fields:
            for word in re.split(r',|!|\?| |\.|\n|\(|\)|\+|/|\"|\'', field.lower()):
                for character in word:
                    if character not in node.children:
                        node.children[character] = TrieNode()

                    node = node.children[character]

                node.word = word
                
                # Save space by creating dicts only when needed
                if not node.modelIds:
                    node.modelIds = {}
                if model not in node.modelIds:
                    node.modelIds[model] = set()
                # Store ids of relevant rows
                node.modelIds[model].add(id)
                
                # Reset node to root for adding new words
                node = self

def loadTrie():
    illegalMeds = IllegalMedication.objects.all().values_list("id", "product_name", "manufacturer")
    approvedMeds = ApprovedMedication.objects.all().values_list("id", "product_name", "manufacturer", "active_ingredients")
    approvedDevices = ApprovedDevice.objects.all().values_list("id", "device_name", "product_owner_name", "models_name")

    trie = TrieNode()

    for row in illegalMeds:
        trie.insert(row, IllegalMedication)
    print("Completed Illegal Medication")

    for row in approvedMeds:
        trie.insert(row, ApprovedMedication)
    print("Completed Approved Medication")

    for row in approvedDevices:
        trie.insert(row, ApprovedDevice)
    print("Completed Approved Devices")

    return trie


def search(word, maxCost, trie):
    currentRow = range(len(word) + 1)

    results = []

    for character in trie.children:
        searchRecursive(trie.children[character], character, word, currentRow, results, maxCost)

    return sorted(results, key=lambda r: r[2])


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
        results.append((node.word, node.modelIds, currentRow[-1]))

    if min(currentRow) <= maxCost:
        for character in node.children:
            searchRecursive(node.children[character], character, word, currentRow, results, maxCost)
