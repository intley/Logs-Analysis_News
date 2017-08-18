# Logs Analysis Project
This project aims to provide practice interacting with a live database with over a million rows. By exploring the database, we are tasked to build and refine complex queries and use them to draw business conclusions from data.

## Questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started
#### Pre-requisites:
- [Python 2/3](https://www.python.org/)
- [Vagrant](https://www.vagrantup.com/)
- [Virtual Box](https://www.virtualbox.org/)

#### Configuration:
1. Make sure you have a command-line terminal installed on your system such as GitBash or the Terminal application on macOS.
2. Install Vagrant and Virtualbox.
3. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
4. Download the news database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
5. Unzip the file and move the newsdata.sql file into the vagrant folder.

#### Launching Vagrant:
1. To launch vagrant, navigate to the fullstack-nanodegree-vm folder and inside this folder, VagrantFile.
2. Once you are in the VagrantFile directory, you can start the virtual machine using the command:
```
vagrant up
```
3. Proceed to launch the VM using the following command:
```
vagrant ssh
```
And now change directory to the vagrant folder:
```
cd /vagrant
```
4. You should have the newsdata.sql file in this folder. You may check using the ls command. If the file is not present, move the file into this folder.

#### Loading the Database:
1. Load the News Database using the following command:
```
psql -d -f newsdata.sql
```
2. Use the following command to connect to the database:
```
psql -d news
```
You can now run PostgreSQL queries on this database.

#### PostgreSQL Documentation:
The Documentation for PostgreSQL can be found [here](https://www.postgresql.org/docs/9.6/static/index.html).

## Tables within the Database:
There are three tables within the News Database:
1. articles
2. authors
3. log

You can use the following command to know the contents of a table:
```
\d tablename
```

## Creating Views:
1. This View was created to compute the top three-most popular articles on the basis of views:
```
CREATE VIEW top_three_articles AS
SELECT a.title AS title, count(*) AS views
FROM articles AS a, log AS l
WHERE l.path LIKE CONCAT('%', a.slug)
GROUP BY a.title
ORDER BY views DESC
LIMIT 3;
```

2. This View was created to compute the most popular authors of all time based on the number of views for the articles written by them:
```
CREATE VIEW top_authors AS
SELECT au.name AS name, count(*) AS views
FROM articles AS a, log AS l, authors AS au
WHERE au.id=a.author AND l.path LIKE CONCAT('%', a.slug)
GROUP BY name
ORDER BY views DESC;
```

3. This View was created to compute the total requests grouped by a given date:
```
CREATE VIEW total_requests AS
SELECT time::date AS date, count(*) AS views
FROM log
GROUP BY date
ORDER BY date;
```

4. This View was created to compute the error requests grouped by a given date:
```
CREATE VIEW error_requests AS
SELECT time::date AS date, count(*) AS views
FROM log
WHERE status!= '200 OK'
GROUP BY date
ORDER BY date;
```

5. This view was created to compute the error percent for a given date in the log.
```
CREATE VIEW error_rate AS
SELECT tr.date, (100.0*er.views/tr.views) AS percent
FROM total_requests as tr, error_requests as er
WHERE tr.date=er.date
ORDER BY tr.date;
```

#### Running the python file to view results of the queries:
The python file can be run in Python version-2 or version-3 as follows:
```
python3 newsdb.py
```  
OR
```
python2 newsdb.py
```
