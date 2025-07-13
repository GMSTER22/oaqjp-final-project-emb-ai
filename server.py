"""Server modules and the emotion detector module"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/")
def render_index_page():
    """handles requests to the main route by rendering the index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_handler():
    """handles the emotionDetector route by returning a list of emotions dictionary"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalide text! Please try again!.'

    return (
        f"For the given statement, the system response is "
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} "
        f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
