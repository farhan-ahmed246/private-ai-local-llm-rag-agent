def chunk_text(text:str,size:int=900,overlap:int=120)->list[str]:
 text=' '.join(text.split())
 if not text:return []
 if size<=overlap or overlap<0:raise ValueError('size must exceed overlap')
 out=[];start=0
 while start<len(text):
  end=min(start+size,len(text));out.append(text[start:end])
  if end==len(text):break
  start=end-overlap
 return out
