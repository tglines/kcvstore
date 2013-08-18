import flask
from kcvstore import KeyColumnValueStore

store = KeyColumnValueStore('/tmp/restserverstore')
app = flask.Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
request = flask.request


# REST URL Structure
# GET / -> performs store.get_keys() ... this way it's sort of a directory to the kv store
# GET /key -> performs store.get(key)
# GET /key/col -> performs store.get(key,col)
# GET /key/start/stop -> performs store.get_slice(key, start, stop) ... not truly rest but convenient
# POST /key/col/val -> performs store.set(key,col,val)
# DELETE /key -> performs store.delete_key(key)
# DELETE /key/col -> performs store.delete(key,col)
#
# Assuming that I don't need to call get_key because get with just key is same code

@app.route("/")
def get_keys():
  d = {'result': store.get_keys()}
  return flask.jsonify(d)

@app.route('/<key>')
def get_key(key):
  d = {'result': store.get(key)}
  return flask.jsonify(d)

@app.route('/<key>/<col>', methods=['GET','DELETE'])
def action_on_keycol(key,col):
  if request.method == 'GET':
    d = {'result': store.get(key,col)}
    return flask.jsonify(d)
  else:
    print "DELETE KEY COL"
    store.delete(key,col)
    d = {'status':'success', 'result': ''}
    return flask.jsonify(d)

@app.route('/<key>/<start>/<stop>')
def get_slice(key,start,stop):
  d = {'result': store.get_slice(key,start,stop)}
  return flask.jsonify(d)

@app.route('/<key>/<col>/<val>', methods=['POST'])
def set(key,col,val):
  store.set(key,col,val)
  d = {'status':'success', 'result': ''}
  return flask.jsonify(d)

@app.route('/<key_to_delete>', methods=['DELETE'])
def delete_key(key_to_delete):
  store.delete_key(key_to_delete)
  d = {'status':'success', 'result': ''}
  return flask.jsonify(d)

if __name__ == "__main__":
  print "Running KeyColumnValueStore"
  app.debug = True
  app.run()
