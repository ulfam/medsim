from flask import Flask, render_template, request
from knn import search_similar_medicines

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    medicine_name = request.form.get('medicine')
    similar_medicines = search_similar_medicines(medicine_name)
    return render_template('results.html', medicines=similar_medicines)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8096)
