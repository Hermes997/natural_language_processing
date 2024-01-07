from nltk.stem import PorterStemmer, LancasterStemmer


def stemmer_lemmatizer_func():
    stem1 = PorterStemmer()
    stem2 = LancasterStemmer()
    words = ["eat", "ate", "eaten", "eating"]
    print("Porter Stemmer   :", [stem1.stem(w) for w in words])
    print("Lancaster Stemmer:", [stem2.stem(w) for w in words])
