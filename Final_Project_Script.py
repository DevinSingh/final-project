from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import json
import lyricsgenius

# defined lexicon based sentitment analyzer using below:
analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
    return score

# This is calling on this lyricsgenius module to get the artist, title, lyrics, etc.
genius = lyricsgenius.Genius("zXGyzkSRHQeI7tu9A6sTIV_AqmTajXbuL9SRpEEkB6qulnvMCs3-fwHWYG12GS3d")
# this removies all headers (E.g. [Chorus])
genius.remove_section_headers = True

# Calling on top 40 songs ranked by Popularity
Ariana_Grande = genius.search_artist("Ariana Grande", max_songs=40, sort="popularity")
Mariah_Carey = genius.search_artist("Mariah Carey", max_songs=40, sort="popularity")
NeYo = genius.search_artist("Ne-Yo", max_songs=40, sort="popularity")
Drake = genius.search_artist("Drake", max_songs=40, sort="popularity")
Rihanna = genius.search_artist("Rihanna", max_songs=40, sort="popularity")

# Created Empty list to append dictionary items to
results = []

title_counter = 0

# Loop through and append Artist name, Song Title, Song Lyrics, and Sentiment polarity scores
# to empty list
for song in Ariana_Grande.songs:
    results.append(
                    {'Artist':'Ariana Grande',
                    'Title':str(Ariana_Grande.songs[title_counter]), # need to convert title to string to be written into JSON
                    'Lyrics':song.lyrics,
                    'Score':sentiment_analyzer_scores(song.lyrics)}
                    )
    title_counter = title_counter + 1

title_counter = 0

for song in Mariah_Carey.songs:
    results.append(
                    {'Artist':'Mariah Carey',
                    'Title':str(Mariah_Carey.songs[title_counter]),
                    'Lyrics':song.lyrics,
                    'Score':sentiment_analyzer_scores(song.lyrics)}
                    )
    title_counter = title_counter + 1

title_counter = 0

for song in NeYo.songs:
    results.append(
                    {'Artist':'Ne-Yo',
                    'Title':str(NeYo.songs[title_counter]),
                    'Lyrics':song.lyrics,
                    'Score':sentiment_analyzer_scores(song.lyrics)}
                    )
    title_counter = title_counter + 1

title_counter = 0

for song in Drake.songs:
    results.append(
                    {'Artist':'Drake',
                    'Title':str(Drake.songs[title_counter]),
                    'Lyrics':song.lyrics,
                    'Score':sentiment_analyzer_scores(song.lyrics)}
                    )
    title_counter = title_counter + 1

title_counter = 0

for song in Rihanna.songs:
    results.append(
                    {'Artist':'Rihanna',
                    'Title':str(Rihanna.songs[title_counter]),
                    'Lyrics':song.lyrics,
                    'Score':sentiment_analyzer_scores(song.lyrics)}
                    )
    title_counter = title_counter + 1

#dump results into a JSON file
with open('Lyrics.json', 'w') as file:
    file.write(json.dumps(results, indent=2))
