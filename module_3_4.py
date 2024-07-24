def single_root_words(root_word, *other_words,):
    same_words = list()
    for i in other_words:
        other_words = i.lower()
        same_words.append(other_words)
        for j in same_words:
            if root_word not in j:
                same_words.remove(j)
    print(same_words)

single_root_words('rich', 'riChest', 'orichalcum', 'cheers', 'richies')