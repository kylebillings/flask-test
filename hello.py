import flask
app = flask.Flask(__name__)


@app.route('/<name>')
def main(name):
  return flask.render_template('main.html', name=name.title())


@app.route('/', methods=['POST', 'GET'])
def index():
  if flask.request.method == 'POST':
    return flask.redirect(flask.url_for("main", name=flask.request.form["name"]))
  return flask.render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
