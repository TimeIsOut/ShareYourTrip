from flask import Flask, render_template, redirect


main = Flask(__name__)

@main.route('/home')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    main.run(debug = True)