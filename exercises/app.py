from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

add_student("hh",9,True)
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/student/<int:student_id>')
def display_student(student_id):
    stud=query_by_id(student_id)
    return render_template("student.html",student_id=student_id)

app.run(debug=True)
