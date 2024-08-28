from pyspark.sql.functions import *

employee_list = employee_list\
.select('first_name','last_name')\
.where((col('last_name') == 'Johnson') & (col('profession') == 'Doctor'))\
.toPandas()

#https://platform.stratascratch.com/coding/10356-finding-doctors?code_type=6