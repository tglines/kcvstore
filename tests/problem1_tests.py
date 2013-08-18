from kcvstore import KeyColumnValueStore

store = KeyColumnValueStore()

# ---- PROBLEM 1 Tests ----

def test_set_get():
  store.set('a', 'aa', 'x')
  store.set('a', 'ab', 'x')
  store.set('c', 'cc', 'x')
  store.set('c', 'cd', 'x')
  store.set('d', 'de', 'x')
  store.set('d', 'df', 'x')

  # the statements below will evaluate to True
  assert store.get('a', 'aa') == 'x'
  assert store.get_key('a') == [('aa', 'x'), ('ab', 'x')]

def test_nonexistent():
  # nonexistent keys/columns, the statements below
  # will evaluate to True
  assert store.get('z', 'yy') is None
  assert store.get('z') == []

def test_overwriting():
  # if we set different values on the 'a' key:
  store.set('a', 'aa', 'y')
  store.set('a', 'ab', 'z')

  # the statements below will evaluate to True
  assert store.get('a', 'aa') == 'y'
  assert store.get_key('a') == [('aa', 'y'), ('ab', 'z')]

def test_deleting():
  # deleting
  store.delete('d', 'df')

  # this will evaluate to True
  assert store.get_key('d') == [('de', 'x')]

  # delete an entire key
  store.delete_key('c')

  # this will evaluate to True
  assert store.get_key('c') == []
