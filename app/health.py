from app.ollama_client import health
def status()->dict:return {'ollama_reachable':health()}