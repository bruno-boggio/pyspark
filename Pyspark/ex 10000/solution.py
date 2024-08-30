from pyspark.sql.functions import *

# Start writing code
uber_advertising = uber_advertising\
.where((col('customers_acquired') >= 2000) & (col('advertising_channel') == 'celebrities'))\
.select('year')\
.toPandas()

#https://platform.stratascratch.com/coding/10000-find-the-year-that-uber-acquired-more-than-2000-customers-through-celebrities?code_type=6