WITH stadium as (
select 1 as id, convert(datetime, '2017-01-01', 102) as visit_date, 10 as people  UNION ALL
select 2,       convert(datetime, '2017-01-02', 102),               109           UNION ALL  
select 3,       convert(datetime, '2017-01-03', 102),               150           UNION ALL
select 4,       convert(datetime, '2017-01-04', 102),               99            UNION ALL  
select 5,       convert(datetime, '2017-01-05', 102),               145           UNION ALL  
select 6,       convert(datetime, '2017-01-06', 102),               1455          UNION ALL  
select 7,       convert(datetime, '2017-01-07', 102),               199           UNION ALL  
select 8,       convert(datetime, '2017-01-09', 102),               188
)

select 
    st_1.id
    , st_1.visit_date
    , st_1.people
from 
    stadium st_1
left join
    stadium st_2
    on st_2.id between st_1.id - 2 and st_1.id + 2
where 
    st_1.people >= 100
    and st_2.people >= 100
group by
    st_1.id
    , st_1.visit_date
    , st_1.people
having
    sum(case when st_2.id < st_1.id then st_2.id else 0 end) = st_1.id * 2 - 3
    or sum(case when st_2.id > st_1.id then st_2.id else 0 end) = st_1.id * 2 + 3
    or (sum(case when st_2.id < st_1.id then st_2.id else 0 end) = st_1.id - 1 
            and sum(case when st_2.id > st_1.id then st_2.id else 0 end) = st_1.id + 1)
order by
    st_1.id