from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')


def word_tokenize_func():
    text = "Model-based RL don't need a value function for the policy."
    tokens = word_tokenize(text)
    print(tokens)
