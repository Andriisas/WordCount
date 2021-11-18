def word_count():
    vocabulary = []
    result_list = []
    print("Welcome to the Word Count\nPlease provide all words you want to see in vocabulary(passing by 1 word) \n"
          "Use 'STOP' keyword to finish writing")
    while True:
        vocabulary.append(input('Enter the word here: '))
        if vocabulary[-1] == 'STOP':
            vocabulary.pop()
            break

        if vocabulary[-1].isdigit():
            vocabulary.pop()
            print('Can not input numbers, try again')
            continue

        if len(vocabulary[-1].split()) > 1:
            vocabulary.pop()
            print('Please, provide one word in a time')
            continue

        if len(vocabulary[-1]) == 0:
            vocabulary.pop()
            print('Please, provide a word ')
            continue

        if vocabulary[-1].isspace():
            vocabulary.pop()
            print('Please, provide a word, not a space ')
            continue

        if not vocabulary[-1].isalnum():
            vocabulary.pop()
            print('Please, do not use any special characters or extra spaces ')
            continue

        if len(vocabulary) == 0:
            print()
            continue

    letter_to_search = input('Write down letters you looking for : ')
    for word in vocabulary:
        if letter_to_search in word:
            result_list.append(word)

    print('Here is list of asked letters and matching words ordered by length :')
    print(f'Letters : {letter_to_search}')
    print(f'Number of occasions in vocabulary : {len(result_list)}')
    print(f'Matching words : {result_list}')
