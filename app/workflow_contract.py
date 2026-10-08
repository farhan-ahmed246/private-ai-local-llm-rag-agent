from pydantic import BaseModel,Field
class AgentAction(BaseModel):
 action:str
 arguments:dict=Field(default_factory=dict)
 requires_human_approval:bool=True
 rationale:str=Field(max_length=1000)