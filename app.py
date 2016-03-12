import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)

#we use DictReader when there are headers
def get_csv(csv_path) :
    csv_file = open(csv_path, "r")
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj) #to convert csv object into a list
    return csv_list

@app.route("/")
def index():
    template = "index.html"
    object_list = get_csv(csv_path = "./static/la-riots-death.csv")
    return render_template(template, object_list=object_list)
#def is short for definition
# we are calling a function called index

@app.route("/<row_id>/") 
#between two slashes, Flask knows to accept the row_id 
def detail(row_id):
    template = "detail.html"
    object_list = get_csv(csv_path = "./static/la-riots-death.csv")
    for row in object_list:
        if row["id"] == row_id:
            return render_template(template, row=row)
    abort(404)



if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)