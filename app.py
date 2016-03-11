from flask import Flask
from flask import render_template
app = Flask(__name__)

#decorator connects one function with another function
@app.route("/")
def index():
    template = "index.html"
    return render_template(template)
#def is short for definition
# we are calling a function called index

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)