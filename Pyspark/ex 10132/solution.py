from pyspark.sql.functions import *

# Start writing code
sf_crime_incidents_2014_01 = sf_crime_incidents_2014_01\
.groupBy('day_of_week')
\.agg(count('incidnt_num'))\
.toPandas()
