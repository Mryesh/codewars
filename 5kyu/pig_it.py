def pig_it(text):
    text = text.split()
    strs = ''
    sentence = ''
    new_word = []
    for s in text:
        if len(s) > 0:
            word = list(str(s))
            word.append(word[0])
            del word[0]
            if s != '?' and s != '!':
                word.append('ay')
            new = strs.join(word)
            new_word.append(new)
    for c in range(0, len(new_word)):
        sentence = sentence + new_word[c] + ' '
    return sentence.rstrip()
