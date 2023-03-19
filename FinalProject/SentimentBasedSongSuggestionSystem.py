import nltk.sentiment
import random
import emoji
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()

def main():
        user_text = input('Do you want to say anything ? ')
        score = get_sentiment(user_text)
        reaction = get_reaction(score)
        print("You seems to be "+reaction)
        predict_song(score)

def predict_song(score):
    if score>0.5:
        file=open('VeryHappy.txt')
        l = []
        for line in file:
            l.append(line)
        ans=random.choice(l)
        print("You should try this Song! "+ans)
    elif score>0:
        file=open('Happy.txt')
        la = []
        for line in file:
            la.append(line)
        ans1=random.choice(la)
        print("You should try this Song! "+ans1)
    elif score==0:
        file=open('Neutral.txt')
        lal = []
        for line in file:
            lal.append(line)
        ans2=random.choice(lal)
        print("You should try this Song! "+ans2)
    elif score<0:
        file=open('Sad.txt')
        lala = []
        for line in file:
            lala.append(line)
        ans3=random.choice(lala)
        print("You should try this Song! "+ans3)
    elif score<-0.5:
        file=open('VerySad.txt')
        lu = []
        for line in file:
            lu.append(line)
        ans4=random.choice(lu)
        print("You should try this Song! "+ans4)
def get_reaction(score):
    """
    Parameter score: a float between -1 and +1
    Return: An emoji as a string!
    """
    if score > 0.5:
        return "😍(Very Happy)"
    if score > 0:
        return "🙂(Happy)"
    if score == 0:
        return "😶(Normal)"
    if score < -0.5:
        return "😢(Very Sad)"
    if score < 0:
        return "😟(Sad)"

def get_sentiment(user_text):
    """
    Parameter user_text: any text (string)
    Return: a sentiment score between -1 and +1 (float)
    """
    # 1. pass the text into the analyzer.polarity_scores function, part of the nltk package
    scores = analyzer.polarity_scores(user_text)
    # 2. extract the sentiment score. Scores is a "dictionary" (covered on May 17th)
    sentiment_score = scores['compound']

    return sentiment_score

if __name__ == '__main__':
    main()