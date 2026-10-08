from app.retriever import retrieve
def test_match():assert retrieve('office policy',[{'source':'a','text':'office policy'}])[0]['source']=='a'
