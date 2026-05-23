import random

#The text my "AI" will read and learn from
training_text = """
the cat sat on the mat and the dog sat on the rug 
the cat chased the mouse and the dog chased the cat
"""

#Split the text into individual words
words = training_text.split()

#Create a memory dictionary (database)
word_memory = {}

#Teach my AI: Look at every word and see what word comes right after it
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    
    #If it had't seen this word before, create a list for it
    if current_word not in word_memory:
        word_memory[current_word] = []
        
    #Save the next word into its memory
    word_memory[current_word].append(next_word)

print("--- AI Memory Check ---")
print("Words that can follow 'the':", word_memory['the'])
print("Words that can follow 'sat':", word_memory['sat'])
print("\n")

#Generate NEW text using the memory
print("--- Generated Text ---")
current = "the" #Starting word
generated_story = [current]

# Generate 10 words
for _ in range(10):
    if current in word_memory:
        # Pick a random word from the list of possibilities
        next_word = random.choice(word_memory[current])
        generated_story.append(next_word)
        current = next_word  # Move to the new word
    else:
        break

# Print the final result
print(" ".join(generated_story))
