def translate(di,list_words):
    swedish_words = []
    for word in list_words:
        if word in di:
            swedish_words.append(di[word])
        else:
            swedish_words.append(word)
    return swedish_words
    

b_dict = {'Merry':'god',
          'Christmas':'jul',
          'And':'orch',
          'Happy':'gott',
          'New':'nytt',
          'Year':'ar'
          }
words = ["Merry","Christmas"]
print(" ".join(translate(b_dict,words)))