from flask import Flask
from flask import render_template, redirect, url_for, request
from database import get_all_cats, get_cat_by_id, create_cat, update_votes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    name = "shelly"
    return render_template("home.html", cats = cats, name = name)

@app.route('/cats/<int:id>')
def vote_cats(id):
	cat = get_cat_by_id(id)
	update_votes(cat)
	return render_template('cat.html', cat = cat)

@app.route('/add_cat', methods = ['GET', 'POST'])
def add_cat():
	if request.method == 'GET':
		return render_template("add_cat.html")
	else:
		name = request.form['name']
		create_cat(name)
		return redirect(url_for("catbook_home"))




if __name__ == '__main__':
   app.run(debug = True)
