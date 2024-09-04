from pyspark.sql.functions import *

# Start writing code
orders_analysis = orders_analysis\
.where((quarter('week') == 1) & (year('week') == 2023))\
.groupBy('week')\
.agg(sum('quantity').alias('total_qnt'))\
.select('week','total_qnt')\
.toPandas()

#https://platform.stratascratch.com/coding/10363-weekly-orders-report?code_type=6