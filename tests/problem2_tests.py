from kcvstore import KeyColumnValueStore

store = KeyColumnValueStore()

# ---- PROBLEM 2 Tests ----

def test_slicing():
  store.set('a', 'aa', 'x')
  store.set('a', 'ab', 'x')
  store.set('a', 'ac', 'x')
  store.set('a', 'ad', 'x')
  store.set('a', 'ae', 'x')
  store.set('a', 'af', 'x')
  store.set('a', 'ag', 'x')

  # the following statements will evaluate to True
  print store.get_slice('a', 'ac', 'ae') == [('ac', 'x'), ('ad', 'x'), ('ae', 'x')]
  print store.get_slice('a', 'ae', None) == [('ae', 'x'), ('af', 'x'), ('ag', 'x')]
  print store.get_slice('a', None, 'ac') == [('aa', 'x'), ('ab', 'x'), ('ac', 'x')]
