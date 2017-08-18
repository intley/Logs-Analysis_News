#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

question1 = "What are the three most popular articles of all time?"
question2 = "Who are the most popular article authors of all time?"
question3 = "On which days did more than 1 percent of requests lead to errors?"


def top_articles():
    """
    This function connects to the news database and computes the query
    to find the three most popular articles.
    """

    # Connects to the news database and creates a cursor
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Question 1
    print("_" * 75)
    print(question1)
    query1 = """
    SELECT *
    FROM top_three_articles;
    """
    c.execute(query1)
    ans1 = c.fetchall()
    for(title, views) in ans1:
        print("\n {}    -   {}".format(title, views))
    print("-" * 75)

    # Closing DB Connection
    db.close()


def top_authors():
    """
    This function connects to the news database and computes the query
    to find the authors with the most popular articles.
    """

    # Connects to the news database and creates a cursor
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Question 2
    print(question2)
    query2 = """
    SELECT *
    FROM top_authors;
    """
    c.execute(query2)
    ans2 = c.fetchall()
    for(name, views) in ans2:
        print("\n {}    -   {}".format(name, views))
    print("-" * 75)

    # Closing DB Connection
    db.close()


def error_rate():
    """
    This function connects to the news database and computes the query to
    find the date where the error rate is greater than 1 percent.
    """

    # Connects to the news database and creates a cursor
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Question 3
    print(question3)
    query3 = """
    SELECT *
    FROM error_rate
    WHERE percent > 1;
    """
    c.execute(query3)
    ans3 = c.fetchall()
    for(date, percent) in ans3:
        print("\n {}    -   {}".format(date, percent))
    print("-" * 75)

    # Closing DB Connection
    db.close()


if __name__ == "__main__":
    top_articles()
    top_authors()
    error_rate()
