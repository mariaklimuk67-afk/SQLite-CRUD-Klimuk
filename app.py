from flask import Flask, render_template, request, redirect, url_for
import database_connector as db

app = Flask(__name__)

@app.route('/')
def index():
    books = db.get_all_items()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        db.insert_item(title, author, year, genre)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = db.get_item_by_id(id)
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        db.update_item(id, title, author, year, genre)
        return redirect(url_for('index'))
    return render_template('edit.html', book=book)

@app.route('/delete/<int:id>')
def delete(id):
    db.delete_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_db_table()
    app.run(debug=True)