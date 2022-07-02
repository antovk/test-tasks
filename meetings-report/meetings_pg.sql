WITH RECURSIVE t1 AS (SELECT m1.meeting_id
                           , m1.start_datetime
                           , m1.start_datetime + INTERVAL '14 minutes' AS period_end_time
                           , m1.end_datetime
                      FROM meetings m1
                      UNION ALL
                      SELECT t1.meeting_id
                           , t1.period_end_time + INTERVAL '1 minute'
                           , t1.period_end_time + INTERVAL '15 minutes'
                           , t1.end_datetime
                      FROM t1
                      WHERE t1.period_end_time < t1.end_datetime)
SELECT to_char(start_datetime, 'hh24:mi') as start_time
     , to_char(period_end_time, 'hh24:mi') as end_time
     , count(*) as num_meetings
FROM t1
GROUP BY t1.start_datetime
       , t1.period_end_time
ORDER BY t1.start_datetime
       , t1.period_end_time;