from flask import Flask, request, render_template
import google.generativeai as genai
import markdown2  # Import markdown2 for Markdown to HTML conversion
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Replace with your actual Gemini API key
api_key = 'YOUR_API_KEY_HERE'

def call_gemini_api(prompt, task):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    try:
        if task == 'generate':
            response = model.generate_content(prompt)
        elif task == 'shayari':
            response = model.generate_content(f"Generate a Shayari for the keyword: {prompt}")
        else:
            return "Invalid task selected."

        # Convert Markdown to HTML if the response is in Markdown
        html_content = markdown2.markdown(response.text)
        print("Response from API:", html_content)  # Debug print
        return html_content
    except Exception as e:
        print("Error:", str(e))  # Debug print
        return "An error occurred."

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_text = request.form['text']
    task = request.form['task']
    
    result = call_gemini_api(user_text, task)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
