from app.ollama_client import health
if not health():raise SystemExit('Ollama unavailable; check OLLAMA_BASE_URL')
print('Ollama reachable')