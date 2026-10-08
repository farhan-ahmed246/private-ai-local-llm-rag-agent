def dispatch(name:str,args:dict,handlers:dict)->dict:
 if name not in handlers:return {'ok':False,'error':'Action not allow-listed'}
 try:return {'ok':True,'result':handlers[name](**args)}
 except Exception:return {'ok':False,'error':'Action failed'}