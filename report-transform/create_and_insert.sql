CREATE TABLE events
(
    event_id      integer,
    event_date    date,
    event_type_id integer
);

insert into events (event_id, event_date, event_type_id)
values (19, '2022-05-01', 10)
     , (23, '2022-05-01', 20)
     , (38, '2022-05-02', 20)
     , (43, '2022-05-03', 20)
     , (56, '2022-05-04', 20)
     , (61, '2022-05-05', 10)
     , (77, '2022-05-06', 10)
     , (83, '2022-05-06', 20)
     , (98, '2022-05-07', 20)
     , (120, '2022-05-08', 20)
     , (131, '2022-05-09', 10)
     , (144, '2022-05-10', 10)
     , (151, '2022-05-10', 20)
     , (174, '2022-05-11', 10)
     , (183, '2022-05-11', 20)
     , (196, '2022-05-12', 20)
     , (211, '2022-05-15', 10)
;