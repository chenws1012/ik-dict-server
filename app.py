import sys

from bloom_filter2 import BloomFilter
from flask import Flask, request
from waitress import serve

from config import prop

app = Flask(__name__)

bloom = BloomFilter(max_elements=1000000, error_rate=0.0001)


@app.post('/dict')
def put_dict():
    body = request.json
    dicts = body.get("dicts")

    with open(prop['file_path'], 'a') as f:
        for word in dicts:
            if word in bloom:
                continue
            f.write(word + '\n')
            bloom.add(word)

    return "Done"


def load_dict():
    print('dict loading...')
    with open(prop['file_path'], 'r') as f:
        line = f.readline()
        while line:
            print(line, end='')
            word = line.replace('\n', '')
            bloom.add(word)
            line = f.readline()


if __name__ == '__main__':
    load_dict()
    serve(app, listen='*:10006')
    # waitress-serve --port=5000 app:app
