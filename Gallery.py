from flask import Flask, render_template, request, url_for, redirect,flash
# import MySQLdb
import mysql.connector
from flask_mysqldb import MySQL

# from _mysql_exceptions import IntegrityError
app = Flask(__name__)
app.secret_key = 'xyzpqrabcd'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shk99",
    database="PROJECT"
)
cur = mydb.cursor(dictionary=True,buffered=True)
#cur = mydb.cursor(buffered=True)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'shk99'
app.config['MYSQL_DB'] = 'Project'
mysql = MySQL(app)



@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods = ['GET','POST'])
def login():
        global id
        if request.method == 'POST':

            details = request.form
            nm = details['uname']
            id = nm
            passwd = details['psw']

            cur.execute("select * from login where id = %s AND passwd=%s", (nm, passwd))
            login_id = cur.fetchone()

            if login_id:
                return redirect(url_for('homepage'))
            else:
                flash('Invalid Username or Password')
                return render_template('login.html')

@app.route('/homepage',methods=['POST', 'GET'])
def homepage():
    cur.execute("select c_name from customer where c_id = %s ", (id,))
    name = cur.fetchone()
    return render_template('homepage.html', cust_name=name)



@app.route('/gal1.html',methods=['POST','GET'])
def gal1():
    return render_template('gal1.html')

@app.route('/gal2.html',methods=['POST','GET'])
def gal2():
    return render_template('gal2.html')

@app.route('/gal3.html',methods=['POST','GET'])
def gal3():
    return render_template('gal3.html')

@app.route('/gal4.html',methods=['POST','GET'])
def gal4():
    return render_template('gal4.html')

@app.route('/gal5.html',methods=['POST','GET'])
def gal5():
    return render_template('gal5.html')



@app.route('/artist.html', methods=['POST', 'GET'])
def artist():
    cur.execute("SELECT * from artist")
    artist_details = cur.fetchall()
    x = len(artist_details)

    return render_template('artist.html', c=artist_details, z=x)


@app.route('/paintings.html', methods=['POST', 'GET'])
def artworks():
    cur.execute("SELECT * from painting")
    paint_details = cur.fetchall()
    cur.execute("SELECT cost from bought_by")
    cost = cur.fetchall()
    x = len(paint_details)

    return render_template('paintings.html', c=paint_details, z=x,d=cost)


@app.route('/customers.html', methods=['POST', 'GET'])
def customers():
    cur.execute("SELECT * from customer")
    cust_details = cur.fetchall()
    x = len(cust_details)

    return render_template('customers.html', c=cust_details, z=x)


@app.route('/sales.html', methods=['POST', 'GET'])
def sales():
    cur.execute("SELECT * from sales")
    sales_ = cur.fetchall()
    x = len(sales_)
    return render_template('sales.html', c=sales_,z=x)



@app.route('/filter', methods = ['GET','POST'])
def filter_():
    return render_template('filter.html')

@app.route('/show_filtered', methods = ['GET','POST'])
def show_filter():
    if request.method == 'POST':
        filt = request.form
        c1 = filt['c1']
        c2 = filt['c2']
        y1 = filt['y1']
        y2 = filt['y2']
        if c1 and c2 and y1 and y2:
            cur.execute("select url,p.title ,name,year,cost from painting p,bought_by b,artist a where p.title=b.title and "
                        "p.a_id=a.a_id and p.year between %s and %s and b.cost between %s and %s order by p.title",(y1,y2,c1,c2))
            details = cur.fetchall()
            x = len(details)
            if details:
                return render_template('show_filtered.html',c=details,z=x)
            else:
                flash('No paintings match the required parameters')
                return render_template('show_filtered.html', c=details, z=x)



        elif c1 and c2:
            cur.execute("select url,p.title ,name,year,cost from painting p,bought_by b,artist a where p.title=b.title and "
                        "p.a_id=a.a_id and b.cost between %s and %s order by p.title",(c1,c2))
            details = cur.fetchall()
            x = len(details)
            if details:
                return render_template('show_filtered.html', c=details, z=x)
            else:
                flash('No paintings match the required parameters')
                return render_template('show_filtered.html', c=details, z=x)


        elif y1 and y2:
            cur.execute("select url,p.title ,name,year,cost from painting p,bought_by b,artist a where p.title=b.title and "
                        "p.a_id=a.a_id and p.year between %s and %s order by p.title",(y1,y2))
            details = cur.fetchall()
            x = len(details)
            if details:
                return render_template('show_filtered.html', c=details, z=x)
            else:
                flash('No paintings match the required parameters')
                return render_template('show_filtered.html', c=details, z=x)






