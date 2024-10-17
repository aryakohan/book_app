import flask
from book_app import Book
from model import PrimaryKeyError
app = flask.Flask(__name__)

@app.route("/")
def index():
  return flask.render_template("index.html")

@app.route("/about")
def about():
  return flask.render_template("about.html")

@app.route("/bookslist")
def bookslist():
  all= Book.allbooks()
  return flask.render_template("bookslist.html",allbooks=all)
@app.route("/update")
def update():
   return flask.render_template("update.html")

@app.route("/newbook",methods = ["POST","GET"])
def newbook():
  if flask.request.method == "POST":
    book_data= dict(flask.request.form)
    try:
      book1 = Book(int(book_data["isbn"]),book_data["title"],book_data["author"],int(book_data["year"]),float(book_data["price"]),int(book_data["pages"]),book_data["genre"])
    except(ValueError):
      return flask.render_template("error.html",error="ISBN must be a 8 digit number")
    except(PrimaryKeyError):
      return flask.render_template("error.html",mistake="ISBN must be a unique number")
    return flask.redirect("/")
  return flask.render_template("newbook.html")

@app.route('/update_book', methods=['GET', 'POST'])
def update_book_route():
    if flask.request.method == 'POST':
        isbn1 = flask.request.form['isbn1']
        isbn2 = flask.request.form['isbn2']
        Book.update_book(isbn1, isbn2)
        return flask.redirect("/")
    return flask.render_template('update_book.html')

@app.route('/update_book1', methods=['GET', 'POST'])
def update_book_route1():
    if flask.request.method == 'POST':
        price = flask.request.form['price']
        isbn = flask.request.form['isbn']
        Book.update_book1(price, isbn)
        return flask.redirect("/")
    return flask.render_template('update_book1.html')

@app.route("/delete_book", methods=["GET","POST"])
def deletebook():
    if flask.request.method == "POST" :
        isbn = dict(flask.request.form)
        Book.delete_book(isbn["isbn"])
        return flask.redirect("/bookslist")        
    return flask.render_template("delete_book.html")
app.run(debug=True)
