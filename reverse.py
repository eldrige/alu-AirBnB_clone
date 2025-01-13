def reverse_words(text):
    mylist = text.split(' ')
    for i in range(len(mylist)):
        if len(mylist[i]) >= 5:
            mylist[i] = mylist[i][::-1]
    return ' '.join(mylist)



print(reverse_words('The quick brown fox jumps over the lazy dog')) # 'The quick brown fox jumps over the lazy dog'
