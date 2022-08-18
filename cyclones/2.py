from datetime import datetime, timedelta
from os import listdir
from os.path import isfile, join

import pandas as pd
import psycopg2

conn = psycopg2.connect(
    database="xxx",
    user='xxx',
    password='xxx',
    host='localhost',
    port='5432'
)


def clear_data_by_date(conn, date):
    prev_date = (date - timedelta(days=1)).strftime('%Y%m%d')
    cur_date = date.strftime('%Y%m%d')

    cursor = conn.cursor()

    try:
        cursor.execute('''
        delete from
        	cyclones_history ch
        where
        	ch.date_from = {0}
            and ch.date_to = {0}
        '''.format(cur_date))
        conn.commit()

        cursor.execute('''
        update
        	cyclones_history ch
        set ch.date_to = {0}
        where
            ch.date_to = {1}
        '''.format(prev_date, cur_date))
        conn.commit()

    except (Exception, psycopg2.DatabaseError):
        conn.rollback()
        cursor.close()
    cursor.close()


def insert_data_by_date(conn, date):

    prev_date = (date - timedelta(days=1)).strftime('%Y%m%d')
    cur_date = date.strftime('%Y%m%d')

    try:
        df = pd.read_csv('output/cyclones_' + cur_date +
                         '.csv', sep=',', header=None)
    except FileNotFoundError:
        return

    cursor = conn.cursor()

    for item in df.itertuples():
        try:
            cyclone_id = item[1]
            cyclone_status = item[3]

            cursor.execute('''
            insert into cyclones_history
            (date_from, date_to, id, status)
            select {3}, {3}, '{0}', '{1}'
            where
            	not exists (
                    select 1
                    from
                        cyclones_history ch_1
                    where
                        ch_1.id = '{0}'
                        and ch_1.status = '{1}'
                        and ch_1.date_to = {2})
            '''.format(cyclone_id, cyclone_status, prev_date, cur_date))
            conn.commit()
            cursor.execute('''
            update
            	cyclones_history
            set date_to = {3}
            where
                id = '{0}'
                and status = '{1}'
                and date_to = {2}
            '''.format(cyclone_id, cyclone_status, prev_date, cur_date))
            conn.commit()

        except (Exception, psycopg2.DatabaseError):
            conn.rollback()
            cursor.close()

    cursor.close()


def process_data():
    path = 'output/'
    input_files = [f for f in listdir(path) if isfile(join(path, f))]
    input_files.sort()
    for file in input_files:
        dt = datetime.strptime(file[9:17], '%Y%m%d')
        clear_data_by_date(conn, dt)
        insert_data_by_date(conn, dt)


process_data()
