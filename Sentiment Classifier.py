# Stripping values
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for punc in punctuation_chars:
        if punc in word:
            word = word.replace(punc, "")
    return word

# Positive
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(sentence):
    sentence = sentence.lower()
    list_words_uncleaned = sentence.split()
    list_words_cleaned = []
    for word in list_words_uncleaned:
        list_words_cleaned.append(strip_punctuation(word))
    count = 0
    for pword in positive_words:
        if pword in list_words_cleaned:
            count += 1
    return count

# Negative
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):
    sentence = sentence.lower()
    list_words_uncleaned = sentence.split()
    list_words_cleaned = []
    for word in list_words_uncleaned:
        list_words_cleaned.append(strip_punctuation(word))
    count = 0
    for nword in negative_words:
        if nword in list_words_cleaned:
            count += 1
    return count

# Opening the main file
with open("twitter_data.csv", "r") as twitter_f:
    lines = twitter_f.readlines()
    mainGuy = []
    for line in lines:
        line = line.strip()
        mainGuy.append(line.split(","))
    mainGuy.pop(0)
    
    print(mainGuy)
    with open("resulting_data.csv", "w") as resulting_txt:
        resulting_txt.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
        for tweet_text, retweet_count, reply_count in mainGuy:
            pos = get_pos(tweet_text)
            neg = get_neg(tweet_text)
            net = pos - neg
            resulting_txt.write("{},{},{},{},{}\n".format(retweet_count,reply_count,pos,neg,net))
        