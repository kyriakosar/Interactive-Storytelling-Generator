# Interactive Story Generator

Welcome to the Interactive Story Generator! This project utilizes OpenAI's GPT-3 to co-create dynamic stories with user inputs. Below is an overview, instructions on how to use the system, and details on how to run it.

## Contents

- [System Overview](#system-overview)
- [How to Use](#how-to-use)
- [How to Run](#how-to-run)
- [Requirements](#requirements)

## System Overview

### app.py

`app.py` serves as the backend of the system, implemented using Flask. It handles API calls to OpenAI's GPT-3 engine for generating both regular and random stories. The core functionalities include story initialization, real-time interaction, and end-story options.

### index.html

The frontend, `index.html`, provides an interactive user interface. It prompts users to input essential story details, introduces characters, and facilitates the real-time interaction loop. The interface is designed for ease of use, incorporating Bootstrap for styling. You have to create a folder named `templates` and put the index.html file in it.

## How to Use

1. **Initialize the Story:**
   - Enter the story title, category, and characters when prompted.
   - Click the "Generate Story" button to kickstart the storytelling journey.

2. **Real-Time Interaction:**
   - After story initialization, the "Continue Story" button appears.
   - Make decisions for the evolving narrative by following the prompts.

3. **End the Story:**
   - Click the "End Story" button when ready to finalize the story.
   - Two end-story options will be provided for selection.

4. **Explore Creativity:**
   - Engage with the system to explore collaborative and creative storytelling.

## How to Run

1. **Install Dependencies:**
   - Ensure you have the required libraries by installing them using the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Flask App:**
   - Execute the following command in your terminal to start the Flask server:
     ```bash
     python app.py
     ```
   - The application will run locally, and you can access it through your web browser at `http://127.0.0.1:5000/`.

Feel free to reach out if you have any questions or feedback. Happy storytelling!
