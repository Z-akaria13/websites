from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import openai
import json

openai.api_key = "removed"

def home(request):
    return render(request, 'basec.html')



example_interactions = [
    {
        "user": "What is AI?",
        "cerebrum": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines programmed to think and learn like humans. This technology has evolved over the years, resulting in various applications, including natural language processing, computer vision, and autonomous systems."
    },
    {
        "user": "How do neural networks work?",
        "cerebrum": "Neural networks are a type of machine learning model inspired by the human brain's structure. They consist of interconnected nodes or 'neurons' organized in layers. When data is fed into the network, each neuron processes the input, applies a transformation, and passes the result to the next layer. Through a process called backpropagation, the network adjusts its weights to minimize the error between its predictions and actual outputs. Over time, the neural network learns to recognize patterns and make accurate predictions."
    },
    {
        "user": "What is natural language processing?",
        "cerebrum": "Natural Language Processing (NLP) is a subfield of AI and linguistics focused on enabling computers to understand, interpret, and generate human language. NLP encompasses various tasks, such as sentiment analysis, machine translation, and question-answering systems. It uses techniques like tokenization, part-of-speech tagging, and dependency parsing to break down language into smaller components and understand their relationships, allowing computers to process and analyze text more effectively."
    },
]

# Convert the interactions list to an array of strings formatted as "User: <user_input>\nCerebrum: <cerebrum_output>"
formatted_interactions = [f"User: {interaction['user']}\nCerebrum: {interaction['cerebrum']}" for interaction in example_interactions]



@csrf_exempt
@require_POST
def submit_text(request):
    text_input = request.POST.get('text_input', '')
    print(f"Received text: {text_input}")

    # Get prior paragraph contents for context
    prior_paragraphs_json = request.POST.get('prior_paragraphs', '[]')
    prior_paragraphs = json.loads(prior_paragraphs_json)

    # Limit the conversation history to 5000 characters, prioritizing the most recent interactions
    conversation_history = "\n".join(prior_paragraphs)[-5000:]

    # Prepend the formatted_interactions to the conversation_history
    conversation_history = "\n".join(formatted_interactions) + "\n" + conversation_history
    print(conversation_history)

    # Query the OpenAI GPT-3 API
    prompt = f"{conversation_history}\n\nUser: {text_input}\nCerebrum:"
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=300,         # Increase the maximum token limit to allow for longer responses
        n=1,
        temperature=.85,        # Increase the temperature to encourage more creativity and unique outputs
        stop=["\n"]
    )

    # Add query and response to the div
    ai_response = response.choices[0].text.strip()
    print(f"AI response: {ai_response}")

    html = f'Cerebrum: {ai_response}'
    response_data = {'status': 'success', 'html': html}
    return JsonResponse(response_data)