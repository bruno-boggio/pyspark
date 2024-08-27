# Import your libraries
from pyspark.sql.functions import *

# Start writing code
yelp_business = yelp_business\
.groupBy('state')\
.agg(avg('stars').alias('avg_stars'))\
.toPandas()

#https://platform.stratascratch.com/coding/10052-find-the-average-number-of-stars-for-each-state?code_type=6