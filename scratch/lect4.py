import flask
import os

app = flask.Flask(__name__)
@app.route('/') # Python decorator
def index():
    #return('reached index method')
    #//return "<h1>Hello world!</h1>"
    return flask.render_template("index.html")
app.run(

    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP','0.0.0.0')

)
