def single_root_words(root_word, *other_words,):
    root_word = root_word.lower()
    same_words = list()
    for i in other_words:
        if root_word in i.lower() or i.lower() in root_word:
            same_words.append(i)
    print(same_words)


single_root_words('rich', 'riChest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement','Able', 'Mable', 'Disable', 'Bagel')
