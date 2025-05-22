with source as (
    select * from {{ source('main', 'ratings') }}
)

select
    cast(userId as integer) as user_id,
    cast(movieId as integer) as movie_id,
    rating,
    timestamp
from source
