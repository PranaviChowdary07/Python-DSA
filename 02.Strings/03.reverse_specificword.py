def reverse_word_in_sentence(sentence, target_word):
    words = sentence.split()  
    for i, word in enumerate(words):
        if word == target_word:
            words[i] = word[::-1]  # Reverse the target word

    return ' '.join(words)  # Join the modified words back into a string
sentence = "Pranavi learns Python"
target_word = "learns"
output_sentence = reverse_word_in_sentence(sentence, target_word)
print("Output:", output_sentence)

""" Output:

Output: Pranavi snrael Python
 """
