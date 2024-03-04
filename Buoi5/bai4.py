def count_word_frequency(word_list):

    word_frequency = {}
  
    for word in word_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    for word, frequency in word_frequency.items():
        print(f'{word}: {frequency}')

words = ['apple','orange','banana','apple','orange','apple']
count_word_frequency(words)
