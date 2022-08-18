import psycopg2
import pandas as pd
from calendar import monthrange
from datetime import datetime
from dateutil.relativedelta import relativedelta

conn = psycopg2.connect(
    database="xxx",
    user='xxx',
    password='xxx',
    host='localhost',
    port='5432'
)


def get_data_by_period(date_from, date_to):
    cursor = conn.cursor()
    cursor.execute('''
    select
    	id,
    	"date",
    	status as last_status
    from
    	cyclones c1
    where
    	c1."date" between {0} and {1}
    	and not exists (
    	select
    		1
    	from
    		cyclones c2
    	where
    		c2.id = c1.id
    		and c2."date" = c1."date"
    		and c2."time" > c1."time")
    order by
    	c1.id,
    	c1."date" desc,
    	c1."time" desc'''.format(date_from, date_to))

    result = cursor.fetchall()
    cursor.close()
    return result


def save_data_by_month(year, month):
    date_from = datetime(year, month, 1).strftime('%Y%m%d')
    date_to = datetime(year, month, monthrange(
        year, month)[1]).strftime('%Y%m%d')

    df = pd.DataFrame(get_data_by_period(date_from, date_to))
    if (len(df.index) != 0):
        days = df[1].unique()
        for day in days:
            day_df = df[df[1] == day]
            day_df.to_csv('output/cyclones_' + str(day) + '.csv',
                          index=False, header=False)


def save_all_data(date_from):
    dt = datetime.strptime(date_from, '%Y-%m-%d')
    while (dt <= datetime.today()):
        save_data_by_month(dt.year, dt.month)
        dt += relativedelta(months=1)


save_all_data('2013-01-01')
