import logging
logger=logging.getLogger('private_ai.audit')
def audit_event(event:str,actor:str):logger.info('event=%s actor=%s',event,actor)