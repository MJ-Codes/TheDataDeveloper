


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
	 




MORE IN DEPTH SQL CODE EXAMPLES


QUERY INFORMATION_SCHEMA WITH SELECT

-- Query the right table in information_schema
SELECT table_name 
FROM information_schema.tables
-- Specify the correct table_schema value
WHERE table_schema = 'public';


-- Query the right table in information_schema to get columns
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'university_professors' AND table_schema = 'public';


CREATING TABLES

-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

-- Print the contents of this table
SELECT * 
FROM professors


ADDING COLUMNS

-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;

-- Print the contents of this table
SELECT * 
FROM professors




RENAMING AND DROPPING COLUMNS

-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;


-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;


MIGRATE DATA FROM ONE TABLE TO ANOTHER TABLE STRUCTURE

-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM university_professors;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;

DROP TABLE

DROP TABLE university_professors;



CASTING DATA TYPES

-- Calculate the net amount as amount + fee
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount 
FROM transactions;


CHANGING DATA TYPES WITH ALTER COLUMN

-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE CHAR(3);


CONVERTING TYPES USING A FUNCTION

-- Convert the values in firstname to a max. of 16 characters
ALTER TABLE professors 
ALTER COLUMN firstname 
TYPE varchar(16)
USING SUBSTRING(firstname FROM 1 FOR 16);


SETTING A NOT NULL CONSTRAINT ON AN EXISTING TABLE COLUMN

-- Disallow NULL values in firstname
ALTER TABLE professors 
ALTER COLUMN firstname
SET NOT NULL;


SETTING A UNIQUE CONSTRAINT ON AN EXISTING TABLE COLUMN

-- Make universities.university_shortname unique
ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE(university_shortname);


-- Rename the organization column to id
ALTER TABLE organizations
RENAME COLUMN organization TO id;

-- Make id a primary key
ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);



DETERMINING WHETHER A CERTAIN COLUMN CAN BE USED AS AN UNIQUE INDENTIFYING KEY

-- Count the number of distinct values in the university_city column
SELECT COUNT(DISTINCT(university_city)) 
FROM universities;

-- Try out different combinations
SELECT COUNT(DISTINCT (firstname,lastname))
FROM professors;




ADDING A  SERIAL SURROGATE

-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);



CONCATENATE COLUMNS TO A SURROGATE KEY

FROM cars;

-- Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);

-- Update id with make + model
UPDATE cars
SET id = CONCAT(make, model);

-- Make id a primary key
ALTER TABLE cars
ADD CONSTRAINT id_pk PRIMARY KEY(id);



REFERENCING A TABLE WITH A FOREIGN KEY

-- Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id;

-- Add a foreign key on professors referencing universities
ALTER TABLE professors  
ADD CONSTRAINT professors_fkey FOREIGN KEY(university_id) REFERENCES universities(id);



POPULATING A TABLES COLUMN WITH VALUES FROM ANOTHER TABLES COLUMN

-- Set professor_id to professors.id where firstname, lastname correspond to rows in professors
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname;



RETRIEVING TABLE FOREIGN KEY CONSTRAINT INFORMATION

-- Identify the correct constraint name
SELECT constraint_name, table_name, constraint_type
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';


DROPPING A CONSTRAINT IN ORDER TO ALTER THE CONSTRAINT

-- Drop the right foreign key constraint
ALTER TABLE affiliations
DROP CONSTRAINT affiliations_organization_id_fkey;


ADDING BACK THE ALTERED CONSTRAINT WITH DIFFERENT REFERENTIAL INTEGRITY INSTRUCTIONS

-- Add a new foreign key constraint from affiliations to organizations which cascades deletion
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_id_fkey FOREIGN KEY(organization_id) REFERENCES organizations (id) ON DELETE CASCADE;








SUBQUERYS

INSIDE THE WHERE CLAUSE

# notice filter 'year' must be the same in the sub and main query
SELECT *
FROM populations
WHERE life_expectancy >
   1.15 * (SELECT AVG(life_expectancy)
   FROM populations
   WHERE year = 2015) AND
  year = 2015;
  

