import requests
from app.config import OLLAMA_BASE_URL,OLLAMA_MODEL
def generate(prompt:str)->str:
 r=requests.post(OLLAMA_BASE_URL+'/api/generate',json={'model':OLLAMA_MODEL,'prompt':prompt,'stream':False},timeout=120);r.raise_for_status();return r.json().get('response','')
def health()->bool:
 try:return requests.get(OLLAMA_BASE_URL+'/api/tags',timeout=3).ok
 except requests.RequestException:return False
