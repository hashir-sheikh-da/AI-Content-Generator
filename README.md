# AI Content Generator

This repository contains two assignments completed as part of the Masai School data analytics course. The assignments focus on creating an AI Content Generator using Google's Gemini model. The project demonstrates using APIs to generate text, summarize content, translate text, and create Shayaris (poetic expressions).

## Authors
- [Hashir Sheikh](https://github.com/hashir-sheikh-da)

## Key Objectives:
The primary objective of this project was to gain hands-on experience in building AI-based applications that utilize text generation models. Through these assignments, the following objectives were achieved:

- Understanding API integration in Python and Flask.
- Building web applications with HTML, CSS, and JavaScript.
- Implementing light/dark mode functionality.
- Handling different text processing tasks using an AI model.

## Assignment Deliverables:
#### Tools and Technologies Used
- 🐍 Python: For backend logic and API integration.
- 🌐 Flask: As the web framework.
- 🎨 HTML/CSS: For creating the web interface.
- 💻 JavaScript: For interactive elements and theme toggling.
- 🤖 Google Gemini API: For text generation, summarization, translation, and Shayari creation.
- 🔄 Markdown2: For converting Markdown to HTML.

#### Project Structure
- 📂 In-Class Assignment: Focused on text generation and Shayari creation.
- 📂 Take-Home Assignment: Included generative text, summarization, and translation tasks.

## Table of Contents 
    1. Introduction
    2. Getting Started and Running the Application
    3. In-Class Assignment
    4. Take-Home Assignment
    5. Conclusion

### 1. Introduction
This project comprises two assignments, each designed to leverage the capabilities of Google's Gemini AI for various text-processing tasks. The first assignment was completed in class, focusing on building a basic web app for text and Shayari generation. The second, a take-home assignment, extended the functionality to include text summarization and translation.
    
### 2. Getting Started and Running the Application
#### Prerequisites
- [Python](https://www.python.org/downloads/)
- Open a terminal in VS Code and navigate to your project folder.
- Set Up a Virtual Environment: 
```bash

python -m venv env

```

- Activate the virtual environment:
```bash

Windows: .\env\Scripts\activate
macOS/Linux: source env/bin/activate

```

- requests: 
```bash

pip install requests

```

- Flask: 
```bash

pip install Flask

```

- google-generativeai: 
```bash

pip install -q -U google-generativeai

```

- markdown2
```bash

pip install -q -U markdown2

```


#### Clone the repository:
- Navigate to the assignment folder (In-Class_Assignment or Take-Home_Assignment).
- Run the prerequisites:

```bash

python app.py

```
- Open your web browser and go to http://127.0.0.1:5000/ to use the application.

### 3. In-Class Assignment
#### Overview
The in-class assignment involved creating a web application where users can input text prompts and select a task: either generating general text or creating a Shayari. The application uses the Gemini API to process the input and display the generated content.

#### Features
- ✍️ Text Generation: Generate content based on a given prompt.
- 📜 Shayari Generation: Create poetic expressions (Shayaris) based on a keyword.
- 🌗 Light/Dark Mode: Toggle between light and dark themes for user interface preferences.

#### Code Highlights
- Backend: Flask-based backend to handle user requests and API calls.
- Frontend: HTML/CSS for layout and design, JavaScript for theme toggling.

![Screenshot]([https://github.com/hashir-sheikh-da/Preamble_PyTorch_048/blob/main/Data_PowerBI_Assets/dashboard_world_electricity_analysis.png](https://github.com/hashir-sheikh-da/GENAI-B38/blob/main/S1D2_Assignment_Screenshot/S1D2_In_Class_Assignment.png))

### 4. Take-Home Assignment
#### Overview
The take-home assignment expanded the application to include additional functionalities like summarization and translation. This assignment aimed to create a more versatile tool that could assist with various text-processing tasks.

#### Features
- ✍️ Text Generation: Generate content based on a given prompt.
- 🔍 Text Summarization: Summarize the given text to extract key information.
- 🌐 Text Translation: Translate text to English.

#### Code Highlights
- API Integration: Utilizes the Gemini API for different tasks.
- Enhanced Interface: Added functionality for selecting the type of text processing task.
- Improved User Experience: Seamless transitions and user-friendly interface.

![Screenshot]([https://github.com/hashir-sheikh-da/Preamble_PyTorch_048/blob/main/Data_PowerBI_Assets/dashboard_world_electricity_analysis.png](https://github.com/hashir-sheikh-da/GENAI-B38/blob/main/S1D2_Assignment_Screenshot/S1D2_Take_Home_Assignment.png))

### 5. Conclusion
This project provided an excellent opportunity to learn and implement AI-based text-processing applications. By completing these assignments, I have gained valuable skills in web development, API integration, and using AI models for practical applications. The in-class assignment laid the foundation, while the take-home assignment allowed for deeper exploration and enhancement of the initial concept.

### 📁 Repository Structure
```bash
.
├── In-Class_Assignment
│   ├── app.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   └── styles.css
├── Take-Home_Assignment
│   ├── app.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   └── styles.css
│   │   └── script.js
├── README.md

```
