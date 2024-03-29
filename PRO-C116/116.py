from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    picture = request.form['picture']
    return render_template('tree.html', name=name, age=age, picture=picture)

if _name_ == '_main_':
    app.run(debug=True)
