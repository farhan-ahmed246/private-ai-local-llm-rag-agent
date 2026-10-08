from pathlib import Path
from app.chunking import chunk_text
def load_chunks(root:str)->list[dict]:
 out=[];base=Path(root)
 if not base.exists():return out
 for p in base.rglob('*'):
  if p.is_file() and p.suffix.lower() in {'.txt','.md'}:
   out += [{'source':p.name,'text':c} for c in chunk_text(p.read_text(encoding='utf-8',errors='replace'))]
 return out
def retrieve(q:str,chunks:list[dict],limit:int=4)->list[dict]:
 terms={x.lower().strip('.,?!') for x in q.split() if len(x)>2}
 rank=[(len(terms&set(c['text'].lower().split())),c) for c in chunks]
 return [c for score,c in sorted(rank,key=lambda x:x[0],reverse=True) if score][:limit]