SELECT DISTINCT name
  FROM languages
WHERE code IN
  (SELECT code
   FROM countries
   WHERE region = 'Middle East')
ORDER BY name;

THE INNER JOIN EQUIVALENT TO THE ABOVE

SELECT DISTINCT languages.name AS language
FROM languages
INNER JOIN countries
ON languages.code = countries.code
WHERE region = 'Middle East'
ORDER BY language;



SELECT name
  FROM cities AS c1
  WHERE country_code IN
(
   SELECT e.code
    FROM economies AS e
      UNION -- combines the first two SELECT statements
    SELECT c2.code
    FROM currencies AS c2
      EXCEPT -- returns only those rows not available in the following SELECT statement
    SELECT p.country_code
    FROM populations AS p
);
  
 
SELECT name, country_code, city_proper_pop, metroarea_pop,
	  -- Calculate city_perc
      city_proper_pop / metroarea_pop * 100 AS city_perc
   FROM cities
   WHERE name IN
     (SELECT capital
     FROM countries
     WHERE (continent = 'Europe'
        OR continent LIKE '%America'))
       AND metroarea_pop IS NOT NULL
ORDER BY city_perc DESC
LIMIT 10;
  
  
  
  
  
DETERMINING MISSING VALUES AFTER A JOIN
(When joining countries table to continent table
 on code column)

SELECT code, name
  FROM countries
  WHERE continent = 'Oceania'
  	AND code NOT IN
  	(SELECT code
  	 FROM currencies);
  
  
  
    
SUBQUERY INSIDE THE SELECT CLAUSE COMPARED TO THE EQUIVALENT INNER JOIN

SELECT countries.name AS country, COUNT(*) AS cities_num
  FROM cities
    INNER JOIN countries
    ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;


SELECT countries.name AS country,
  (SELECT COUNT(*) AS cities_num
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;




  
 

SUBQUERY INSIDE THE FROM CLAUSE
'''relates the local_name from countries to code from languages
to ultimately get a count of local names'''
SELECT local_name, subquery.lang_num
  FROM countries,
  	(SELECT code, COUNT(*) AS lang_num
  	 FROM languages
  	 GROUP BY code) AS subquery
  WHERE countries.code = subquery.code
ORDER BY lang_num DESC;




'''INNER JOING OF TWO TABLES
USING A SELECTION FROM A SUBQUERY IN THE FROM CLAUSE THAT IS GROUPED
BY CONTINENT'''
SELECT name, continent, inflation_rate
    FROM countries
		INNER JOIN economies
		ON countries.code = economies.code
    WHERE year = 2015
       AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             USING(code)--ON countries.code = economies.code
             WHERE year = 2015) AS subquery
           GROUP BY continent);
 
   
    
    

MORE SUBQUERY EXAMPLES

-- Select fields
SELECT code, inflation_rate, unemployment_rate
  -- From economies
  FROM economies
  -- Where year is 2015 and code is not in
  WHERE year = 2015 AND code NOT IN
  	-- Subquery
  	(SELECT code
  	 FROM countries
  	 WHERE (gov_form = 'Constitutional Monarchy' OR gov_form LIKE '%Republic%'))
-- Order by inflation rate
ORDER BY inflation_rate;
    
    
    

SELECT DISTINCT c.name, e.total_investment, e.imports
  FROM countries AS c
    LEFT JOIN economies AS e
      ON (c.code = e.code
        AND c.code IN (
          SELECT l.code
          FROM languages AS l
          WHERE official = 'true'
        ) )
  WHERE region = 'Central America' AND year = 2015
ORDER BY name;




SELECT name, country_code, city_proper_pop, metroarea_pop,
	  -- Calculate city_perc
      city_proper_pop / metroarea_pop * 100 AS city_perc
   FROM cities
   WHERE name IN
     (SELECT capital
     FROM countries
     WHERE (continent = 'Europe'
        OR continent LIKE '%America'))
       AND metroarea_pop IS NOT NULL
ORDER BY city_perc DESC
LIMIT 10;




REMOVING MISSING VALUES

