# Netflix Content Analytics

A data analytics project exploring a movie dataset using **Python, SQL, and Matplotlib**.

The project focuses on cleaning the data, analyzing patterns through SQL, and presenting useful findings through visualizations.

## Dashboard Preview

The dashboard brings together eight visualizations covering content distribution, genre-level insights, audience response, and movie financial performance

## Project Overview
This project demonstrates an end-to-end data analytics workflow, from data cleaning and preprocessing to SQL-based analysis and data visualization. The goal is to extract meaningful insights from a movie dataset and present the findings through clear, interpretable visualizations.
* **Dataset:** Movie metadata up to 2025
* **Content type:** Movies
* **Tools used:**

  * Python
  * Pandas
  * MySQL
  * Matplotlib
  * Git & GitHub

## Project Workflow

The project follows a simple analytics workflow:

1. **Data Cleaning**

   * Loaded the raw CSV using Pandas.
   * Standardized column names.
   * Removed duplicate records.
   * Converted dates and numerical columns to appropriate data types.
   * Handled missing text values.
   * Removed columns with no useful analytical value.
   * Exported the cleaned dataset for further analysis.

2. **SQL Analysis**

   * Loaded the cleaned data into MySQL.
   * Analyzed movie languages, genres, ratings, popularity, audience engagement, budgets, and revenue.
   * Created a separate `show_genres` table to work with the multi-valued genre column.
   * Used filtering, aggregation, joins, subqueries, and calculated metrics.

3. **Data Visualization**

   * Used Matplotlib to visualize selected SQL results.
   * Generated the charts automatically through `visualization.py`.
   * Saved the final charts as high-resolution PNG files in the `visuals/` directory.

## Key Analysis Areas

### Content & Language

* Language distribution across movies
* Most frequent languages
* Genre frequency

### Genre Analysis

* Genre frequency
* Average rating by genre
* Average popularity by genre

### Financial Analysis

* Highest-budget movies
* Highest-revenue movies
* Return relative to budget

### Audience Analysis

* Average ratings
* Audience vote counts
* Highly rated movies with at least 10,000 votes

## Visualizations

The project contains 8 visualizations:

1. Language Distribution
2. Genre Distribution
3. Average Rating by Genre
4. Average Popularity by Genre
5. Top 15 Movies by Budget
6. Top 15 Movies by Revenue
7. Top 15 Movies by Return Relative to Budget
8. Highly Rated Movies with at Least 10,000 Votes

All generated charts are available in the [`visuals/`](visuals/) directory.

## Project Structure

```text
Netflix_Content_Analytics/
│
├── netflix.py(Data_Cleaning and Preprocessing)
├── sql_analysis.sql
├── netflix_movies_detailed_up_to_2025.csv (Raw Dataset)
├── visualize.py
├── netflix_cleaned.csv(Clean Dataset)
├── README.md
└── visuals/
    ├── Average_Rating_by_Genre.png
    ├── Highly_Rated_Movies.png
    ├── Language_Distribution_of_Movies.png
    ├── Top_15_Genres_by_Average_Popularity.png
    ├── Top_15_Movies_by_Budget.png
    ├── Top_15_Movies_by_Return_Relative_to_Budget.png
    ├── Top_15_Movies_by_Revenue.png
    └── Top_8_Genres_by_Movie.png

```

## Technical Skills Demonstrated

* **Python:** Data cleaning and preparation with Pandas
* **SQL:** Aggregation, filtering, joins, subqueries, `JSON_TABLE`, and calculated metrics
* **Data Visualization:** Matplotlib
* **Data Handling:** Missing values, duplicates, data types, and multi-valued fields
* **Database:** MySQL
* **Version Control:** Git & GitHub

## Notes on the Data

* The dataset contains movie metadata and is not limited to Netflix-produced movies.
* `budget` and `revenue` contain missing/zero values, so financial analysis only considers records with usable values.
* A movie can belong to multiple genres. Therefore, genre-level counts and revenue-related calculations can include the same movie in multiple genres.
* Revenue represents the revenue value available in the dataset and should not be interpreted as Netflix's own revenue.
* For highly rated movie analysis, a minimum threshold of **10,000 votes** is used to reduce the effect of ratings based on very small numbers of votes.

## How to Run

### 1. Install dependencies

```bash
pip install pandas mysql-connector-python matplotlib
```

### 2. Set up MySQL

Create the required database and `netflix` table, then load the cleaned dataset.

### 3. Run the visualization script

```bash
python visualization.py
```

The script connects to MySQL, runs the analysis queries, generates the charts, and saves them automatically inside the `visuals/` directory.

## What I Learned

Through this project, I practiced:

* Turning raw data into an analysis-ready dataset
* Writing SQL queries for real analytical questions
* Working with multi-valued categorical data
* Connecting Python with MySQL
* Selecting visualizations based on the type of analysis
* Organizing an end-to-end analytics project using Git and GitHub

## Future Improvements

* Add an interactive dashboard using **Power BI**
* Add more detailed exploratory analysis
* Compare additional audience and financial metrics
* Improve the project with additional business-oriented questions
