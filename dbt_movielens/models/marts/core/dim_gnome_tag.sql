select distinct *
from {{ ref('stg_genome_tags') }}
