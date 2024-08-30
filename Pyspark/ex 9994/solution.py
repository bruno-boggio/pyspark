from pyspark.sql.functions import *

# Start writing code
spot = spotify_worldwide_daily_song_ranking.where(col('streams') < 2000)\
.select('trackname', 'streams')\
.toPandas()

#https://platform.stratascratch.com/coding/9994-find-songs-with-less-than-2000-streams?code_type=6