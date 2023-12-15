from flask import Flask, render_template
app = Flask(__name__)

@app.route('/my_profile')
def my_profile():
    return render_template('my_profile.html')

@app.route('/cakes')
def my_print_credit():
    return render_template('cakes.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