-- Return the specified columns
SELECT IncidentDateTime, IncidentState
FROM Incidents
-- Exclude all the missing values from IncidentState  
WHERE IncidentState IS NOT NULL;

IMPUTING MISSING VALUES

-- Check the IncidentState column for missing values and replace them with the City column
SELECT IncidentState, ISNULL(IncidentState, City) AS Location
FROM Incidents
-- Filter to only return missing values from IncidentState
WHERE IncidentState IS NULL


-- Replace missing values in Country with the first non-missing value from IncidentState or City or 'Unknown'
SELECT Country, COALESCE(IncidentState, City, 'Unknown') AS Location
FROM Incidents
WHERE Country IS NULL



COUNTING THE NUMBER OF DAYS BETWEEN DATES

"""
year, yyyy, yy = Year
quarter, qq, q = Quarter
month, mm, m = month
dayofyear = Day of the year
day, dy, y = Day
week, ww, wk = Week
weekday, dw, w = Weekday
hour, hh = hour
minute, mi, n = Minute
second, ss, s = Second
millisecond, ms = Millisecond

"""

-- Return the difference in OrderDate and ShipDate
SELECT OrderDate, ShipDate, 
       DATEDIFF(y, OrderDate, ShipDate) AS Duration
FROM Shipments



ADDING DAYS TO A DATE

-- Return the DeliveryDate as 5 days after the ShipDate
SELECT OrderDate, 
       DATEADD(y, 5, ShipDate) AS DeliveryDate
FROM Shipments


-- Round Cost to the nearest dollar
SELECT Cost, 
       ROUND(Cost,0) AS RoundedCost
FROM Shipments



ABSOLUTE VALUES, SQUARES, AND SQUARE ROOT

SELECT DeliveryWeight,
       ABS(DeliveryWeight) AS AbsoluteValue
FROM Shipments

SELECT WeightValue, 
       SQUARE(WeightValue) AS WeightSquare, 
       SQRT(WeightValue) AS WeightSqrt
FROM Shipments


CREATING AND USING VARIABLES

-- Declare the variable (a SQL Command, the var name, the datatype)
DECLARE @counter INT 

-- Set the counter to 20
SET @counter = 20

-- Select the counter
SELECT @counter



CREATING A WHILE LOOP

DECLARE @counter INT 
SET @counter = 20

-- Create a loop
WHILE @counter < 30

-- Loop code starting point
BEGIN
	SELECT @counter = @counter + 1
-- Loop finish
END

-- Check the value of the variable
SELECT @counter



QUERIES WITH DERIVED TABLES

SELECT a.RecordId, a.Age, a.BloodGlucoseRandom, 
-- Select maximum glucose value (use colname from derived table)    
       b.MaxGlucose
FROM Kidney a
-- Join to derived table
JOIN (SELECT Age, MAX(BloodGlucoseRandom) AS MaxGlucose FROM Kidney GROUP BY Age) b
-- Join on Age
ON a.Age = b.Age




CREATING A CTE

-- Specify the keyowrds to create the CTE
WITH BloodGlucoseRandom -- This creates a table out the same table that can be used in the following query
AS (SELECT MAX(BloodGlucoseRandom) AS MaxGlucose FROM Kidney)

SELECT a.Age, b.MaxGlucose
FROM Kidney a
-- Join the CTE on blood glucose equal to max blood glucose
JOIN BloodGlucoseRandom b
ON a.BloodGlucoseRandom = b.MaxGlucose;


-- Create the CTE
WITH BloodPressure
AS (SELECT MAX(BloodPressure) AS MaxBloodPressure
FROM kidney b) -- This creates a table out of the same that can be used in the following query

SELECT *
FROM Kidney a
-- Join the CTE  
JOIN  BloodPressure AS b
ON a.BloodPressure = b.MaxBloodPressure;



WINDOWS FUNCTIONS WITH AGGREGATIONS

SELECT OrderID, TerritoryName, 
       -- Total price for each partition
        SUM(OrderPrice) OVER(PARTITION BY TerritoryName) AS TotalPrice -- OVER creates a window for the entire table 
       -- Create the window and partitions
       
