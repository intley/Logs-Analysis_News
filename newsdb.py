#Database Code running queries on the News Database
import psycopg2

DBNAME = "news"

question1="What are the three most popular articles of all time?"
question2="Who are the most popular article authors of all time?"
question3="On which days did more than 1 percent of requests lead to errors?"

def run_query():
    """This function connects to the news database and runs the three
    queries to display the details for the questions asked.
    """
    #Connects to the news database and creates a cursor
    db=psycopg2.connect(database=DBNAME)
    c=db.cursor()

    #Question 1
    print("_" * 75)
    print(question1)
    query1="""
    SELECT *
    FROM top_three_articles;
    """
    c.execute(query1)
    ans1=c.fetchall()
    for(title,views) in ans1:
        print("\n {}    -   {}".format(title,views))
    print("_" * 75)

    #Question 2
    print(question2)
    query2="""
    SELECT *
    FROM top_authors;
    """
    c.execute(query2)
    ans2=c.fetchall()
    for(name,views) in ans2:
        print("\n {}    -   {}".format(name,views))
    print("_" * 75)

    #Question 3
    print(question3)
    query3="""
    SELECT *
    FROM error_rate
    WHERE percent > 1;
    """
    c.execute(query3)
    ans3=c.fetchall()
    for(date, percent) in ans3:
        print("\n {}    -   {}".format(date,percent))
    print("_" * 75)

    #Closing DB Connection
    db.close()

run_query()
