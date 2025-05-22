select
  cast(movieId as integer) as movie_id,
  cast(tagId as integer) as tag_id,
  cast(relevance as float) as relevance
from {{ source('main', 'genome_scores') }}
