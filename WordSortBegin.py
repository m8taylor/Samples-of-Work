def word_count(str):
    import operator

    str = list(str)

    j = len(str)
    for i in range(0, j):
        if str[i] == '-':
            str[i] = ' '
#        if str[i] == '.':
#            str[i] = ''
#        if str[i] == '!':
#            str[i] = ''
#        if str[i] == '?':
#            str[i] = ''


    while j>0:
        if str[j-1] == ' ':
            del str[j-1]
            break
        del str[j-1]
        j -= 1

    str = ''.join(str)
    str = str.lower()


    counts = dict()
    str = str.split()

    for word in str:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