FROM Orders



SELECT OrderID, TerritoryName, 
       -- Number of rows per partition
       COUNT(OrderPrice) 
       -- Create the window and partitions
       OVER(PARTITION BY TerritoryName) AS TotalOrders
FROM Orders






WINDOWS FUNCTIONS
LEAD(), LAG(), FIRST_VALUE(), and LAST_VALUE()



FIRST VALUE IN A WINDOW

SELECT TerritoryName, OrderDate, 
       -- Select the first value in each partition
       FIRST_VALUE(OrderDate) 
       -- Create the partitions and arrange the rows
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS FirstOrder
FROM Orders



PREVIOUS AND NEXT VALUES

SELECT TerritoryName, OrderDate, 
       -- Specify the previous OrderDate in the window
       LAG(OrderDate) 
       -- Over the window, partition by territory & order by order date
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS PreviousOrder,
       -- Specify the next OrderDate in the window
       LEAD(OrderDate) 
       -- Create the partitions and arrange the rows
       OVER(PARTITION BY OrderDate ORDER BY OrderDate) AS NextOrder
FROM Orders




CREATING RUNNING TOTALS

SELECT TerritoryName, OrderDate, 
       -- Create a running total
       SUM(OrderPrice)
       -- Create the partitions and arrange the rows
       -- Create the running total by ordering by a column that has a different value for each row
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS TerritoryTotal	  
FROM Orders




ASSIGNING ROW NUMBERS

SELECT TerritoryName, OrderDate, 
       -- Assign a row number
       ROW_NUMBER()
       -- ORDER BY in the OVER clause is required when using ROW_NUMBER()
       -- Create the partitions and arrange the rows
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS OrderCount
FROM Orders



CALCULATING STANDARD DEVIATION

SELECT OrderDate, TerritoryName, 
       -- Calculate the standard deviation
	   STDEV(OrderPrice) 
       OVER() AS StdDevPrice	  
FROM Orders


# calculation of the running standard deviation

SELECT OrderDate, TerritoryName, 
       -- Calculate the standard deviation
	   STDEV(OrderPrice) 
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS StdDevPrice	  
FROM Orders




CALCULATING MODE

-- Create a CTE Called ModePrice which contains two columns
 WITH ModePrice AS 
(
	SELECT OrderPrice, 
	ROW_NUMBER() 
	OVER(PARTITION BY OrderPrice ORDER BY OrderPrice) AS UnitPriceFrequency
	FROM Orders 
)
'''
USING ROW_NUMBER IS THE KEY TO GETTING A COUNT OF THE PARTITIONED ROWS TO THEN
CALCULATE THE MODE OF THE DATA
'''
SELECT OrderPrice AS ModeOrderPrice
FROM ModePrice
-- Select the maximum UnitPriceFrequency from the CTE
WHERE UnitPriceFrequency IN (SELECT MAX(UnitPriceFrequency) FROM ModePrice);






-- Select the count of profits_change, 
-- subtract from total number of rows, and alias as missing
SELECT COUNT(*) - COUNT(profits_change) as missing
FROM fortune500;

-- Use coalescee for specifying a default or backup
-- value when a column contains NULL values.
SELECT COALESCE(industry, sector, 'Unknown') AS industry2,
       COUNT(*) AS count
 FROM fortune500 
 GROUP BY industry2
 ORDER BY count DESC
 LIMIT 1;


--using coalesce with a series of joins
SELECT company_original.name, title, rank
    FROM company AS company_original
       	   LEFT JOIN company AS company_parent
       ON company_original.parent_id = company_parent.id 
           INNER JOIN fortune500 
              ON coalesce(company_parent.ticker, 
                 company_original.ticker) = 
                 fortune500.ticker
           ORDER BY rank; 
           
 
TWO WAYS TO CAST DATA TYPE OF A SQL COLUMN
       
-- Select the original value
SELECT profits_change, 
	   -- Cast profits_change
       CAST(profits_change AS integer) AS profits_change_int
  FROM fortune500;
  
