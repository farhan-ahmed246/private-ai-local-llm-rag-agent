from app.chunking import chunk_text
def test_empty():assert chunk_text('')==[]
def test_chunks():assert chunk_text('abcdefghij',6,2)==['abcdef','efghij']
