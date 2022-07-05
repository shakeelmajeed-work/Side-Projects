"""
ID: shakeel5
LANG: PYTHON3
TASK: block game
"""
fin = open ('blocks.in', 'r')
fout = open ('blocks.out', 'w')

words = [] #list of words to play with
alpha = list('abcdefghijklmnopqrstuvwxyz')
blocks = [0]*26

def blocks_needed(word):
    curr_counts = [0]*26
    
    for letter in word:
        index = alpha.index(letter)
        curr_counts[index]+=1
    return curr_counts

num_words = int(fin.readline())

for i in range(num_words):
    card_word1, card_word2 = map(str, fin.readline().split())
    blocks_word1 = blocks_needed(card_word1)
    blocks_word2 = blocks_needed(card_word2)

    for j in range(26):
        max_value_for_curr_letter =  max(blocks_word1[j],blocks_word2[j])
        blocks[j] += max_value_for_curr_letter

for letter in blocks:
    fout.write(str(letter)+'\n')
fout.close()
