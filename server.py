'''
this is a flask server for watson NLP emotion
'''

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the emotion of the provided text and return the result."""
    text_to_analyze = request.args.get('textToAnalyze', '')
    # Print debug information
    print(f"Received text: '{text_to_analyze}'")  # Log the received text
    # Check for empty input
    if not text_to_analyze.strip():   # Check if there is no text input
        print("Empty input detected. Returning error response.")
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)
    # Handle None response or invalid dominant emotion
    if response is None or response['dominant_emotion'] is None:
        print("No valid emotion detected. Sending error message.")
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Prepare the output format
    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    return output
@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
