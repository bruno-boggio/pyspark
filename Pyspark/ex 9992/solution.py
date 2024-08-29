from pyspark.sql.functions import *

# Start writing code
spotify_worldwide_daily_song_ranking = spotify_worldwide_daily_song_ranking.groupBy('artist')\
.agg(count('position').alias('n_occurences'))\
.toPandas()

#https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=6