-- Select the count of each revenues_change integer value
SELECT revenues_change::integer AS int_revenue, COUNT(*)
  FROM fortune500
 GROUP BY int_revenue
 -- order by the values of revenues_change
 ORDER BY int_revenue;
 
TO EXAMINE THE DATA TYPES OF YOUR SQL TABLE COLUMNS BEFORE DATA ANALYSIS

SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'yourTableName'
 


  -- Select average revenue per employee by sector
SELECT sector, 
       AVG(revenues/employees::numeric) AS avg_rev_employee
 FROM fortune500
 GROUP BY sector
 -- Use the column alias to order the results
 ORDER BY avg_rev_employee;
 
 -- INCORPORATING STACKOVERFLOW INTO A QUERY
SELECT unanswered_count/question_count::numeric AS computed_pct, 
  unanswered_pct
  FROM stackoverflow
  WHERE question_count != 0 
  LIMIT 10;
  
  
DISPLAY AGGREGATE VALUES OF THE GROUPED TAGS IN THE SUBQUERY

SELECT min(maxval),
	   -- min
       max(maxval),
       -- max
       avg(maxval),
       -- avg
       stddev(maxval)
  -- Subquery to compute max of question_count by tag
  FROM (SELECT max(question_count) AS maxval, tag
        FROM stackoverflow
        GROUP BY tag) AS max_results;
        

-- Truncate employees of fortune 500 companies into bins of 100000
SELECT trunc(employees, -5) AS employee_bin,
       -- Count number of companies with each truncated value
       COUNT(title)
  FROM fortune500
  GROUP BY employee_bin
  ORDER BY employee_bin;
  
SAME AS ABOVE BUT with BINS OF 10000 UP TO 99999
-- Truncate employees
SELECT trunc(employees, -4) AS employee_bin,
       -- Count number of companies with each truncated value
       COUNT(title)
  FROM fortune500
 -- Limit to which companies?
 WHERE employees < 100000
 -- Use alias to group
 GROUP BY employee_bin
 -- Use alias to order
 ORDER BY employee_bin;
 
 
 
 
 
USING COMMON TABLE EXPRESSIONS TO SIMPLIFY THE JOINS

USING generate_series for two sets of bounding numbers for grouping a count
WITH bins AS (
      SELECT generate_series(2200, 3050, 50) AS lower,
             generate_series(2250, 3100, 50) AS upper),
     -- Subset stackoverflow to just tag dropbox (Step 1)
     dropbox AS (
      SELECT question_count 
        FROM stackoverflow
       WHERE tag='dropbox') 
-- Select columns for result
-- What column are you counting to summarize?
SELECT lower, upper, count(question_count) 
  FROM bins  -- Created above
       -- Join to dropbox (created above), 
       -- keeping all rows from the bins table in the join
       LEFT JOIN dropbox
       -- Compare question_count to lower and upper
         ON lower <= question_count 
         AND upper > question_count
        
 -- Group by lower and upper to count values in each bin
 GROUP BY lower, upper
 -- Order by lower to put bins in order
 ORDER BY lower;
 
 
 

 
 -- What groups are you computing statistics by?
SELECT sector,
       -- Select the mean of assets with the avg function
       AVG(assets) AS mean,
       -- Select the median
       percentile_disc(0.5) WITHIN GROUP (ORDER BY assets) AS median
  FROM fortune500
  GROUP BY sector
  ORDER BY mean;
  
  
  
  

INTERMEDIATE DATA PROCESSING WITH A TEMP TABLE

DROP TABLE IF EXISTS profit80;

CREATE TEMP TABLE profit80 AS
  SELECT sector, 
         percentile_disc(0.8) WITHIN GROUP (ORDER BY profits) AS pct80
    FROM fortune500 
   GROUP BY sector;

-- Select columns, aliasing as needed
SELECT title, fortune500.sector, 
       profits, profits/pct80 AS ratio
-- What tables do you need to join?  
  FROM fortune500 
       LEFT JOIN profit80
-- How are the tables joined?
       ON fortune500.sector=profit80.sector
