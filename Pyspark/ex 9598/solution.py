from pyspark.sql.functions import *

# Start writing code
sat_scores = sat_scores.filter(~col('school').like('%HS')).select('*').toPandas()

#https://platform.stratascratch.com/coding/9598-find-non-hs-sat-scores?code_type=6