import json
from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open('static/columnsNames.json', 'r') as f:
        columns = json.load(f)
    del columns['code']
    del columns['name']
    del columns['wishlist']
    del columns['gen']
    return render_template('index.html', columns=columns)


@app.route('/inventory', methods=['POST'])
def upload_file():
    file = request.files['datafile']
    checkboxes = ['code', 'name', 'wishlist', 'gen']
    checkboxes = checkboxes + request.form.getlist('checkboxes')
    with open('static/columnsIndexes.json', 'r') as f1:
        columnsIndexes = json.load(f1)
    with open('static/columnsNames.json', 'r') as f2:
        columnsNames = json.load(f2)
    columns_choosed_indexes = {key: columnsIndexes[key] for key in checkboxes if key in columnsIndexes}
    data = []
    if file:
        csv_file = csv.reader(file.stream.read().decode("UTF8").splitlines())
        next(csv_file, None)
        for row in csv_file:
            filtered_row = [row[i] for i in columns_choosed_indexes.values()]
            filtered_row.append(str(sum_stats(row)))
            data.append(filtered_row)
        columns_choosed_names = [columnsNames[key] for key in checkboxes if key in columnsNames]
        columns_choosed_names.append('Sum of stats')
        return render_template("inventory.html", data=data, columnsNames=columns_choosed_names)


def sum_stats(card):
    with open('static/columnsIndexes.json', 'r') as f1:
        columnsIndexes = json.load(f1)
    statsIndexes = [columnsIndexes['attack'], columnsIndexes['defense'], columnsIndexes['speed'], columnsIndexes['hp']]
    stats_sum = sum([int(card[i]) for i in statsIndexes])
    return stats_sum


if __name__ == '__main__':
    app.run()
