-- Import in hbtn_0c_0 database this table dump:[https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql]
-- displays the max temperature of each state (ordered by State name).

SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;
