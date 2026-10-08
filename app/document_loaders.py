from pathlib import Path
def extract_text(path:str)->str:
 p=Path(path)
 if p.suffix.lower() in {'.txt','.md','.csv'}:return p.read_text(encoding='utf-8',errors='replace')
 if p.suffix.lower()=='.pdf':
  from pypdf import PdfReader
  return '\n'.join(pg.extract_text() or '' for pg in PdfReader(str(p)).pages)
 raise ValueError('Unsupported type')