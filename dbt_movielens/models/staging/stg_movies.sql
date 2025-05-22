with source as (
    select * from {{ source('main', 'movies') }}
)

select
    cast(movieId as integer) as movie_id,
    title,
    genres,
    {{ extract_year_from_title('title') }} as release_year
from source
