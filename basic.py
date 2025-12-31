import requests
import json

# Function to simulate Ollama API call
def get_ollama_response(prompt, model_name="llama3.2"): 
    """
    Simulates a call to an Ollama server.
    Replace this with your actual Ollama API endpoint and logic.
    """
    try:
        url = "http://localhost:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        data = {"model": model_name, "prompt": prompt, "stream": False}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        return result.get('response', 'No response field found.')
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure it's running."
    
    except requests.exceptions.RequestException as e:
        return f"Error during Ollama request: {e}"


prompt = "Write a short tamil melody song"
model_name = "llama3.2"

print(get_ollama_response(prompt=prompt, model_name=model_name))
