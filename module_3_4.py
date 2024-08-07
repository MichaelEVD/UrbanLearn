def single_root_words(root_word, *other_words):
    same_words = []
    root_word.lower()
    other_words_lower = []
    for i in range(len(other_words)):
        other_words_lower = [s.lower() for s in other_words]
        if root_word in other_words_lower[i]:
            same_words.append(other_words[i])
        elif other_words_lower[i] in root_word.lower():
            same_words.append(other_words[i])
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
