# Book Recommendation System

This project builds a simple book recommendation system based on user rating correlations. It analyzes user-book interactions to suggest books similar to a selected title. The dataset was obtained from Kaggle.

## What Does This Project Do?

- Filters active users and frequently rated books based on a minimum threshold.
- Creates a pivot table with users as rows and books as columns.
- Calculates correlation scores between books based on user ratings.
- Recommends books similar to a selected one (e.g., *The Da Vinci Code*).
- Lists books with the highest average ratings and the most rating counts.

## Dataset Used

The dataset was sourced from Kaggle:  
🔗 [Kaggle: Book Recommendation System Dataset](https://www.kaggle.com/code/fahadmehfoooz/book-recommendation-system/input)

- **Books.csv** → Contains book information (ISBN, Book-Title, Book-Author, etc.)
- **Ratings.csv** → Contains user ratings for books (User-ID, ISBN, Book-Rating)

## Requirements

Make sure the following Python libraries are installed:

```bash
pandas
numpy
