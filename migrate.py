import sqlite3
from os.path import join, isfile


DATABASE_PATH = 'animal.db'
SQL_DIR_PATH = 'sql'
INIT_MIGRATION_FILE_PATH = 'init.sql'
DATA_MIGRATION_FILE_PATH = 'migrate.sql'

def get_sql_from_file(file_name):
    content = ''
    if isfile(file_name):
        with open(file_name) as file:
            content = file.read()
        return content


def main():
    """
    Оснавная функция. Выполняет миграцию данных.
    """
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Создаем структуру базы.
    init_sql = get_sql_from_file(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH))
    cursor.executescript(init_sql)

    # Заполняем данными.
    data_sql = get_sql_from_file(join(SQL_DIR_PATH, DATA_MIGRATION_FILE_PATH))
    cursor.executescript(data_sql)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()