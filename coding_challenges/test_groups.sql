-- An automatic judging system checks a solution for the task on multiple test cases. 
-- The outcome of a test case is binary: either the solution succeeds or fails. 
-- But not all test cases are equally important. Each test case is assigned to a group, 
-- and every test case in the group is worth the same number of points.

-- You have received a raw report with the results of the automatic testing. 
-- The report consists of two tables, 

--   create table test_groups (
--       name varchar(40) not null,
--       test_value integer not null,
--       unique(name)
--   );

--   create table test_cases (
--       id integer not null,
--       group_name varchar(40) not null,
--       status varchar(5) not null,
--       unique(id)
--   );

-- Each row of the table test_goups contains information about a single group of tests: 
-- unique name (name) and the value of each test in the group (test_value). Each row of the table
-- test_cases contains information about a single test case: unique id(id), the name of the group
-- to which it belongs (group_name) and status(status). Status contains either one of two possible words: 
-- OK or ERROR.

-- Write an SQL query that summarizes each group of tests. The table of results should contain 
-- four columns: name(name f the group), all_test_cases(number of tests in the group), passed_tests_cases
-- (number of test cases with the status OK), and total_value(total value of passed tests in this group). 
-- Rows should be ordered by decreasing 

-- In the case of a tie, rows should be sorted lexicographically by name.

-- write your code in PostgreSQL 9.4
SELECT test_groups.name, 
    COUNT(test_cases.group_name) AS all_test_cases,
    SUM(CASE WHEN test_cases.status = 'OK' THEN 1 ELSE 0 END) AS passed_test_cases,
    SUM(CASE WHEN test_cases.status = 'OK' THEN 1 ELSE 0 END) * test_groups.test_value AS total_value
FROM test_groups
LEFT JOIN test_cases
ON test_groups.name = test_cases.group_name
GROUP BY test_groups.name, test_groups.test_value
ORDER BY total_value DESC, test_groups.name;