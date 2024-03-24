from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', page_title="HOME")


@app.route('/all_pizzas')
def all_pizzas():
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pizza;")
    results = cur.fetchall()
    return render_template("all_pizzas.html", page_title="ALL PIZZAS", results=results)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
