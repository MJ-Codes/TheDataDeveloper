# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:13:43 2020

@author: crein
"""


CREATE TABLE CUSTOMERS(
   ID   INT              NOT NULL,
   NAME VARCHAR (20)     NOT NULL,
   AGE  INT              NOT NULL,
   ADDRESS  CHAR (25) ,
   SALARY   DECIMAL (18, 2),  -- 18 total digits, 2 after the period     
   PRIMARY KEY (ID)
);





SELECT title
FROM films
WHERE release_year >= 1994
AND release_year <= 2000;


SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000; -- BETWEEN is inclusive


SELECT title, release_year
 FROM films
 WHERE release_year IN (1990, 2000)
 AND duration > 120;
 
SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;

SELECT name
FROM people
WHERE birthdate IS NOT NULL

SELECT name
FROM people
WHERE name LIKE 'B%';


SELECT name 
FROM people
WHERE name NOT LIKE 'A%'; 


SELECT MAX(gross)
FROM films
WHERE release_year BETWEEN 2000 AND 2012;


SELECT (AVG(duration) / 60.0) AS avg_duration_hours
FROM films;


SELECT (MAX(release_year) - MIN(release_year)) / 10 AS number_of_decades
FROM films;


SELECT * 
FROM films 
WHERE release_year <> 2015
ORDER BY duration;

SELECT imdb_score, film_id
FROM reviews
ORDER BY imdb_score DESC;


SELECT certification, release_year, title
FROM films
ORDER BY certification, release_year;


SELECT release_year, country, MAX(budget)
FROM films
GROUP BY release_year, country
ORDER BY release_year, country;



Select release_year, AVG(budget) AS avg_budget , AVG(gross) AS avg_gross
FROM films
WHERE country = 'USA'
GROUP BY release_year
HAVING AVG(budget) > 3800000
ORDER BY AVG(gross) DESC;



SELECT country, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
GROUP BY country
HAVING COUNT(title) > 10
ORDER BY country
LIMIT 5;




JOINS


SELECT cities.name AS city, countries.name AS country, region
FROM cities
  INNER JOIN countries
    ON cities.country_code = countries.code;
    
    
SELECT c.code AS country_code, c.name, e.year, e.inflation_rate
FROM countries AS c
    INNER JOIN economies AS e
        ON c.code = e.code;
        
        
SELECT c.code, c.name, c.region, e.year, e.unemployment_rate, p.fertility_rate
  FROM countries AS c
   INNER JOIN populations AS p
        ON c.code = p.country_code
    INNER JOIN economies AS e
        ON p.country_code = e.code AND p.year = e.year;
        
        
        
SELECT c.name AS country, c.continent, l.name AS language, l.official
    FROM countries AS c
    INNER JOIN languages AS l
        USING(code);   
        
        
#SELF  JOIN COMPARING THE TWO DIFFERENT YEARS IN THE YEAR COLUMN OF TABLE POPULATIONS
        
SELECT p1.country_code,
       p1.size AS size2010, 
       p2.size AS size2015,
       -- 1. calculate growth_perc
       ((p2.size - p1.size)/p1.size * 100.0) AS growth_perc
-- 2. From populations (alias as p1)
FROM populations AS p1
  -- 3. Join to itself (alias as p2)
  INNER JOIN populations AS p2
    -- 4. Match on country code
    ON p1.country_code = p2.country_code
        -- 5. and year (with calculation)
        AND p1.year = p2.year - 5;
        
        
        
        
SELECT country_code, size,
  CASE WHEN size > 50000000
            THEN 'large'
       WHEN size > 1000000
            THEN 'medium'
       ELSE 'small' END
       AS popsize_group
INTO pop_plus  --INTO creates a new table in the default filegroup and inserts the resulting rows from the query into it.  
FROM populations
WHERE year = 2015;


SELECT name, continent, geosize_group, popsize_group
FROM countries_plus AS c
  INNER JOIN pop_plus AS p
    ON c.code = p.country_code
ORDER BY geosize_group;
        



SELECT region, AVG(gdp_percapita) AS avg_gdp
FROM countries as c
  LEFT JOIN economies as e
    ON c.code = e.code
WHERE e.year = 2010
GROUP BY region
ORDER BY avg_gdp DESC;



SELECT cities.name AS city, urbanarea_pop, countries.name AS country,
       indep_year, languages.name AS language, percent
FROM languages
  RIGHT JOIN countries 
    ON languages.code = countries.code
  RIGHT JOIN cities
    ON countries.code = cities.country_code
ORDER BY city, language;





SELECT name AS country, code, region, basic_unit
FROM countries
   FULL JOIN currencies -- can also use LEFT AND INNER JOINS
      USING (code)
WHERE region = 'North America' OR region IS NULL
ORDER BY region;


SELECT countries.name, code, languages.name AS language
FROM languages 
   FULL JOIN countries 
      USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;



SELECT c1.name AS country, region, l.name as language, c2.basic_unit, frac_unit

FROM countries AS c1
   FULL JOIN languages AS l
      USING (code)
   FULL JOIN currencies AS c2
      USING (code)
WHERE region LIKE 'M%a';



CROSS JOIN


SELECT c.name AS city, l.name AS language
FROM cities AS c        
  CROSS JOIN languages AS l -- # of rows in the first table multiplied by the number of rows in the second table, filtered by the where clause
WHERE c.name LIKE 'Hyder%';



UNION AND UNION ALL


SELECT country_code
    FROM cities
		UNION --combines unique value result sets of two more select statements
SELECT code
   FROM currencies
ORDER BY country_code;


SELECT code, year
    FROM economies
	UNION ALL -- combines all value including duplicate result sets of two more select statements
SELECT country_code, year
   FROM populations
ORDER BY code, year;



INTERSECT

SELECT code, year
  FROM economies
	INTERSECT /* Used to combine two SELECT statments, returning rows only from the 
                first SELECT statment that are identical to a row in the 
                second SELECT statement */
SELECT country_code, year
   FROM populations
ORDER BY code, year;


EXCEPT

SELECT name
   FROM cities
	EXCEPT   /* Used to combine two SELECT statements and returns rows from the first 
              SELECT statement that are not returned by the second SELECT statement.*/
SELECT capital
  FROM countries
ORDER BY name;



 
 
COMPARING VALUES IN CASE STATEMENTS

SELECT 
	-- Select the date of the match
	date,
	-- Identify home wins, losses, or ties
	CASE WHEN home_goal > away_goal THEN 'Home win!'
        WHEN home_goal < away_goal THEN 'Home loss :(' 
        ELSE 'Tie' END AS outcome
FROM matches_spain;




SELECT 
	m.date,
	t.team_long_name AS opponent,
    -- Complete the CASE statement with an alias
	CASE WHEN m.home_goal > m.away_goal THEN 'Barcelona win!'
        WHEN m.home_goal < m.away_goal THEN 'Barcelona loss :(' 
        ELSE 'Tie' END AS outcome 
FROM matches_spain AS m
LEFT JOIN teams_spain AS t 
ON m.awayteam_id = t.team_api_id
-- Filter for Barcelona as the home team
WHERE m.hometeam_id = 8634; 




MULTIPLE LOGICAL CONDITIONS IN A CASE STATEMENT

SELECT
	date,
	CASE WHEN hometeam_id = 8634 THEN 'FC Barcelona' 
         ELSE 'Real Madrid CF' END as home,
	CASE WHEN awayteam_id = 8634 THEN 'FC Barcelona' 
         ELSE 'Real Madrid CF' END as away,
	-- Identify all possible match outcomes
	CASE WHEN home_goal > away_goal AND hometeam_id = 8634 THEN 'Barcelona win!'
         WHEN home_goal > away_goal AND hometeam_id = 8633 THEN 'Real Madrid win!'
         WHEN home_goal < away_goal AND awayteam_id = 8634 THEN 'Barcelona win!'
         WHEN home_goal < away_goal AND awayteam_id = 8633 THEN 'Real Madrid win!'
         ELSE 'Tie!' END AS outcome
FROM matches_spain
WHERE (awayteam_id = 8634 OR hometeam_id = 8634)
      AND (awayteam_id = 8633 OR hometeam_id = 8633);
      
  




FILTERING THE CASE STATEMENT IN THE WHERE CLAUSE


-- Select the season, date, home_goal, and away_goal columns
SELECT 
	season,
    date,
	home_goal,
	away_goal
FROM matches_italy
WHERE 
-- Exclude games not won by Bologna
	CASE WHEN hometeam_id = 9857 AND home_goal > away_goal THEN 'Bologna Win'
		 WHEN awayteam_id = 9857 AND away_goal > home_goal THEN 'Bologna Win' 
		 END IS NOT NULL;    -- this filters out all NULL values generated
         
         


COUNTING MATCHES PLAYED BY EACH COUNTRY ACROSS 3 SEASONS

SELECT 
	c.name AS country,
    -- Count matches in each of the 3 seasons
	COUNT(CASE WHEN m.season = '2012/2013' THEN m.country_id END) AS matches_2012_2013,
	COUNT(CASE WHEN m.season = '2013/2014' THEN m.country_id END) AS matches_2013_2014,
	COUNT(CASE WHEN m.season = '2014/2015' THEN m.country_id END) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
-- Group by country name alias
GROUP BY country;


USING SUM AND CASE WITH MULTIPLE CONDITIONS

SELECT 
	c.name AS country,
    -- Sum the total records in each season where the home team won
	SUM(CASE WHEN m.season = '2012/2013' AND m.home_goal > m.away_goal 
        THEN 1 ELSE 0 END) AS matches_2012_2013,
 	SUM(CASE WHEN m.season = '2013/2014' AND m.home_goal > m.away_goal 
        THEN 1 ELSE 0 END) AS matches_2013_2014,
	SUM(CASE WHEN m.season = '2014/2015' AND  m.home_goal > m.away_goal
        THEN 1 ELSE 0 END) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
-- Group by country name alias
GROUP BY country;



USING AVERAGE AND CASE WITH MULTIPLE CONDITIONS

SELECT 
	c.name AS country,
    -- Round the percentage of tied games to 2 decimal points
	ROUND(AVG(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2013/2014' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2013_2014,
	ROUND(AVG(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2014/2015' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;



SUBQUERYS IN THE WHERE CLAUSE

SELECT 
	-- Select the team long and short names
	team_long_name,
	team_short_name
	FROM team
-- Exclude all values from the subquery
WHERE team_api_id NOT IN
     (SELECT DISTINCT hometeam_ID FROM match);
     
     
SELECT
	-- Select the team long and short names
	team_long_name,
	team_short_name
FROM team
-- Filter for teams with 8 or more home goals
WHERE team_api_id IN
	  (SELECT hometeam_id 
       FROM match
       WHERE home_goal >= 8);
    
    
    

SUBQUERYS IN THE FROM CLAUSE

SELECT
	-- Select country, date, home, and away goals from the subquery
    country,
    date,
    home_goal,
    away_goal
FROM 
	-- Select country name, date, and total goals in the subquery
	(SELECT c.name AS country, 
     	    m.date as date, 
     		m.home_goal as home_goal,
     		m.away_goal as away_goal,
        (m.home_goal + m.away_goal) AS total_goals
    FROM match AS m
    LEFT JOIN country AS c
    ON m.country_id = c.id) AS subq
-- Filter by total goals scored in the main query
WHERE total_goals >= 10;




SUBQUERYS IN THE SELECT CLAUSE

SELECT 
	l.name AS league,
    -- Select and round the average goals per league in 2013/2014
    ROUND(AVG(m.home_goal + m.away_goal),2) AS avg_goals,
    -- Select and round the average total goals for all leagues in 2013/2014
    (SELECT ROUND(AVG(home_goal + away_goal),2) 
     FROM match
     WHERE season = '2013/2014') AS overall_avg
FROM league AS l
LEFT JOIN match AS m
ON l.country_id = m.country_id
-- Filter for the 2013/2014 season
WHERE m.season = '2013/2014'
GROUP BY l.name;


SELECT 
	-- Select the league name and average goals scored
	l.name AS league,
	ROUND(AVG(m.home_goal + m.away_goal),2) AS avg_goals,
    -- Subtract the overall average from the league average
	ROUND(AVG(m.home_goal + m.away_goal) - 
          (SELECT AVG(home_goal + away_goal)
           FROM match 
           WHERE season = '2013/2014'),2) AS diff
FROM league AS l
LEFT JOIN match AS m
ON l.country_id = m.country_id
-- Only include 2013/2014 results
WHERE m.season = '2013/2014'
GROUP BY l.name;



MORE SUBQUERIES

SELECT 
	-- Select the stage and average goals for each stage
	m.stage,
    ROUND(AVG(m.home_goal + m.away_goal),2) AS avg_goals,
    -- Select the average overall goals for the 2012/2013 season
    (SELECT ROUND(AVG(home_goal + away_goal),2) 
       FROM match 
       WHERE season = '2012/2013') AS overall
FROM match AS m
-- Filter for the 2012/2013 season
WHERE season = '2012/2013'
-- Group by stage
GROUP BY m.stage;


SELECT 
	-- Select the stage and average goals from the subquery
	s.stage,
    ROUND(s.avg_goals,2) AS avg_goals
FROM 
	-- Select the stage and average goals in 2012/2013
	(SELECT
         stage,
         AVG(home_goal + away_goal) AS avg_goals
     FROM match
     WHERE season = '2012/2013'
     GROUP BY stage) AS s
WHERE 
	-- Filter the main query using the subquery
	s.avg_goals > (SELECT AVG(home_goal + away_goal) 
                   FROM match WHERE season = '2012/2013');



SELECT 
	-- Select the stage and average goals from s
s.stage,
ROUND(s.avg_goals,2) AS avg_goal,
    -- Select the overall average for 2012/2013
	(SELECT AVG(home_goal + away_goal) FROM match WHERE season = '2012/2013') AS overall_avg
FROM 
	-- Select the stage and average goals in 2012/2013 from match
	(SELECT
         stage,
         AVG(home_goal + away_goal) AS avg_goals
     FROM match
     WHERE season = '2012/2013'
     GROUP BY stage) AS s
WHERE 
	-- Filter the main query using the subquery
s.avg_goals > 
    (SELECT AVG(home_goal + away_goal) 
                   FROM match WHERE season = '2012/2013');
    
    

CORRELATED SUBQUERIES

"""
Correlated Subqueries are used to select data from a table referenced in the outer query.
The subquery is known as a correlated because the subquery is related to the outer query.

