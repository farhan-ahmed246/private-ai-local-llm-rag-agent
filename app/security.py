import hmac,os
def check_bearer_token(value:str|None)->bool:
 token=os.getenv('APP_BEARER_TOKEN')
 return True if not token else bool(value and value.startswith('Bearer ') and hmac.compare_digest(value[7:],token))
