class DatabaseAdapter:
 def query_readonly(self,sql:str,params:tuple=()):raise NotImplementedError('Configure read-only driver and allow-listed queries')