"""

SELECT 
	-- Select country ID, date, home, and away goals from match
	main.country_id,
    main.date,
    main.home_goal, 
    main.away_goal
FROM match AS main
WHERE 
	-- Filter the main query by the subquery
	(main.home_goal + main.away_goal) > 
        (SELECT AVG((sub.home_goal + sub.away_goal) * 3)
         FROM match AS sub
         -- Join the main query to the subquery in WHERE
         WHERE main.country_id = sub.country_id);
    
    
        
SELECT 
	-- Select country ID, date, home, and away goals from match
	main.country_id,
    main.date,
    main.home_goal,
    main.away_goal,
    main.season
FROM match AS main
WHERE 
	-- Filter for matches with the highest number of goals scored
	(main.home_goal + main.away_goal) =
        (SELECT MAX(sub.home_goal + sub.away_goal)
         FROM match AS sub
         WHERE main.country_id = sub.country_id
               AND main.season = sub.season);
        
        




NESTED SUBQUERIES


# Simply nested subquery
SELECT 
	-- Select the season and max goals scored in a match
season,
MAX(home_goal + away_goal) AS max_goals,
    -- Select the overall max goals scored in a match to complete the first simple nested subquery
   (SELECT MAX(home_goal + away_goal) FROM match) AS overall_max_goals,
    -- Select the max number of goals scored in any match in July to complete the second simple nested subquery
   (SELECT MAX(home_goal + away_goal) 
        FROM match
        WHERE id IN (
              SELECT id FROM match WHERE EXTRACT(MONTH FROM date) = 07)) AS july_max_goals
FROM match
GROUP BY season







# Nested, correlated  subquery in FROM
SELECT
	c.name AS country,
    -- Calculate the average matches per season
    AVG(outer_s.matches) AS avg_seasonal_high_scores
FROM country AS c
-- Left join outer_s to country
LEFT JOIN (
-- the outer subquery in FROM
  SELECT country_id, season,
         COUNT(id) AS matches
-- the inner subquery in FROM
  FROM (
    SELECT country_id, season, id
	FROM match
	WHERE home_goal >= 5 OR away_goal >= 5) AS inner_s
  -- Close parentheses and alias the subquery
  GROUP BY country_id, season) AS outer_s
-- This is the correlation between the main query and the outer subquery
ON c.id = outer_s.country_id
GROUP BY country;





COMMON TABLE EXPRESSIONS

"""
You can list one (or more) subqueries as common table expressions (CTEs)
by declaring them ahead of your main query, which is an excellent tool 
for organizing information and placing it in a logical order.