-- What rows do you want to select?
 WHERE profits > pct80;
 
 
 
 
SELECTING FROM A TEMP TABLE
USING SELF AND INNNER JOINS

-- To clear table if it already exists
DROP TABLE IF EXISTS startdates;

CREATE TEMP TABLE startdates AS
SELECT tag, min(date) AS mindate
  FROM stackoverflow
 GROUP BY tag;
 
-- Select tag (Remember the table name!) and mindate
SELECT startdates.tag, 
       mindate, 
       -- Select question count on the min and max days
	   so_min.question_count AS min_date_question_count,
       so_max.question_count AS max_date_question_count,
       -- Compute the change in question_count (max- min)
       so_max.question_count - so_min.question_count AS change
  FROM startdates
       -- Join startdates to stackoverflow with alias so_min
       INNER JOIN stackoverflow AS so_min
          -- tag and min_date need to match between tables
          ON startdates.tag = so_min.tag
         AND startdates.mindate = so_min.date
       -- Join to stackoverflow again with alias so_max
       INNER JOIN stackoverflow AS so_max
          -- tag and a date need to match between tables
          ON startdates.tag = so_max.tag
         AND so_max.date = '2018-09-25';
 
    
    
    

DROP TABLE IF EXISTS correlations;

CREATE TEMP TABLE correlations AS
SELECT 'profits'::varchar AS measure,
       corr(profits, profits) AS profits,
       corr(profits, profits_change) AS profits_change,
       corr(profits, revenues_change) AS revenues_change
  FROM fortune500;

INSERT INTO correlations
SELECT 'profits_change'::varchar AS measure,
       corr(profits_change, profits) AS profits,
       corr(profits_change, profits_change) AS profits_change,
       corr(profits_change, revenues_change) AS revenues_change
  FROM fortune500;

INSERT INTO correlations
SELECT 'revenues_change'::varchar AS measure,
       corr(revenues_change, profits) AS profits,
       corr(revenues_change, profits_change) AS profits_change,
       corr(revenues_change, revenues_change) AS revenues_change
  FROM fortune500;

-- Select each column, rounding the correlations
SELECT measure, 
       round(profits::numeric, 2) AS profits,
       round(profits_change::numeric, 2) AS profits_change,
       round(revenues_change::numeric, 2) AS revenues_change
  FROM correlations;
  
  
  
  
USING TRIM FUNCTION
  
SELECT distinct street,
       -- Trim off unwanted characters from street
       trim(street, '0123456789 #/.' ) AS cleaned_street
  FROM evanston311
 ORDER BY street;
 

 USING LIKE, ILIKE, AND NOT LIKE
 
-- Count rows with each category
SELECT category, count(*)
  FROM evanston311 
 WHERE (description LIKE '%trash%'
    OR description ILIKE '%garbage%') 
   AND category NOT LIKE '%Trash%'
   AND category NOT LIKE '%Garbage%'
 -- What are you counting?
 GROUP BY category
 --- order by most frequent values
 ORDER BY count DESC
 LIMIT 10;
 
 
 
 RTRIM USED WITH CONCAT
 
 -- Concatenate house_num, a space, and street
-- and trim spaces from the start of the result
SELECT rtrim(concat(house_num, ' ', street)) AS address
  FROM evanston311;
  

USING SPLIT_PART

-- Select the first word of the street value
SELECT split_part(street, ' ', 1) AS street_name, 
       count(*)
  FROM evanston311
 GROUP BY street_name
 ORDER BY count DESC
 LIMIT 20;
 
 
 USING LEFT, SPLIT_PART AND CONCAT(||) WITH A CASE STATEMENT
 
 -- Select the first 50 chars when length is greater than 50
SELECT CASE WHEN length(description) > 50
            THEN left(description, 50) || '...'
       -- otherwise just select description
       ELSE description
       END
  FROM evanston311
 -- limit to descriptions that start with the word I
 WHERE split_part(description, ' ', 1) LIKE 'I'
 ORDER BY description;
 
 
 

USING TEMP TABLE WITH JOIN AND MULTIPLE TRANSFORMATIONS

