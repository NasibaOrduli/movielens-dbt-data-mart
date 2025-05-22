{% macro extract_year_from_title(title_column) %}
    case
        when substr(trim({{ title_column }}), length(trim({{ title_column }})) - 4, 4) GLOB '[0-9][0-9][0-9][0-9]'
        then cast(substr(trim({{ title_column }}), length(trim({{ title_column }})) - 4, 4) as integer)
        else null
    end
{% endmacro %}
