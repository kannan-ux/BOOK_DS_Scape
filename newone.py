import mysql.connector
import streamlit as st
import pandas as pd
import requests
import sqlite3
def str_to_int(x):
    if x != None:
        try:
            int_value = int(x)
            return int_value
        except ValueError:
            return None
    else:
        return None

# API link and key
link = "https://www.googleapis.com/books/v1/volumes"
api = "AIzaSyA30cMef6yRkEAstfCFmY7J9UwiZhqf3ZQ"
# Replace with your actual API key

# Simple query and parameters
input_query = input("Enter your search query: ")
 # Your search query
max_results_per_page = 40  # Max results per page (API allows up to 40)
total_needed = 500
results = []  # To store fetched books
start_index = 0  # Start index for pagination

# Loop to fetch books in batches until we reach the desired number
while len(results) < total_needed:
    response = requests.get(link, params={
        "key": api,
        "q": input_query,
        "maxResults": max_results_per_page,
        "startIndex": start_index
    })

    if response.status_code == 200:
        data = response.json()  # Parse the JSON response

        if "items" in data:
            results.extend(data["items"])
            start_index += max_results_per_page
            print(f"Total books fetched so far: {len(results)}")
        else:
            print("No books found in the response or an error occurred.")
            print(data)
            break
    else:
        print(f"Error fetching data: Status Code {response.status_code}")
        print(f"Response Content: {response.text}")
        break

# Trim the list to exactly the number of books needed
results = results[:total_needed]
book_data = []
for item in results:
    volume_info = item.get('volumeInfo', {})
    accessInfo = item.get('accessInfo', {})
    saleInfo = item.get('saleInfo', {})
    p_obj = None

    book_data.append({
        'bookID': item.get('id', 'N/A'),
        'book_title': volume_info.get('title', 'N/A'),
        'book_subtitle': volume_info.get('subtitle', 'N/A'),
        'authors': ','.join(volume_info.get('authors', [])),
        'publishedDate': volume_info.get('publishedDate', 'N/A'),
        'publisher': volume_info.get('publisher', 'N/A'),
        'book_description': volume_info.get('description', 'N/A'),
        'text_readingModes': volume_info.get('readingModes', {}).get('text', False),
        'image_readingModes': volume_info.get('readingModes', {}).get('image', False),
        'pageCount': volume_info.get('pageCount', 0),
        'language': volume_info.get('language', 'N/A'),
        'ratingsCount': volume_info.get('ratingsCount', 0),
        'averageRating': volume_info.get('averageRating', 0),
        'country': accessInfo.get('country', '-'),
        'saleability': saleInfo.get('saleability', '-'),
        'isEbook': saleInfo.get('isEbook', False),
        'amount_listPrice': saleInfo.get('listPrice', {}).get('amount', 0),
        'amount_retailPrice': saleInfo.get('retailPrice', {}).get('amount', 0),
        'currencyCode_retailPrice': saleInfo.get('retailPrice', {}).get('currencyCode', '-'),
        'buyLink': saleInfo.get('buyLink', 'N/A'),
        'year': (str_to_int(volume_info.get('publishedDate')[:4])) if volume_info.get(
            'publishedDate') is not None else None,




    })
df = pd.DataFrame(book_data)
print(df)
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:kannadi%40123@127.0.0.1:3306/sakthi')
df.to_sql(name="correct2",con=engine,index=False,if_exists='replace')