-- Code from previous step
DROP TABLE IF EXISTS recode;
CREATE TEMP TABLE recode AS
  SELECT DISTINCT category, 
         rtrim(split_part(category, '-', 1)) AS standardized
  FROM evanston311;
  
  
UPDATE recode SET standardized='Trash Cart' 
 WHERE standardized LIKE 'Trash%Cart';
UPDATE recode SET standardized='Snow Removal' 
 WHERE standardized LIKE 'Snow%Removal%';
UPDATE recode SET standardized='UNUSED' 
 WHERE standardized IN ('THIS REQUEST IS INACTIVE...Trash Cart', 
               '(DO NOT USE) Water Bill',
               'DO NOT USE Trash', 'NO LONGER IN USE');

-- Select the recoded categories and the count of each
SELECT standardized, COUNT(*)
-- From the original table and table with recoded values
  FROM evanston311
       LEFT JOIN recode 
       -- What column do they have in common?
       ON evanston311.category = recode.category
 -- What do you need to group by to count?
 GROUP BY standardized
 -- Display the most common val values first
 ORDER BY count(standardized) DESC;
 
 
 
 
 
 
ADDING CASTING AND AGGREGATE FUNCTIONS TO ABOVE
 
-- To clear table if it already exists
DROP TABLE IF EXISTS indicators;

-- Create the temp table
CREATE TEMP TABLE indicators AS
  SELECT id, 
         CAST (description LIKE '%@%' AS integer) AS email,
         CAST (description LIKE '%___-___-____%' AS integer) AS phone 
    FROM evanston311;
  
-- Select the column you'll group by
SELECT priority, 
       -- Compute the proportion of rows with each indicator
  sum(email)/count(email)::numeric AS email_prop, 
  sum(phone)/count(phone)::numeric AS phone_prop
  -- Tables to select from
  FROM evanston311
       LEFT JOIN indicators
       -- Joining condition
       ON evanston311.id =indicators.id
 -- What are you grouping by?
 GROUP BY priority;
 
 

COMBINING CASTING WITH A SUBQUERY, GENERATE SERIES AND JOIN

-- Count number of requests made per day
SELECT daily_series.day, count(id) AS count
-- Use a daily series from 2016-01-01 to 2018-06-30 
-- to include days with no requests
  FROM (SELECT generate_series('2016-01-01',  -- series start date
                               '2018-06-30',  -- series end date
                               '1 day'::interval)::date AS day) AS daily_series
       LEFT JOIN evanston311
       -- match day from above (which is a date) to date_created
       ON daily_series.day = date_created::date
 GROUP BY daily_series.day
 ORDER BY count DESC;
 
 
 

USING DATES, TIMESTAMPS, AND TIME ZONES

-- Count requests created on January 31, 2017
SELECT count(*) 
  FROM evanston311
 WHERE date_created:: date = 'January 31, 2017';
 
-- Subtract the min date_created from the max
SELECT max(date_created) - min(date_created)
  FROM evanston311;
  


-- Select the category and the average completion time by category
SELECT category, 
       AVG(date_completed - date_created) AS completion_time
  FROM evanston311
 Group by category
-- Order the results
 Order by completion_time Desc;
 
 
 
 USING EXTRACT
 
 -- Extract the month from date_created and count requests
SELECT EXTRACT(MONTH FROM date_created) AS month, 
    count(id)   
  FROM evanston311
 -- Limit the date range
 WHERE date_created >= '2016-01-01'
   AND date_created < '2018-01-01'
 -- Group by what to get monthly counts?
 GROUP BY month;
 
 
 USING DATE_PART
 
 -- Get the hour and count requests
SELECT date_part('hour', date_created) AS hour,
       count(*)
  FROM evanston311
 GROUP BY hour
 -- Order results to select most common
 ORDER BY count DESC
 LIMIT 1;
 
 
 
 USING TO_CHAR FOR NAMES AND DOW FOR INTEGER VALUES
