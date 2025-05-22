with recursive genres_exploded as (
  select
    movie_id,
    substr(genres || '|', 1, instr(genres || '|', '|') - 1) as genre,
    substr(genres || '|', instr(genres || '|', '|') + 1) as rest
  from {{ ref('stg_movies') }}

  union all

  select
    movie_id,
    substr(rest, 1, instr(rest, '|') - 1),
    substr(rest, instr(rest, '|') + 1)
  from genres_exploded
  where rest != ''
)

select
  row_number() over (order by genre) as genre_id,
  genre
from genres_exploded
where genre != ''
group by genre
