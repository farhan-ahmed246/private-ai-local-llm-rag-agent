from app.security import check_bearer_token
def test_auth(monkeypatch):
 monkeypatch.setenv('APP_BEARER_TOKEN','abc');assert check_bearer_token('Bearer abc')
