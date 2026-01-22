# NLP Emotion Detection

## Project Overview

This project provides a web-based application for analyzing emotions in text using Natural Language Processing (NLP). Users can input a text statement, and the application will analyze and return the dominant emotion along with individual scores for various emotions. The primary emotions detected include anger, disgust, fear, joy, and sadness.

## Features

- **Simple User Interface**: An easy-to-use form for submitting text for emotion analysis.
- **Emotion Detection**: Utilizes an external NLP service to detect emotions in the provided text.
- **Error Handling**: Appropriate messages are shown for empty or invalid inputs.
- **Dynamic Results Display**: Results and error messages are displayed without refreshing the page using AJAX.

## Technologies Used

- **Flask**: A micro web framework for Python used to create the backend server.
- **Bootstrap**: A front-end framework for designing responsive web applications.
- **JavaScript**: Used for asynchronous requests to the server to enhance user experience.
- **Pylint**: A static code analysis tool for checking the quality and style of Python code.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Flask
- Requests library
- Pylint

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your_username/nlp-emotion-detection.git
   cd nlp-emotion-detection
   ```

2. Install the required packages:

   ```bash
   pip install Flask requests pylint
   ```

3. Start the Flask server:

   ```bash
   python server.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

### Usage

1. Enter a text statement in the input field.
2. Click on the "Run Sentiment Analysis" button.
3. The application will display the emotion analysis result, including individual emotion scores and the dominant emotion.

### Running Pylint

To check code quality, run Pylint against your Python files:

```bash
pylint server.py
```

### Contributing

Contributions are welcome! If you have suggestions for improvements or would like to contribute in any other way, please create an issue or a pull request.

### License

This project is licensed under the MIT License.

