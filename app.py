import sqlite3

from flask import Flask, jsonify

import queries



app = Flask(__name__)

DATABASE_PATH = 'animal.db'


def serialize_row(row: sqlite3.Row):
    return {key: row[key] for key in row.keys()}


@app.route('/<animal_id>')
def get_animal_by_id(animal_id):

    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()

    cursor.execute(queries.GET_ANIMAL_BY_ID_SHORT_QUERY, (animal_id, ))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))


@app.route('/<animal_id>/full')
def get_animal_by_id_full(animal_id):
    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()

    cursor.execute(queries.GET_ANIMAL_BY_ID_FULL_QUERY, (animal_id, ))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))




if __name__ == '__main__':
    connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    app.config['db'] = connection
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        connection.close()