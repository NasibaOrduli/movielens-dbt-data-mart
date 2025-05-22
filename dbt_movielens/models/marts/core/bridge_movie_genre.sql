with exploded as (
  select
    movie_id,
    genre_json.value as genre
  from {{ ref('stg_movies') }},
       json_each('["' || replace(genres, '|', '","') || '"]') as genre_json
)

select
  e.movie_id,
  d.genre_id
from exploded e
join {{ ref('dim_genre') }} d
  on lower(e.genre) = lower(d.genre)
