# Human Traffic of Stadium (leetcode hard) MS T-SQL

## Task

<pre>
Table: Stadium

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the primary key for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
No two rows will have the same visit_date, and as the id increases, the dates increase as well.

Write an SQL query to display the records with three or more rows with consecutive id's,
and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.

The query result format is in the following example.

Example 1:

Input:
Stadium table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
Output:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
Explanation:
The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended. 
Note that row 8 was included even though the visit_date was not the next day after row 7.
The rows with ids 2 and 3 are not included because we need at least three consecutive ids.

</pre>

## [solution](https://github.com/antovk/test-tasks/blob/main/trips-and-users/human-traffic-of-stadium.sql)

```sql
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
```
