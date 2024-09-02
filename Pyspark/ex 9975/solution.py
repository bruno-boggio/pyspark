from pyspark.sql.functions import *

# Start writing code
sf = sf_public_salaries.where(col('jobtitle')\
.contains('METROPOLITAN TRANSIT AUTHORITY'))\
.select('employeename','totalpaybenefits').toPandas()



#https://platform.stratascratch.com/coding/9975-metropolitan-transit-authority-employees?code_type=6