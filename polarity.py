from textblob import TextBlob






# def sentiment_analysis(tweet):

  
#  #Create a function to get the polarity
 
#  #Create two new columns ‘Subjectivity’ & ‘Polarity’
#  tweet["TextBlob_Subjectivity"] =    tweet["tweet"].apply(getSubjectivity)
#  tweet ["TextBlob_Polarity"] = tweet["tweet"].apply(getPolarity)
#  def getAnalysis(score):
#   if score < 0:
#     return "Negative"
#   elif score == 0:
#     return "Neutral"
#   else:
#     return "Positive"



#  tweet ["TextBlob_Analysis"] = tweet  ["TextBlob_Polarity"].apply(getAnalysis)
# return tweet



def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity


def getPolarity(text):
   polar = TextBlob(text).sentiment.polarity
   if(polar> 0):
    return 1
   elif(polar< 0):
    return -1
   else:
    return 0

  
  
text = "my lover i love you "

print(getSubjectivity(text))
