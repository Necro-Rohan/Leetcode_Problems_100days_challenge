class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        letters_in_sentence = set(sentence)
        
        return alphabet.issubset(letters_in_sentence)