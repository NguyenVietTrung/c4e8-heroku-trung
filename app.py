from flask import *
from datetime import *
import mlab
from models.experience import Experience
import os

# connect to mlab database
app = Flask(__name__)

#create a new FoodItem and save it to database
mlab.connect()

app.config['UPLOAD_PATH'] = os.path.join(app.root_path,'uploads')
if not os.path.exists(app.config['UPLOAD_PATH']):
    os.makedirs(app.config['UPLOAD_PATH'])

@app.route('/')
def hello_world():
    return redirect(url_for("deleteinfo"))


current_time = str(datetime.now())
number_of_visitor = 0


@app.route('/login')
def login():
    global number_of_visitor
    number_of_visitor += 1
    current_time = str(datetime.now())
    return render_template("login.html", current_time=current_time, number_of_visitor=number_of_visitor)


@app.route('/dota')
def dota():
    return render_template("dota.html", images=images_on_sever)


@app.route('/contact')
def information():
    return render_template("contact.html")

@app.route('/cssdemo')
def cssdemo():
    return render_template("cssdemo.html")

@app.route('/w3cssdemo')
def w3cssdemo():
    return render_template("w3cssdemo.html")

@app.route('/Mio_CV')
def Mio_CV():
    return render_template("Mio_CV.html", experience_list=Experience.objects())

@app.route('/addimage', methods=["GET","POST"])
def addImage():
    if request.method == "GET":
        return render_template("addimage.html")
    if request.method == "POST":
        new_info = Experience()
        new_info.from_ = request.form["time"]
        new_info.title = request.form["title"]
        new_info.description = request.form["description"]
        # new_info.image = request.files["image"]
        new_info.save()
        return render_template("addimage.html")

@app.route('/deleteinfo', methods=["GET","POST"])
def deleteinfo():
    if request.method == "GET":
        return render_template("deleteinfo.html")
    if request.method == "POST":
        new_info = Experience.objects(title=request.form["title"]).first()
        if new_info is not None:
            new_info.delete()
        return render_template("deleteinfo.html")

if __name__ == '__main__':
    app.run()
