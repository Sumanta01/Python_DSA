# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:40:20 2023

@author: KIIT
"""

import os
from flask import Flask, request, render_template

# Step 1: GitHub API Integration

import requests

def fetch_user_repositories(github_url):
    # Authenticate with GitHub API using your token
    headers = {'Authorization': 'Bearer YOUR_GITHUB_TOKEN'}
    
    # Extract the username from the GitHub URL
    username = github_url.split('/')[-1]
    
    # Send a request to fetch user's repositories
    response = requests.get(f'https://github.com/Sumanta01', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching user repositories")


def generate_prompt(repository):
    # Implement code to generate a prompt for GPT-3
    # The prompt should be customized based on the repository's characteristics
    
    # Example: Create a simple prompt based on the repository's name and description
    repo_name = repository['name']
    repo_description = repository['description']
    
    prompt = f"Evaluate the technical complexity of the repository '{repo_name}' with the description: '{repo_description}'."
    
    return prompt

# Step 2: Preprocessing
def preprocess_repository(repository):
    code_content = repository['content']
    
    # Implement your preprocessing logic here
    # For example, you can tokenize, remove comments, or handle large files
    
    # Placeholder: Replace this with your actual preprocessing logic
    preprocessed_code = code_content
    # Implement code to preprocess each repository
    # Handle large files, Jupyter notebooks, and tokenization
    # This needs to be implemented based on your specific requirements
    return preprocessed_code

# Step 3: GPT-3 Integration - Use OpenAI GPT-3 API

import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def calculate_complexity_score(prompt, code):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=150,  # Adjust token limit as needed
        temperature=0.7,  # Adjust for creativity vs. consistency
        stop=None,  # Add stop words as needed
        n=1,  # Number of completions
        top_p=1.0
    )
    
    # Extract and return GPT-3's response
    return response.choices[0].text

# Step 4: Deployment - Use a web framework like Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    github_url = request.form['github_url']
    repositories = fetch_user_repositories(github_url)
    
    most_complex_repo = None
    max_complexity_score = -1
    
    for repo in repositories:
        preprocessed_code = preprocess_repository(repo)
        prompt = generate_prompt(repo)  # This function is still missing
        complexity_score = calculate_complexity_score(prompt, preprocessed_code)
        
        if complexity_score > max_complexity_score:
            max_complexity_score = complexity_score
            most_complex_repo = repo
    
    return render_template('result.html', repository=most_complex_repo)

if __name__ == '__main__':
    app.run(debug=True)
