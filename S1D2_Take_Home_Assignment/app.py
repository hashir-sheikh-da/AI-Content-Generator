from flask import Flask, request, render_template
import google.generativeai as genai
import markdown2  # Import markdown2 for Markdown to HTML conversion
import warnings

# Suppress any warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Replace with your actual Gemini API key
api_key = 'YOUR_API_KEY_HERE'

def call_gemini_api(prompt, task):
    """
    Calls the Gemini API to generate, summarize, or translate content.
    
    Parameters:
    - prompt: The input text for the API.
    - task: The type of task to perform ('generate', 'summarize', 'translate').

    Returns:
    - HTML content generated by the API or an error message.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    try:
        # Call the API based on the selected task
        if task == 'generate':
            response = model.generate_content(prompt)
        elif task == 'summarize':
            response = model.generate_content(f"Summarize this for me: {prompt}")
        elif task == 'translate':
            response = model.generate_content(f"Translate this to English: {prompt}")
        else:
            return "Invalid task selected."

        # Convert Markdown response to HTML
        html_content = markdown2.markdown(response.text)
        print("Response from API:", html_content)  # Debug print
        return html_content
    except Exception as e:
        print("Error:", str(e))  # Debug print
        return "An error occurred."

@app.route('/', methods=['GET'])
def index():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """
    Handles the form submission and displays the generated content.

    Returns:
    - The rendered HTML page with the result.
    """
    user_text = request.form['text']
    task = request.form['task']
    
    result = call_gemini_api(user_text, task)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