@app.route('/e1.html',methods = ['GET','POST'])
def e1():
    eid = 'EX505'
    cur.execute("SELECT url,p1.title,year,type,cost,p1.p_id from painting p1, exhibition e,bought_by b where"
    "p1.e_id=e.e_id AND e.e_id= %s AND p1.p_id=b.p_id",(eid,))
    arts = cur.fetchall()
    x=len(arts)
    return render_template('e1.html',f=arts,z=x)

@app.route('/e2.html',methods = ['GET','POST'])
def e2():
    eid = 'EX510'
    cur.execute("SELECT url,p1.title,year,type,cost,p1.p_id from painting p1, exhibition e,bought_by b where p1.e_id=e.e_id AND e.e_id= %s AND p1.p_id=b.p_id",(eid,))
    arts = cur.fetchall()
    x = len(arts)
    return render_template('e2.html',f=arts,z=x)

@app.route('/e3.html',methods = ['GET','POST'])
def e3():
    eid = 'EX605'
    cur.execute("SELECT url,p1.title,year,type,cost,p1.p_id from painting p1, exhibition e,bought_by b where p1.e_id=e.e_id AND e.e_id= %s AND p1.p_id=b.p_id",(eid,))
    arts = cur.fetchall()
    x = len(arts)
    return render_template('e3.html',f=arts,z=x)

@app.route('/e4.html',methods = ['GET','POST'])
def e4():
    eid = 'EX705'
    cur.execute("SELECT url,p1.title,year,type,cost,p1.p_id from painting p1, exhibition e,bought_by b where p1.e_id=e.e_id AND e.e_id= %s AND p1.p_id=b.p_id",(eid,))
    arts = cur.fetchall()
    x = len(arts)
    return render_template('e4.html',f=arts,z=x)

@app.route('/e5.html',methods = ['GET','POST'])
def e5():
    eid = 'EX805'
    cur.execute("SELECT url,p1.title,year,type,cost,p1.p_id from painting p1, exhibition e,bought_by b where p1.e_id=e.e_id AND e.e_id= %s AND p1.p_id=b.p_id",(eid,))
    arts = cur.fetchall()
    x = len(arts)
    return render_template('e5.html',f=arts,z=x)

@app.route('/e6.html',methods = ['GET','POST'])
def e6():
    eid = 'EX905'
    cur.execute(
        "SELECT url,p1.title,year,type,cost,p1.p_id from painting p1, exhibition e,bought_by b where p1.e_id=e.e_id AND e.e_id= %s AND p1.p_id=b.p_id",
        (eid,))
    arts = cur.fetchall()
    x = len(arts)
    return render_template('e6.html',f=arts,z=x)


@app.route('/bought',methods = ['POST'])
def bought():
    if request.method == 'POST':
         num = request.form['num']

         cur.execute("SELECT c_id from bought_by b where p_id = %s",(num,))
         cust_id = cur.fetchone()

         if cust_id != (None,):
             return ("This painting has already been sold ")
         else:
            cur.execute("UPDATE bought_by set c_id = %s where p_id = %s ",(id,num))
            mydb.commit()
            return ("Painting has been successfully bought!")



if __name__ == "__main__":
    app.run(debug=True, port=5000)

