
import mysql.connector
import pandas as pd
import  streamlit as st
connn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kannadi@123",
    database="sakthi")
st.markdown("""
    <style>

        .stApp {
            background-color:  #FFB6C1;  
        }


    </style>
""", unsafe_allow_html=True)
myquery3=connn.cursor()
r=st.sidebar.selectbox("Select_The_Tabs",['About','Query_1_to_10','Query_11_to_20'])
if r == "About":
    st.title("Hello Teammates I am kannan")
    st.markdown("""
    :moon:
    ## Description :

    """)
    st.title("BookScape Explorer")
    st.snow()
    st.markdown("""


    ### PROBLEM STATEMENT :
    ### OBJECTIVE:
    The BookScape Explorer project aims to facilitate users in discovering and analyzing book data through a web application. 
    The application will extract data from online book APIs, store this information in a SQL database, and enable data analysis using SQL queries
    ### GOALS:
    The project will provide insights into book trends, user preferences, and reviews.
    Helping users make informed reading choices while also offering a platform for community engagement. 
    ### MENTOR :
    ### Mrs.GOMATHI ,Mrs.SHADIYA.
    ### Mrs.NEHLATH HARMAIN,Mr.ASVIN

    """)
    st.balloons()
    st.success("ONCE AGAIN THANKYOU GUVI")
