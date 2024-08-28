from pyspark.sql.functions import *

postmates_orders = postmates_orders\
.agg(countDistinct('customer_id').alias('nunique_customer_id'),avg('amount').alias('mean_amount'))\
.toPandas()


#https://platform.stratascratch.com/coding/2013-customer-average-orders?code_type=6