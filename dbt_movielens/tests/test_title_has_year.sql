SELECT *
FROM {{ ref('stg_movies') }}
WHERE title NOT LIKE '%(1___)%' OR title NOT LIKE '%(2___)%' 
