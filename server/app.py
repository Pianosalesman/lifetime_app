import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

DATA = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


@app.route("/")
def index():
    @app.route('/get_data', methods=['GET'])
    def all_data():
        return jsonify({
            'status': 'success',
            'data': DATA
        })


if __name__ == '__main__':
    app.run()
