import sqlite3 as sql
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row
    return conn


def get_film(film_id):
    conn = get_db_connection()
    film = conn.execute('SELECT * FROM films WHERE id = ?',
                        (film_id,)).fetchone()
    conn.close()
    if film is None:
        abort(404)
    return film


@app.route('/')
def index():
    conn = get_db_connection()
    films = conn.execute('SELECT * FROM films').fetchall()
    conn.close()
    return render_template('index.html', films=films)


@app.route('/<int:film_id>')
def film(film_id):
    film = get_film(film_id)
    return render_template('film.html', film=film)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        yearReleased = request.form['yearReleased']
        rating = request.form['rating']
        duration = request.form['duration']
        genre = request.form['genre']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO films (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)',
                         (title, yearReleased, rating, duration, genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    film = get_film(id)

    if request.method == 'POST':
        yearReleased = request.form['yearReleased']
        rating = request.form['rating']
        duration = request.form['duration']
        genre = request.form['genre']

        conn = get_db_connection()
        conn.execute('UPDATE films SET yearReleased = ?, rating = ?, duration = ?, genre = ?'
                     ' WHERE id = ?',
                     (yearReleased, rating, duration, genre, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit.html', film=film)
# ....


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    film = get_film(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM films WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(film['title']))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
