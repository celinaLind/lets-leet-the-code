
-- Incorrect Solution
select distinct W.id AS Id from Weather W 
inner join Weather T
on DATEDIFF(W.recordDate, T.recordDate)=1
where W.recordDate > T.recordDate;

-- Correct Solution: with inner query
select W.id as Id from Weather W
where W.temperature > (
    select T.temperature from Weather T
    where T.recordDate = DATE_SUB(W.recordDate, Interval 1 DAY)
);

-- Explaination
/*
    The inner query returns the temperature from days that are within a day of the W day
    - The DATE_SUB() function subtracts a time/date interval from a date and then returns the date.

    The Outer query: compares the temperature and returns the corresponding ids
*/

-- Correct Solution: with Cartesian Product and Where clause

SELECT T.id FROM Weather W, Weather T
WHERE DATEDIFF(T.recordDate, W.recordDate) = 1
AND T.temperature > W.temperature;

/*
    - 'DATEDIFF' function finds pairs of rows where the difference between the 'recordDate' in T and W is exactly 1 day
    - 'AND T.temperature > W.temperature' finds the days where the temperature is rising compared to the previous day
    - 'T.id' returns id with the higher temperature
*/

-- Better Solution: 320ms

Select w1.id 
from weather w1
Join weather w2
On w1.recordDate = DATE_ADD(w2.recordDate, Interval 1 day)
where w1.temperature > w2.temperature;