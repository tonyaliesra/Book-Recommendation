
import numpy as np
import pandas as pd

#Loading Data
Books = pd.read_csv('Books.csv')
Ratings = pd.read_csv('Ratings.csv')

Books.head()

Ratings.head()

# Books and Ratings data are combined by 'ISBN' column.
x = pd.merge(Books,Ratings,on='ISBN')
x.head()

# Count users and books by number of ratings.
popular_users = x['User-ID'].value_counts()
popular_books = x['Book-Title'].value_counts()

# Users who voted at least 100 times and books with more than 100 votes will be selected.
filtered_users = popular_users[popular_users > 100].index
filtered_books = popular_books[popular_books > 100].index

# Create x_filtered
x_filtered = x[(x['User-ID'].isin(filtered_users)) & (x['Book-Title'].isin(filtered_books))]

# Creates a pivot table (makes users rows, books columns).
# Missing values are left as NaN by default (use fill_value=0 to replace them).
table = x_filtered.pivot_table(
    index='User-ID',
    columns='Book-Title',
    values='Book-Rating',
    #fill_value=0,
    aggfunc='mean'
).astype('float32')
table.head()

# All user ratings for the book 'The Da Vinci Code' are taken into account.
book = table['The Da Vinci Code']
book

# Correlation of other books according to 'The Da Vinci Code'.
corr = pd.DataFrame(table.corrwith(book), columns= ["Correlation"])
corr

# The 10 books with the highest correlation with 'The Da Vinci Code' are ranked.
corr.sort_values ("Correlation", ascending=False).head(10)

# The average score for each book is calculated and the books with the highest average are listed.
Ratings = pd.DataFrame(x.groupby('Book-Title')['Book-Rating'].mean())
Ratings.sort_values("Book-Rating", ascending=False).head()

# The number of times each book has been rated is calculated and the books with the most rates are listed.
Ratings['Num_of_Ratings'] = x.groupby('Book-Title')['Book-Rating'].count()
Ratings.sort_values("Num_of_Ratings", ascending=False).head()

# Join correlation data with the number of ratings each book received.
Correlation = corr.join(Ratings['Num_of_Ratings'])
Correlation.head()

# For users who liked the book 'The Da Vinci Code', book recommendations with high correlation are listed.
Correlation[Correlation['Num_of_Ratings']>100].sort_values('Correlation',ascending=False).head()

