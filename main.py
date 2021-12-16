from flask import Flask,render_template
#adding libries


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_map')
def show_map():
    return render_template('show_map.html')

if __name__ == '__main__':
    app.run(debug=True)