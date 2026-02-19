''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' Main function which will be executed once
        /emotionDetector route is accessed
        as a result it will call emotion_detector function 
        by passing text_to_analyze variable
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)


    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    return (
        f"For the given statement, the system response is 'anger': "
        f"{response['anger']}, 'disgust': {response['disgust']}, 'fear': "
        f"{response['fear']}, 'joy': {response['joy']} and 'sadness': "
        f"{response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}</b>")


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
