from pyspark.sql.functions import *

customers = customers.join(orders, customers.id == orders.cust_id)\
.select('first_name','order_date','order_details','total_order_cost')\
.orderBy('first_name')\
.where((col('first_name') == 'Eva') | (col('first_name') == 'Jill'))\
.toPandas()

#https://platform.stratascratch.com/coding/9913-order-details?code_type=6