Select  
    city,
    property_type,
    avg(bathrooms) as n_bathrooms_avg,
    avg(bedrooms) as n_bedrooms_avg
From
    airbnb_search_details
Group by
    city,property_type