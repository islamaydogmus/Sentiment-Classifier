from WordIndentifier import get_pos,get_neg

#  Opening the main file
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
        
