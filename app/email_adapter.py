class EmailAdapter:
 def draft_reply(self,message_id:str,body:str)->dict:return {'message_id':message_id,'draft':body,'sent':False}
 def list_messages(self,**kwargs):raise NotImplementedError('Configure approved OAuth provider')