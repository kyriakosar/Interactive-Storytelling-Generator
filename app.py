from flask import Flask, render_template, request, jsonify
import openai
import json

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'OpenAI key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_random_story', methods=['POST'])
def generate_random_story():
    # Get user input from the form
    user_input = json.loads(request.json['prompt'])
    generated_story = generate_story_with_gpt3(user_input,end_story = True)
    return jsonify({'generate_random_story': generated_story})

@app.route('/generate_story', methods=['POST'])
def generate_story():
    # Get user input from the form
    user_input = json.loads(request.json['prompt'])

    # Generate the story using OpenAI GPT-3
    generated_story = generate_story_with_gpt3(user_input)

    # Return the generated story as JSON
    return jsonify({'generated_story': generated_story})

def generate_story_with_gpt3(story, end_story = False):
  
    if end_story:
        prompt =  f"Finalise the story: {story['generatedStory']}"
    else:
        # Construct the prompt for GPT-3
        prompt = f"Once upon a time, in a {story['category']} {story['title']}, {', '.join(story['characters'])} embarked on a journey. {' '.join(story['plotPoints'])}"

    # Make an API call to OpenAI GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    generated_story = response.choices[0].text.strip()
    return generated_story


   
    

if __name__ == '__main__':
    app.run(debug=True)