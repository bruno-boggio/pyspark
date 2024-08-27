# Import your libraries
from pyspark.sql.functions import *

# Start writing code
airbnb_search_details = airbnb_search_details\
.where(col('bathrooms') == col('bedrooms'))\
.toPandas()

#https://platform.stratascratch.com/coding/9617-find-all-searches-for-accommodations-with-an-equal-number-of-bedrooms-bathrooms?code_type=6