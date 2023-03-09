from flask import Flask, jsonify
import random
app = Flask(__name__)

# assume `tracked_accounts` is a list of Twitter handles

# list of tracked Twitter handles
tracked_accounts = ['elonmusk', 'BarackObama', 'KimKardashian']

# dictionary mapping Twitter handles to conversation threads
conversation_threads = {
    'elonmusk': {
        'thread1': ['Great news!', 'Thanks for sharing!', 'Can you give more details?'],
        'thread2': ['What do you think of this?', 'I completely agree!', 'Let me know how I can help.']
    },
    'BarackObama': {
        'thread1': ['Congratulations!', 'You are amazing!', 'Keep up the good work!'],
        'thread2': ['I support your cause!', 'This is an important issue!', 'Let me know if I can be of assistance.']
    },
    'KimKardashian': {
        'thread1': ['Wow, that looks amazing!', 'Thanks for sharing!', 'Can you tell me more about it?'],
        'thread2': ['You are an inspiration!', 'I love your style!', 'Let me know if you need anything.']
    }
}

# dictionary mapping Twitter handles to audience information
audience_info = {
    'elonmusk': {
        'followers': random.randint(1000000, 10000000),
        'average_engagement_rate': random.uniform(0.01, 0.1),
        'age_distribution': {
            'under_18': random.randint(10, 20),
            '18-24': random.randint(20, 30),
            '25-34': random.randint(30, 40),
            '35-44': random.randint(10, 20),
            '45-54': random.randint(5, 15),
            '55+': random.randint(5, 15)
        }
    },
    'BarackObama': {
        'followers': random.randint(10000000, 100000000),
        'average_engagement_rate': random.uniform(0.05, 0.2),
        'age_distribution': {
            'under_18': random.randint(5, 15),
            '18-24': random.randint(10, 20),
            '25-34': random.randint(20, 30),
            '35-44': random.randint(20, 30),
            '45-54': random.randint(10, 20),
            '55+': random.randint(5, 15)
        }
    },
    'KimKardashian': {
        'followers': random.randint(100000000, 200000000),
        'average_engagement_rate': random.uniform(0.1, 0.5),
        'age_distribution': {
            'under_18': random.randint(20, 30),
            '18-24': random.randint(30, 40),
            '25-34': random.randint(20, 30),
            '35-44': random.randint(10, 20),
            '45-54': random.randint(5, 15),
            '55+': random.randint(0, 5)
        }
    }
}

# dictionary mapping Twitter handles to sentiment information
sentiment_info = {
    'elonmusk': {
        'positive_sentiment': random.uniform(0.6, 0.9),
        'negative_sentiment': random.uniform(0.1, 0.3),
        'neutral_sentiment': random.uniform(0.0, 0.2)
    },
    'BarackObama': {
        'positive_sentiment': random.uniform(0.6, 0.9),
        'negative_sentiment': random.uniform(0.1, 0.3),
        'neutral_sentiment': random.uniform(0.0, 0.2)
    }, 
          'KimKardashian': {
        'positive_sentiment': random.uniform(0.6, 0.9),
        'negative_sentiment': random.uniform(0.1, 0.3),
        'neutral_sentiment': random.uniform(0.0, 0.2)
    },}
# endpoint to return a json list of all tracked accounts
@app.route('/accounts')
def get_accounts():
    return jsonify(tracked_accounts)

# endpoint to return a json of the user's conversation threads since start
@app.route('/tweets/<string:handle>')
def get_tweets(handle):
    if handle in conversation_threads:
        return jsonify(conversation_threads[handle])
    else:
        return jsonify({'error': 'Twitter handle not found.'})

# endpoint to return a json of information about the audience for a user's account
@app.route('/audience/<string:handle>')
def get_audience(handle):
    if handle in audience_info:
        return jsonify(audience_info[handle])
    else:
        return jsonify({'error': 'Twitter handle not found.'})

# endpoint to return a json about the sentiment information of an account
@app.route('/sentiment/<string:handle>')
def get_sentiment(handle):
    if handle in sentiment_info:
        return jsonify(sentiment_info[handle])
    else:
        return jsonify({'error': 'Twitter handle not found.'})

if __name__ == '__main__':
    app.run(debug=True)