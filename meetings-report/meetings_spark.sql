WITH t1 AS
         (SELECT 1 AS meeting_id, '2022-07-01 01:00:00' AS start_time, '2022-07-01 01:29:00' AS end_time UNION ALL
          SELECT 2 AS meeting_id, '2022-07-01 01:30:00' AS start_time, '2022-07-01 01:59:00' AS end_time UNION ALL
          SELECT 3 AS meeting_id, '2022-07-01 03:00:00' AS start_time, '2022-07-01 03:59:00' AS end_time UNION ALL
          SELECT 4 AS meeting_id, '2022-07-01 03:30:00' AS start_time, '2022-07-01 03:59:00' AS end_time UNION ALL
          SELECT 5 AS meeting_id, '2022-07-01 04:00:00' AS start_time, '2022-07-01 04:59:00' AS end_time UNION ALL
          SELECT 6 AS meeting_id, '2022-07-01 03:30:00' AS start_time, '2022-07-01 04:59:00' AS end_time UNION ALL
          SELECT 7 AS meeting_id, '2022-07-01 01:00:00' AS start_time, '2022-07-01 01:59:00' AS end_time)

SELECT t3.start_time
     , t3.end_time
     , count(*) AS num_meetings
FROM (SELECT t2.meeting_id
           , from_unixtime(unix_timestamp(cast(t2.start_time AS timestamp)) + rn * 15 * 60)           AS start_time
           , from_unixtime(unix_timestamp(cast(t2.start_time AS timestamp)) + rn * 15 * 60 + 14 * 60) AS end_time
      FROM (SELECT t1.*, row_number() OVER (PARTITION BY meeting_id) - 1 AS rn
            FROM t1 LATERAL VIEW explode(
               split(
                    space(
                         cast((unix_timestamp(t1.end_time) - unix_timestamp(t1.start_time) + 60) / 60 / 15 AS int -- calculate number of 15-minute intervals
                         ) - 1 -- subtract 1 to account for the first interval
                    ), ' ' -- split to array of spaces
               )) f1 -- explode the array into a list of 15-minute intervals
          ) t2
     ) t3
GROUP BY t3.start_time
       , t3.end_time
ORDER BY t3.start_time
       , t3.end_time