if r=="Query_1_to_10":
    r1 = st.sidebar.radio("Queries", ['Query1', 'Query2', 'Query3', 'Query4', "Query5", "Query6","Query7","Query8","Query9","Query10"])
    if r1=='Query10':
        st.snow()
        myquery3.execute("select max(averageRating)as HighestAverageRating ,publisher from correct2 group by publisher having  max(averageRating)>4.5")
        data=myquery3.fetchall()
        st.title("Identify the Publisher with the Highest Average Rating")
        df=pd.DataFrame(data,columns=myquery3.column_names)
        st.dataframe(df)
    if r1=='Query2':
        st.balloons()
        myquery3.execute("select max(amount_retailPrice) as RetailPrice,book_title as FiveMostExpensiveBooks from correct2 group by  book_title having max(amount_retailPrice)>14000 order by max(amount_retailPrice) desc")
        data=myquery3.fetchall()
        st.title("Get the Top  Most Expensive Books by Retail Price")
        df=pd.DataFrame(data,columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query3':
        st.snow()
        myquery3.execute("select authors,count(book_title) from correct2 group by authors having count(book_title)>=6 limit 3;")
        data = myquery3.fetchall()
        st.title("Find the Top 3 Authors with the Most Books")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query4':
        st.snow()
        myquery3.execute("select publisher,count(book_title) from correct2 group by publisher having count(book_title)>=10 ")
        data = myquery3.fetchall()
        st.title("List Publishers with More than 10 Books")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query5':
        st.snow()
        myquery3.execute(
            "select book_title,count(authors) from correct2 group by book_title  having count(authors)>3")
        data = myquery3.fetchall()
        st.title("Retrieve Books with More than 3 Authors")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query6':
        st.balloons()
        myquery3.execute(
            " select book_title,count(ratingscount) from correct2 group by book_title having count(ratingscount)>avg(ratingscount)")
        data = myquery3.fetchall()
        st.title("Books with Ratings Count Greater Than the Average")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query7':
        st.snow()
        myquery3.execute(
            " select year, max(amount_listPrice) as Highestaveragebookprice from correct2 group by year order by max(amount_listPrice) desc")
        data = myquery3.fetchall()
        st.title("Year with the Highest Average Book Price")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query8':
        st.balloons()
        myquery3.execute(
            "select book_title as specifickeyword from correct2  where book_title like  '%Maths%'")
        data = myquery3.fetchall()
        st.title("Books with a Specific Keyword in the Title")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query9':
        st.snow()
        myquery3.execute(
            "select max(pageCount) as pages  ,year from correct2  group by year having max(pageCount)>700 and year>2010 order by year asc")
        data = myquery3.fetchall()
        st.title("Find Books Published After 2010 with at Least 500 Pages")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r1 == 'Query1':
        st.balloons()
        myquery3.execute(
            "SELECT book_title, CASE WHEN isEbook = '1' THEN 'ebook' ELSE 'physical' END as ebook_stats FROM correct2")
        data = myquery3.fetchall()
        st.title("Check Availability of eBooks vs Physical Books")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
if r=="Query_11_to_20":
    r2=st.sidebar.radio("Queries",['Query11',"Query12","Query13","Query14","Query15","Query16","Query17","Query18","Query19","Query20"])
    if r2 == 'Query11':
        st.balloons()
        myquery3.execute(
            "select avg(pageCount) as Averagepagecout, case when isEbook='1' then 'ebook' else 'physical' end  as ebook_status  from correct2 group by isEbook")
        data = myquery3.fetchall()
        st.title("Find the Average Page Count for eBooks vs Physical Books")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query12':
        st.snow()
        myquery3.execute(
            "SELECT book_title,authors,Group_CONCAt(year) AS years FROM correct2 GROUP BY authors,book_title ")
        data = myquery3.fetchall()
        st.title("Books with the Same Author Published in the Same Year")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2== 'Query13':
        st.balloons()
        myquery3.execute(
            " SELECT authors, "
            "year AS year1, "
            "year + 1 AS year2, "
            "year + 2 AS year "
            "FROM correct2 "
            "where year between 2015 and 2024 "
            "GROUP BY authors, year "
            "HAVING COUNT(DISTINCT year) = 1 "
            "ORDER BY authors, year")

        data = myquery3.fetchall()
        st.title("Count Authors Who Published 3 Consecutive Years")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query14':
        st.snow()
        myquery3.execute(
            "select publisher,count(book_title)as book_published from correct2 group by publisher having count(book_title)>8")
        data = myquery3.fetchall()
        st.title("Find the Publisher with the Most Books Published")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query15':
        st.balloons()
        myquery3.execute(
            "select book_title ,((amount_listPrice-amount_retailPrice)/amount_listprice)*100  as discount from correct2 having discount>20 order by discount desc")
        data = myquery3.fetchall()
        st.title("List Books with Discounts Greater than 20%")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query16':
        st.snow()
        myquery3.execute(
            "select authors,publisher,Group_Concat( year order by year) as year,count(book_title)as count  from correct2 group by authors,publisher")
        data = myquery3.fetchall()
        st.title("Write a SQL query to find authors who have published books in the same year but under different publishers" 
                   "Return the authors, year, and the COUNT of books they published in that year.")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query17':
        st.balloons()
        myquery3.execute(
            "select avg(amount_retailPrice)as AverageAmountRetailPrice,case when isEbook='1' then 'ebook' else 'physical' end as AvgEbookPrice_AvgPhysicalPrice from correct2 group by isEbook")
        data = myquery3.fetchall()
        st.title("Create a query to find the average amount_retailPrice of eBooks and physical books"
                   "Return a single result set with columns for avg_ebook_price and avg_physical_price"
                    "Ensure to handle cases where either category may have no entries")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query18':
        st.balloons()
        myquery3.execute(
            "select publisher ,count(book_title),max(averageRating) from correct2 group by publisher having count(book_title)>10 and   max(averageRating)>4.5  ")
        data = myquery3.fetchall()
        st.title("Create a SQL query that determines which publisher has the highest average rating among its books" 
                 "but only for publishers that have published more than 10 books" 
                  "Return the publisher, average_rating, and the number of books published")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query19':
        st.snow()
        myquery3.execute(
            "SELECT book_title,averageRating,ratingsCount FROM correct2 WHERE averageRating > (SELECT AVG(averageRating) FROM correct2) + 2 * (SELECT STDDEV(averageRating) FROM correct2)")
        data = myquery3.fetchall()
        st.title("Write a SQL query to identify books that have an averageRating that is more than two standard deviations away from the average rating of all books" 
                     "Return the title, averageRating, and ratingsCount for these outliers.")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)
    if r2 == 'Query20':
        st.balloons()
        myquery3.execute("""
            SELECT 
                CASE
                    WHEN pageCount < 100 THEN 'Short'
                    WHEN pageCount BETWEEN 100 AND 300 THEN 'Medium'
                    WHEN pageCount > 300 THEN 'Long'
                END AS category,
                AVG(pageCount) AS avg_page_count
            FROM correct2
            GROUP BY category
        """)
        data = myquery3.fetchall()
        st.title("   Find the Average Page Count for Each Category ")
        df = pd.DataFrame(data, columns=myquery3.column_names)
        st.dataframe(df)