"""

-- Set up your CTE
WITH match_list AS (
    SELECT 
  		country_id, 
  		id
    FROM match
    WHERE (home_goal + away_goal) >= 10)
-- Select league and count of matches from the CTE
SELECT
    l.name AS league,
    COUNT(match_list.id) AS matches
FROM league AS l
-- Join the CTE to the league table
LEFT JOIN match_list ON l.id = match_list.country_id
GROUP BY l.name;


-- Set up your CTE
WITH match_list AS (
  -- Select the league, date, home, and away goals
    SELECT 
  		l.name AS league, 
     	m.date,
  		m.home_goal,
  		m.away_goal,
       (m.home_goal + m.away_goal) AS total_goals
    FROM match AS m
    LEFT JOIN league as l ON m.country_id = l.id)
-- Select the league, date, home, and away goals from the CTE
SELECT league, date, home_goal, away_goal
FROM match_list
-- Filter by total goals
WHERE total_goals >= 10;



-- Set up your CTE
WITH match_list AS (
    SELECT 
  		country_id, 
  	   (home_goal + away_goal) AS goals
    FROM match
    -- Create a list of match IDs to filter data in the CTE
    WHERE id IN (
       SELECT id
       FROM match
       WHERE season = '2013/2014' AND EXTRACT(MONTH FROM date) = 08))
-- Select the league name and average of goals in the CTE
SELECT
	l.name,
    AVG(match_list.goals)
FROM league AS l
-- Join the CTE onto the league table
LEFT JOIN match_list ON l.id = match_list.country_id
GROUP BY l.name;




COMBINING QUERY SKILLS

# Using Subquery and Joins
SELECT
	m.date,
    -- Get the home and away team names
    hometeam,
    awayteam,
    m.home_goal,
    m.away_goal
FROM match AS m
-- Join the home subquery to the match table
LEFT JOIN (
  SELECT match.id, team.team_long_name AS hometeam
  FROM match
  LEFT JOIN team
  ON match.hometeam_id = team.team_api_id) AS home
ON home.id = m.id
-- Join the away subquery to the match table
LEFT JOIN (
  SELECT match.id, team.team_long_name AS awayteam
  FROM match
  LEFT JOIN team
  -- Get the away team ID in the subquery
  ON match.awayteam_id = team.team_api_id) AS away
ON away.id = m.id;



# Using Correlated Subqueries
SELECT
    m.date,
    (SELECT team_long_name
     FROM team AS t
     WHERE t.team_api_id = m.hometeam_id) AS hometeam,
    -- Connect the team to the match table
    (SELECT team_long_name
     FROM team AS t
     WHERE t.team_api_id = m.awayteam_id) AS awayteam,
    -- Select home and away goals
     home_goal,
     away_goal
     
FROM match AS m;



# Using CTE
WITH home AS (
  SELECT m.id, m.date, 
  		 t.team_long_name AS hometeam, m.home_goal
  FROM match AS m
  LEFT JOIN team AS t 
  ON m.hometeam_id = t.team_api_id),
-- Declare and set up the away CTE
away AS (
  SELECT m.id, m.date, 
  		 t.team_long_name AS awayteam, m.away_goal
  FROM match AS m
  LEFT JOIN team AS t 
  ON m.awayteam_id = t.team_api_id)
-- Select date, home_goal, and away_goal
SELECT 
	home.date,
    home.hometeam,
    away.awayteam,
    home.home_goal,
    away.away_goal
-- Join away and home on the id column
FROM home
INNER JOIN away
ON home.id = away.id;



WINDOWS FUNCTIONS

OVER() CLAUSE

"""
OVER clause defines a window or user-specified set of rows
within a query result set. A window function then computes 
a value for each row in the window

