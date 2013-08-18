import pickle

class KeyColumnValueStore(object):

  def __init__(self, path=None):
    self._data = {}
    self._path = path
    if self._path is not None:
      try:
        self._data = pickle.load( open( self._path, "rb" ) )
        print "Opened data at ", self._path
        print "Data loaded:", self._data
      except:
        #Error opening file, most likely not there
        print "Error opening file, starting with empty kv store"
        pass

  def persist(self):
    if self._path is not None:
      pickle.dump( self._data, open( self._path, "wb" ) )
      print "Saved kv store to ", self._path
      print "Data saved: ", self._data
    else:
      pass

  def set(self, key, col, val):
    """ sets the value at the given key/column """
    if key in self._data:
      self._data[key][col] = val 
    else:
      self._data[key] = {col:val} 
    self.persist()

  def get(self, key, col = None):
    """ return the value at the specified key/column """
    if col is not None:
      if key in self._data and col in self._data[key]:
        return self._data[key][col]
      else:
        return None
    else:
      if key in self._data:
        return sorted( self._data[key].items() )
      else:
        return []

  def get_key(self, key):
    """ returns a sorted list of column/value tuples """
    if key in self._data:
      return sorted( self._data[key].items() )
    else:
      return []

  def get_keys(self):
    """ returns a set containing all of the keys in the store """
    return self._data.keys()

  def delete(self, key, col):
    """ removes a column/value from the given key """
    del self._data[key][col]
    self.persist()

  def delete_key(self, key):
    """ removes all data associated with the given key """
    del self._data[key]
    self.persist()

  def get_slice(self, key, start, stop):
    """ returns a sorted list of column/value tuples where the column
        values are between the start and stop values, inclusive of the
        start and stop values. Start and/or stop can be None values,
        leaving the slice open ended in that direction """

    full_list = sorted( self._data[key].items() )
    start_i = 0
    end_i = len(full_list)
    start_changed = False
    end_changed = False

    if start is None:
      start_changed = True
    if stop is None:
      end_changed = True

    for i, item in enumerate(full_list):
      if start >= item[0] and not start_changed:
        start_i = i
      if stop < item[0] and not end_changed:
        end_i = i
        end_changed = True

    return full_list[start_i:end_i]
