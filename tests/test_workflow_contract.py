def test_workflow_json():
 import json
 with open('n8n/private-ai-local-llm-chat.json',encoding='utf8') as f:assert json.load(f)['nodes']