"""
#Note the Group By clause is not necessary for the simple OVER CLAUSE
SELECT 
	-- Select the id, country name, season, home, and away goals
	m.id, 
    c.name AS country, 
    m.season,
	m.home_goal,
	m.away_goal,
    -- Use a window to include the aggregate average in each row
	AVG(m.home_goal + m.away_goal) OVER() AS overall_avg
FROM match AS m
LEFT JOIN country AS c ON m.country_id = c.id;


# Using the Over() clause with Order By to initiate a Rank()
# Note Ascending Order is default add DESC for Descending Order
SELECT 
	-- Select the league name and average goals scored
	l.name AS league,
    AVG(m.home_goal + m.away_goal) AS avg_goals,
    -- Rank each league according to the average goals
    RANK() OVER(ORDER BY AVG(m.home_goal + m.away_goal)) AS league_rank
FROM league AS l
LEFT JOIN match AS m 
ON l.id = m.country_id
WHERE m.season = '2011/2012'
GROUP BY l.name
-- Order the query by the rank you created
ORDER BY league_rank;


OVER() CLAUSE WITH PARTITION
'''
Note the Group By clause is not necessary for the non aggregation
function columns when using Partition with the Over clause
'''

# The PARTITION BY clause allows you to calculate separate "windows" 
#based on columns you want to divide your results
SELECT
	date,
	season,
	home_goal,
	away_goal,
	CASE WHEN hometeam_id = 8673 THEN 'home' 
		 ELSE 'away' END AS warsaw_location,
    -- Calculate the average goals scored partitioned by season
    AVG(home_goal) OVER(PARTITION BY season) AS season_homeavg,
    AVG(away_goal) OVER(PARTITION BY season) AS season_awayavg
FROM match
-- Filter the data set for Legia Warszawa matches only
WHERE 
	hometeam_id = 8673 
    OR awayteam_id = 8673
ORDER BY (home_goal + away_goal) DESC;



PARTITION BY MULTIPLE COLUMNS

SELECT 
	date,
	season,
	home_goal,
	away_goal,
	CASE WHEN hometeam_id = 8673 THEN 'home' 
         ELSE 'away' END AS warsaw_location,
	-- Calculate average goals partitioned by season and month
    AVG(home_goal) OVER(PARTITION BY season,
         	EXTRACT(MONTH FROM date)) AS season_mo_home,
    AVG(away_goal) OVER(PARTITION BY season,  
            EXTRACT(MONTH FROM date)) AS season_mo_away
FROM match
WHERE 
	hometeam_id = 8673 
    OR awayteam_id = 8673
ORDER BY (home_goal + away_goal) DESC;




SLIDING WINDOWS

"""
Sliding windows allow you to create running calculations between
any two points in a window using functions such as PRECEDING,
FOLLOWING, and CURRENT ROW

