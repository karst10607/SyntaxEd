import nltk

def main():
    sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    print (tokens)

if __name__ == '__main__':
    main()