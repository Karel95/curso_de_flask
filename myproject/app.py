from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
  return render_template('index.html', title='home')

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
  