"""

SELECT 
	date,
	home_goal,
	away_goal,
    -- Create a running total and running average of home goals
	SUM(home_goal) OVER(ORDER BY date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total,
    AVG(home_goal) OVER(ORDER BY date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_avg
FROM match
WHERE 
	hometeam_id = 9908 
    AND season = '2011/2012';
    
    

SELECT 
	-- Select the date, home goal, and away goals
	date,
	home_goal,
	away_goal,
    -- Create a running total and running average of home goals in reverse order with a  backward running total
    SUM(home_goal) OVER(ORDER BY date DESC
        ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS running_total,
    AVG(home_goal) OVER(ORDER BY date DESC
        ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS running_avg
FROM match
WHERE 
	awayteam_id = 9908 
    AND season = '2011/2012';
    
    
    
MORE EXAMPLES OF CASE STATEMENTS, SUBQUERIES, CTE`S, AND WINDOW FUNCTIONS

SELECT 
    m.id, 
	t.team_long_name,
    -- Identify matches as home/away wins or ties
	CASE WHEN m.home_goal > m.away_goal THEN 'MU Win'
		 WHEN m.home_goal < m.away_goal THEN 'MU Loss' 
         ELSE 'Tie' END AS outcome
FROM match AS m
-- Left join team on the home team ID and team API id
LEFT JOIN team AS t 
ON m.hometeam_id = t.team_api_id
WHERE 
	-- Filter for 2014/2015 and Manchester United as the home team
	m.season = '2014/2015'
	AND t.team_long_name = 'Manchester United';
    
    
SELECT 
	m.id, 
    t.team_long_name,
    -- Identify matches as home/away wins or ties
	CASE WHEN m.away_goal < m.home_goal THEN 'MU Loss'
		 WHEN m.away_goal > m.home_goal THEN  'MU Win'
         ELSE 'Tie' END AS outcome
-- Join team table to the match table
FROM match AS m
LEFT JOIN team AS t 
ON m.awayteam_id = t.team_api_id
WHERE 
	-- Filter for 2014/2015 and Manchester United as the away team
	season = '2014/2015'
	AND t.team_long_name = 'Manchester United';
    
    


-- Set up the home team CTE
WITH home AS (
  SELECT m.id, t.team_long_name,
	  CASE WHEN m.home_goal > m.away_goal THEN 'MU Win'
		   WHEN m.home_goal < m.away_goal THEN 'MU Loss' 
  		   ELSE 'Tie' END AS outcome
  FROM match AS m
  LEFT JOIN team AS t 
  ON m.hometeam_id = t.team_api_id),
-- Set up the away team CTE
away AS (
  SELECT m.id, t.team_long_name,
	  CASE WHEN m.home_goal > m.away_goal THEN 'MU Loss'
		   WHEN m.home_goal < m.away_goal THEN 'MU Win' 
  		   ELSE 'Tie' END AS outcome
  FROM match AS m
  LEFT JOIN team AS t
  ON m.awayteam_id = t.team_api_id)
-- Select team names, the date and goals
SELECT DISTINCT
    m.date,
    home.team_long_name AS home_team,
    away.team_long_name AS away_team,
    m.home_goal,
    m.away_goal
-- Join the CTEs onto the match table
FROM match AS m
LEFT JOIN home ON m.id = home.id
LEFT JOIN away ON m.id = away.id
WHERE m.season = '2014/2015'
      AND (home.team_long_name = 'Manchester United' 
           OR away.team_long_name = 'Manchester United');
           
           
           
           
ADDING A WINDOWS FUNCTION TO THE ABOVE EXAMPLE         
           
-- Set up the home team CTE
WITH home AS (
  SELECT m.id, t.team_long_name,
	  CASE WHEN m.home_goal > m.away_goal THEN 'MU Win'
		   WHEN m.home_goal < m.away_goal THEN 'MU Loss' 
  		   ELSE 'Tie' END AS outcome
  FROM match AS m
  LEFT JOIN team AS t ON m.hometeam_id = t.team_api_id),
-- Set up the away team CTE
away AS (
  SELECT m.id, t.team_long_name,
	  CASE WHEN m.home_goal > m.away_goal THEN 'MU Loss'
		   WHEN m.home_goal < m.away_goal THEN 'MU Win' 
  		   ELSE 'Tie' END AS outcome
  FROM match AS m
  LEFT JOIN team AS t ON m.awayteam_id = t.team_api_id)
-- Select columns and and rank the matches by date
SELECT DISTINCT
    m.date,
    home.team_long_name AS home_team,
    away.team_long_name AS away_team,
    m.home_goal, m.away_goal,
    RANK() OVER(ORDER BY ABS(home_goal - away_goal) DESC) as match_rank
-- Join the CTEs onto the match table
FROM match AS m
LEFT JOIN home ON m.id = home.id
LEFT JOIN away ON m.id = away.id
WHERE m.season = '2014/2015'
	  AND ((home.team_long_name = 'Manchester United' AND home.outcome = 'MU Loss')
	  OR (away.team_long_name = 'Manchester United' AND away.outcome = 'MU Loss'));
	 























