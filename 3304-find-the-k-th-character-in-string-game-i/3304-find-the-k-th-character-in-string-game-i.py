def generate_word(word, k):
    if len(word) > k:
        return word[k-1]  # Base case: If word is long enough, return the kth character
    
    new_word = ""  # To store transformed characters
    for c in word:
        char_code = ord(c)  # Convert character to ASCII
        next_code = char_code + 1  # Get next character's ASCII code

        # If character is 'z', wrap around to 'a'
        if c == 'z':
            next_code = ord('a')

        next_char = chr(next_code)  # Convert back to character
        new_word += next_char  # Append to new_word

    return generate_word(word + new_word, k)  # Recursively expand the word

class Solution:
    def kthCharacter(self, k: int) -> str:
        return generate_word("a", k) 
        