from flask import Flask, redirect, url_for, request, render_template, send_file
from flask_mysqldb import MySQL
import MySQLdb.cursors

# import os
# from datetime import datetime
# from base64 import b64encode
# import base64
# from io import BytesIO #Converts data from Database into bytes

app = Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'NwunyeEdu20$'
app.config['MYSQL_DB']= 'my_flaskbase'
mysql= MySQL(app)

with app.app_context():

    cursor = mysql.connection.cursor()

@app.route('/', methods=['GET','POST'])
def post_get():
    if request.method == "GET":
       return render_template("blog_home.html")
    
@app.route('/form', methods=['GET','POST'])
def form_details():
    if request.method== "GET":
         return render_template("blog_form.html")

    if request.method == "POST":
        a_name= request.form['author_name']
        b_title = request.form['blog_title']
        s_btitle = request.form['blog_stitle']
        d_bblog = request.form['blog_details']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO blog_details VALUES ('{0}', '{1}', '{2}', '{3}');".format (a_name, b_title, s_btitle, d_bblog ))
        #mysql.connection.add(newFile)
        mysql.connection.commit()

        return render_template("blog_display.html", author_name= a_name, blog_title= b_title, blog_stitle=s_btitle,blog_details= d_bblog)

    
@app.route('/blog_info', methods=['GET','POST'])
def b_info():
    if request.method == "GET":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM blog_details")
        allblog = cursor.fetchall()
        print(allblog)
        return render_template("read_blog.html", d_allblog = allblog)

@app.route('/blog_auth/<a_name>', methods=['GET','POST'])
def a_details(a_name):
    if request.method == "GET":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM blog_details WHERE author_name = '{}';".format(a_name))
        allblog = cursor.fetchall()
        print(allblog)
        return render_template("author_name.html", d_allblog = allblog )





if __name__ == '__main__':
    print("my world")
    app.run(port=8080, debug=True)