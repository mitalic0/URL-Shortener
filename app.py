
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    search = request.args.get('search')
    query = URL.query

    if request.method == 'POST':
        original = request.form['original_url']
        custom = request.form['custom_code']

        if custom:
            if URL.query.filter_by(short_code=custom).first():
                flash("Custom alias already taken!", "danger")
                return redirect(url_for('index'))
            short_code = custom
        else:
            short_code = generate_code()
            while URL.query.filter_by(short_code=short_code).first():
                short_code = generate_code()

        new_url = URL(original_url=original, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()
        flash("Short URL created successfully!", "success")
        return redirect(url_for('index'))

    if search:
        query = query.filter(URL.original_url.contains(search))

    urls = query.order_by(URL.created_at.desc()).all()
    return render_template("index.html", urls=urls)

@app.route('/<short_code>')
def redirect_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    url.clicks += 1
    db.session.commit()
    return redirect(url.original_url)

@app.route('/delete/<int:id>')
def delete(id):
    url = URL.query.get_or_404(id)
    db.session.delete(url)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
