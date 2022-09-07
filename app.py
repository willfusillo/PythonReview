from flask import Flask, jsonify
import AWS_connector

app = Flask(__name__)

@app.route('/')
def index():
    return "This is a test enviroment for checking on the pulling of data :) "

@app.route('/get-items')
def get_items():
    return jsonify(AWS_connector.describe_table)


if __name__ == '__main__':
    app.run()