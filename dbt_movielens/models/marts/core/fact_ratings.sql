select
    user_id,
    movie_id,
    cast(rating as float) as rating,
    datetime(timestamp) as rating_datetime
from {{ ref('stg_ratings') }}
