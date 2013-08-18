from kcvstore import KeyColumnValueStore

store = KeyColumnValueStore()

# ---- PROBLEM 3 Tests ----

def test_persistance():
  store = KeyColumnValueStore(path='/tmp/codetestdata')
  store.set('a', 'ag', 'x')
