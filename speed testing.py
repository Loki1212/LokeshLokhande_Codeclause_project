import time
import random

# Set the time limit for the test (in seconds)
time_limit = 10

# Define the words to be used in the test
words = ['python', 'programming', 'code', 'algorithm', 'variable', 'function', 'loop', 'list', 'dictionary', 'tuple']

# Print instructions for the user
print('Type as many words as you can in {} seconds.\n'.format(time_limit))

# Wait for the user to start the test
input('Press enter to start the test.')

# Record the start time
start_time = time.time()

# Initialize variables for tracking the user's progress
num_correct = 0
num_incorrect = 0
num_missed = 0

# Loop until the time limit is reached
while (time.time() - start_time) < time_limit:
    # Choose a random word from the list
    word = words[random.randint(0, len(words) - 1)]

    # Print the word and wait for the user to type it
    print(word)
    user_input = input()

    # Check the user's input against the word
    if user_input == word:
        num_correct += 1
    elif user_input == '':
        num_missed += 1
    else:
        num_incorrect += 1

# Calculate the user's typing speed
total_words_typed = num_correct + num_incorrect
typing_speed = total_words_typed / (time.time() - start_time) * 10

# Print the user's results
print('\nResults:')
print('Time taken: {} seconds'.format(int(time.time() - start_time)))
print('Words typed correctly: {}'.format(num_correct))
print('Words typed incorrectly: {}'.format(num_incorrect))
print('Words missed: {}'.format(num_missed))
print('Typing speed: {:.2f} words per minute'.format(typing_speed))