-- Select name of the day of the week the request was created 
SELECT to_char(date_created, 'day') AS day, 
       -- Select avg time between request creation and completion
       avg(date_completed - date_created) AS duration 
  FROM evanston311 
 -- Group by the name of the day of the week and 
 -- integer value of day of week the request was created
 GROUP BY day, EXTRACT(DOW FROM date_created) 
 -- Order by integer value of the day of the week 
 -- the request was created
 ORDER BY EXTRACT(DOW FROM date_created);
 
 
USING DATE TRUNCATION

-- Aggregate daily counts by month
SELECT date_trunc('month', day) AS month,
       avg(count)
  -- Subquery to compute daily counts
  FROM (SELECT date_trunc('day', date_created) AS day,
               count(*) AS count
          FROM evanston311
         GROUP BY day) AS daily_count
 GROUP BY month
 ORDER BY month;
 
 
 
 FINDING MISSING DATES WITH GENERATE_SERIES AND SUBQUERIES
 
 SELECT day
-- 1) Subquery to generate all dates
-- from min to max date_created
  FROM (SELECT generate_series(min(date_created),
                               max(date_created),
                               '1 day'::interval)::date AS day
          -- What table is date_created in?
          FROM evanston311) AS all_dates      
-- 4) Select dates (day from above) that are NOT IN the subquery
 WHERE day NOT IN 
       -- 2) Subquery to select all date_created values as dates
       (SELECT date_created::date
          FROM evanston311);
        
        
USE GENERATE_SERIES TO AGGREGATE DATA BY NON-STANDARD DATE/TIME INTERVALS, SUCH AS SIX MONTHS


-- cte of 6 month bounded generate_series
WITH bins AS (
	 SELECT generate_series('2016-01-01',
                            '2018-01-01',
                            '6 months'::interval) AS lower,
            generate_series('2016-07-01',
                            '2018-07-01',
                            '6 months'::interval) AS upper),

-- cte of 1 day interval generate_series with left join
     daily_counts AS (
     SELECT daily_series.day, count(date_created) AS count
       FROM (SELECT generate_series('2016-01-01',
                                    '2018-06-30',
                                    '1 day'::interval)::date AS day) AS daily_series
            LEFT JOIN evanston311
            ON daily_series.day = date_created::date
      GROUP BY daily_series.day)
-- Select bin bounds
SELECT lower, 
       upper, 
       -- Compute median of count for each bin
       percentile_disc(0.5) WITHIN GROUP (ORDER BY count) AS median
  -- Join bins and daily_counts
  FROM bins
       LEFT JOIN daily_counts
       -- Where the day is between the bin bounds
       ON day >= lower
          AND day < upper
 -- Group by bin bounds
 GROUP BY lower, upper
 ORDER BY lower;
 
 
 
 
CREATING MONTHLY AVERAGES PER DAY WITH MISSING DATES
 
 -- generate series with all days from 2016-01-01 to 2018-06-30
WITH all_days AS 
     (SELECT generate_series('2016-01-01',
                             '2018-06-30',
                             '1 day'::interval) AS date),
     -- Subquery to compute daily counts
     daily_count AS 
     (SELECT date_trunc('day', date_created) AS day,
             count(*) AS count
        FROM evanston311
       GROUP BY day)
-- Aggregate daily counts by month using date_trunc
SELECT date_trunc('month', date) AS month,
       -- Use coalesce to replace NULL count values with 0
       avg(coalesce(count, 0)) AS average
  FROM all_days
       LEFT JOIN daily_count
       -- Joining condition
       ON all_days.date=daily_count.day
 GROUP BY month
 ORDER BY month; 
 
 
 
 
USING LAG AND LEAD

-- Compute the gaps using a cte
WITH request_gaps AS (
        SELECT date_created,
               -- lead or lag
               lag(date_created) OVER (ORDER BY date_created) AS previous,
               -- compute gap as date_created minus lead or lag
               date_created - lag(date_created) OVER (ORDER BY date_created) AS gap
          FROM evanston311)
-- Select the row with the maximum gap
SELECT *
  FROM request_gaps
-- Subquery to select maximum gap from request_gaps
 WHERE gap = (SELECT max(gap) 
                FROM request_gaps);


















