from pyspark.sql.functions import *

# Start writing code
uber_employees = uber_employees.join(uber_annual_review, uber_employees.id == uber_annual_review.emp_id,how = 'left_anti')\
.select('first_name','last_name','hire_date','termination_date')\
.toPandas()
