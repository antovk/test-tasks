
with trips as (
    SELECT 1 as id, 1 as client_id, 10 as driver_id, 1 as city_id, 'completed' as 'status', str_to_date('2013-10-01', '%Y-%m-%d') as request_at UNION ALL
    SELECT 2,       2,              11,              1,            'cancelled_by_driver',   str_to_date('2013-10-01', '%Y-%m-%d')               UNION ALL
    SELECT 3,       3,              12,              6,            'completed',             str_to_date('2013-10-01', '%Y-%m-%d')               UNION ALL
    SELECT 4,       4,              13,              6,            'cancelled_by_client',   str_to_date('2013-10-01', '%Y-%m-%d')               UNION ALL
    SELECT 5,       1,              10,              1,            'completed',             str_to_date('2013-10-02', '%Y-%m-%d')               UNION ALL
    SELECT 6,       2,              11,              6,            'completed',             str_to_date('2013-10-02', '%Y-%m-%d')               UNION ALL
    SELECT 7,       3,              12,              6,            'completed',             str_to_date('2013-10-02', '%Y-%m-%d')               UNION ALL
    SELECT 8,       2,              12,              12,           'completed',             str_to_date('2013-10-03', '%Y-%m-%d')               UNION ALL
    SELECT 9,       3,              10,              12,           'completed',             str_to_date('2013-10-03', '%Y-%m-%d')               UNION ALL
    SELECT 10,      4,              13,              12,           'cancelled_by_driver',   str_to_date('2013-10-03', '%Y-%m-%d')
),
users as (
    SELECT 1 as users_id, 'No' as banned, 'client' as 'role' UNION ALL
    SELECT 2,             'Yes',          'client'           UNION ALL
    SELECT 3,             'No',           'client'           UNION ALL
    SELECT 4,             'No',           'client'           UNION ALL
    SELECT 10,            'No',           'driver'           UNION ALL
    SELECT 11,            'No',           'driver'           UNION ALL
    SELECT 12,            'No',           'driver'           UNION ALL
    SELECT 13,            'No',           'driver'
)

SELECT t1.day
     , round(canceled / total, 2) as 'Cancellation rate' 
FROM (
    SELECT trips.request_at as day
          , count(*) as total
          , sum(case when status != 'completed' then 1 else 0 end) as canceled
    FROM 
        trips
    INNER JOIN
        users as clients
    ON trips.client_id = clients.users_id and clients.banned = 'no'
    INNER JOIN
        users as drivers
    ON trips.driver_id = drivers.users_id and drivers.banned = 'no'
    WHERE trips.request_at between str_to_date('2013-10-01', '%Y-%m-%d') and str_to_date('2013-10-03', '%Y-%m-%d')
    GROUP BY trips.request_at
) t1
ORDER BY t1.day