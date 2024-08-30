from pyspark.sql.functions import *

# Start writing code
spot = spotify_worldwide_daily_song_ranking.where(col('streams') > 3000000)\
.select('trackname', 'artist', 'streams')\
.orderBy(col('streams').desc())\
.toPandas()