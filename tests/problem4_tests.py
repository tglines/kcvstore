from kcvstore import KeyColumnValueStore

import rest_server
app = rest_server.app.test_client()

# ---- PROBLEM 4 Tests ----

def test_set():
  assert app.post('/a/aa/x')

def test_get():
  assert b'"result": "x"' in app.get('/a/aa').data

def test_nonexistant_get():
  assert b'"result": []' in app.get('/b').data

def test_delete():
  assert app.delete('/a/aa')
  assert b'"result": null' in  app.get('/a/aa').data

def test_slice():
  assert app.post('/a/aa/1')
  assert app.post('/a/ab/2')
  assert app.post('/a/ac/3')
  assert app.post('/a/ad/4')
  assert b'{"result": [["aa", "1"], ["ab", "2"], ["ac", "3"]]}' in  app.get('/a/aa/ac').data
  
def test_delete_key():
  assert app.delete('/a')
  assert b'{"result": []}' in app.get('/a').data
