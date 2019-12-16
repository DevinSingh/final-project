# final-project

For this final project, I conducted a sentiment analysis on the top 40 songs from five of my favorite artists - Drake, Ariana Grande, Mariah Carey, Ne-Yo, and Rihanna. A sentiment analysis is the process of determining whether writing is positive, negative, or neutral. I thought that it would be particularly interesting to see how my favorite artists and songs perform on a sentiment analysis. Initially, I attempted to scrape the artist, title, and lyrics from genius.com however, I ran into an issue with web scraping from their site. Ultimately, I used a python package titled “lyricsgenius” which calls on their API to obtain the data that I needed. 

To conduct the sentiment analysis, I used another python package titled “VaderSentiment”. The Vader sentiment analyzer returned a positive, negative, and neutral score for each song lyric. It also returned a composite score while determine the overall negativity or positivity of a song. The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1 (most extreme negative) and +1 (most extreme positive). 

After gathering all the lyrics and conducting the sentiment analysis, I dumped my data into a json file which was then converted into a csv file using http://www.convertcsv.com/json-to-csv.htm. After, I uploaded the csv file to Tableau Public and created an interactive dashboard that show the composite, positive, negative, and neutral scores for each artist.

# How To Recreate This Project

Follow these steps to recreate this project with any artists/songs that you'd like:

1. Install lyricsgenius package by using “pip install lyricsgenius”.
2. Install vaderSentiment by using “pip install vaderSentiment”.
3. Create a free account that authorizes access to Genius API to obtain a “client_access_token”.
4. Run the code “Final_Project_script_1.py” with your unique “client_access_token”.
5. Convert Json file to a CSV using http://www.convertcsv.com/json-to-csv.htm
6. Clean “Title” column of CSV file so that it only contains the songs’ title.
7. Feed cleaned CSV into Tableau Public and create visualizations.
