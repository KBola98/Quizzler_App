# Quizlerr

Quizlerr_App is a simple quiz application built using Python and the `tkinter` module for the graphical user interface (GUI). The application fetches quiz questions from an online API and allows users to answer them, keeping track of their score.

## Features

- Fetches quiz questions from an online API.
- Displays questions in a GUI.
- Allows users to answer questions with "True" or "False" buttons.
- Updates and displays the user's score.

## Requirements

- Python 3.x
- `tkinter` module (usually included with Python)
- `requests` module

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/KBola98/Quizzler_App.git
    cd Quizzler_App
    ```

2. Install the required Python packages:
    ```sh
    pip install requests
    ```

## Usage

1. Run the `main.py` file to start the application:
    ```sh
    python main.py
    ```

2. The GUI will open, displaying the first quiz question. Use the "True" and "False" buttons to answer the questions.

## Project Structure

- `main.py`: The main entry point of the application. It initializes the quiz and the GUI.
- `data.py`: Contains the function to fetch quiz questions from the online API.
- `question_model.py`: Defines the `Question` class.
- `quiz_brain.py`: Contains the `QuizBrain` class, which manages the quiz logic.
- `ui.py`: Contains the `QuizInterface` class, which manages the GUI.

## Code Overview

### `main.py`

This file initializes the quiz and the GUI.

### `data.py`

This file contains the function `get_trivia_data()` to fetch quiz questions from the online API.

### `question_model.py`

This file defines the `Question` class, which represents a quiz question.

### `quiz_brain.py`

This file contains the `QuizBrain` class, which manages the quiz logic, including fetching the next question and checking answers.

### `ui.py`

This file contains the `QuizInterface` class, which manages the GUI using `tkinter`.

## Example

Here is an example of how the application works:

1. The user runs `main.py`.
2. The GUI opens and displays the first quiz question.
3. The user clicks the "True" or "False" button to answer the question.
4. The application updates the score and displays the next question.
5. This process repeats until there are no more questions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
