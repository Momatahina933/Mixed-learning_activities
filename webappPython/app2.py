from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello my name is Momatahina Akter Chaiti, my student ID is 4213933, I am studying Bsc in LSBU, I enjoy reading, painting, exploring new cuisines, and traveling'

@app.route('/my_credit')
def my_print_credit():
    return 'My print credit: £  Print Credit'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
