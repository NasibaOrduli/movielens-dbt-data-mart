select
  cast(tagId as integer) as tag_id,
  tag
from {{ source('main', 'genome_tags') }}
