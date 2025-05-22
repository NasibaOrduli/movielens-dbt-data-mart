select
    m.movie_id,
    CASE
    WHEN substr(trim(m.title), -6, 1) = '('
         AND substr(trim(m.title), -5, 4) GLOB '[0-9][0-9][0-9][0-9]'
         AND substr(trim(m.title), -1, 1) = ')'
    THEN substr(trim(m.title), 1, length(trim(m.title)) - 7)
    ELSE trim(m.title)
  END as title,
    {{ extract_year_from_title('title') }} as release_year,
    l.imdbId,
    l.tmdbId
from {{ ref('stg_movies') }} m
left join {{ ref('stg_links') }} l
  on m.movie_id = l.movie_id
