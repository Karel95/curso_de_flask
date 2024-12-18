from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder='templates')

# Required
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "db_crud_flask"

# # Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}

mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def home():
    return render_template('index.html', title='home')


@app.route('/clients')
def clients():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM clients""")
    clients = cur.fetchall()
    
    return render_template('modules/clients/index.html', title='clients', clients=clients)

@app.route('/about')
def about():
    # user data
    user = {'name': 'Karel', 'lastname': 'Hernandez', 'email': 'karel@te.st'}
    # product data
    products = ['Pardon us', 'Help us', 'Protect us']
    return render_template('about.html', title='about_us', user=user, products=products)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # save data to database or file

        if name and email and password:
            return 'Data saved successfully'
        else:
            return 'Please fill all fields'

    return render_template('contact.html', title='contact_us')


if __name__ == '__main__':
    app.run(debug=True)
