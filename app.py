from flask import Flask, render_template, request
import resolve, main
app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    """ Render result and send data to result.html """
    url = request.form['url']
    data = main.Main(url).get_data()
    return render_template('result.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
