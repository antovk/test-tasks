SELECT 
       row_number() OVER (PARTITION BY event_type_id ORDER BY event_date)                             AS rn
     , event_type_id                                                                                  AS evt_type_id
     , event_date                                                                                     AS start_date
     , lead(t1.lag_evt_date, 1, max_event_date) OVER (PARTITION BY event_type_id ORDER BY event_date) AS end_date

FROM 
     (SELECT 
             event_type_id
           , ev.event_date
           , lag(event_date, 1, event_date) OVER (PARTITION BY event_type_id ORDER BY event_date) AS lag_evt_date
           , max(event_date) OVER (PARTITION BY event_type_id)                                    AS max_event_date
      FROM 
          events ev) t1

WHERE 
     t1.event_date - 1 != t1.lag_evt_date

ORDER BY 
         t1.event_type_id
       , t1.event_date;