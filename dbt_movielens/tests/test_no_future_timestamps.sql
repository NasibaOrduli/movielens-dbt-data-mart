SELECT *
FROM {{ ref('stg_ratings') }}
WHERE datetime(timestamp) > CURRENT_TIMESTAMP
