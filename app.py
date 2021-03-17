import requests
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/query', methods=['GET'])
def main():
    username = request.args.get('username')
    if not username:
        return "request querystring, for example ?username=chronosa"
    url = f'https://api.github.com/users/{username}/gists'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    if response.status_code is not 200:
        # TODO-SJ
        return "ERROR Occurred"

    query_results = response.json()
    urls = []
    for gist_meta in query_results:
        urls.append(gist_meta.get("url"))

    return str(urls)
