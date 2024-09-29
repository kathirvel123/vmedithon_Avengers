from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def main():
    return home()
@app.route('/home')
def home():
    return render_template('mainpage.html')
@app.route('/food')
def food():
    return render_template('food.html')
if __name__=='__main__':
    app.run(debug=True) 