select
  cast(movieId as integer) as movie_id,
  imdbId,
  tmdbId
from {{ source('main', 'links') }}
