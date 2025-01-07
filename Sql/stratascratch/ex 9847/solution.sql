Select
    department, count(worker_id) as num_workers
From 
    worker
Where
    Extract(month from joining_date) >= 4
Group By
    department