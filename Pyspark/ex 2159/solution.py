from pyspark.sql.functions import *

transactions = (
    transactions
    .select('signup_id')
    .filter(
        col('transaction_start_date').between('2020-04-01', '2020-05-30')
    )
    .distinct()
)


# https://platform.stratascratch.com/coding/2159-april-may-sign-ups?code_type=6