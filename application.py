import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import psycopg2.extras


application = app = Flask(__name__)
app.secret_key = 'KREk9tUwUe5aVHEuq1jema/g1GlzGd1Rw67h+jty'

DB_HOST = "threespacedb.ccw4zwitwgyp.us-east-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "changeme"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    s = "SELECT * FROM Themes"
    cur.execute(s)
    list_themes = cur.fetchall()
    return render_template('index.html', list_themes = list_themes)

@app.route('/add_theme', methods=['POST'])
def add_theme():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        thumbnailURL = request.form['thumbnailURL']
        sourceURL = request.form['sourceURL']
        category = request.form['category']
        cur.execute("INSERT INTO Themes (name, thumbnailURL, sourceURL, category) VALUES (%s,%s,%s,%s)", (name, thumbnailURL, sourceURL, category))
        conn.commit()
        flash('Theme Added Successfully')
        return redirect(url_for('index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_theme(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM Themes WHERE id = %s', (id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', theme = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_theme(id):
    if request.method == 'POST':
        name = request.form['name']
        thumbnailurl = request.form['thumbnailurl']
        sourceurl = request.form['sourceurl']
        category = request.form['category']
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
        UPDATE Themes
        SET name = %s,
            thumbnailurl = %s,
            sourceurl = %s,
            category = %s
        WHERE id = %s
        """, (name, thumbnailurl, sourceurl, category, id))
        flash('Theme Updated Successfully')
        conn.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id>', methods = ['POST', 'GET'])
def delete_theme(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM Themes WHERE id = {0}'.format(id))
    conn.commit()
    flash('Theme Removed Successfully')
    return redirect(url_for('index'))


@app.route('/allthemes')
def all_themes():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    s = "SELECT * FROM Themes"
    cur.execute(s)
    list_themes = cur.fetchall()

    return jsonify(list_themes)

        
        
@app.route('/themes/<int:count>/<int:start>')
def themes(count, start):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM Themes LIMIT %s OFFSET %s"
    cur.execute(s, (count, start - 1))
    list_themes = cur.fetchall()

    if not list_themes:
        return jsonify([])
    else:
        return jsonify(list_themes)


