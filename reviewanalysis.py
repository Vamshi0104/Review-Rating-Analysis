from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def output_scenti(m):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(m)
    res=int(sentiment_dict['compound']*100)
    if(res>60):
        return "5"
    elif(res>=50 and res<60):
        return "4.5"
    elif(res>=45 and res<50):
        return "4"
    elif(res>=40 and res<45):
        return "3.5"
    elif(res>=30 and res<40):
        return "3"
    elif(res>=20 and res<30):
        return "2.5"
    elif(res>=10 and res<20):
        return "2"
    elif(res>=0 and res<10):
        return "1.5"
    elif(res<0):
        return "1"
