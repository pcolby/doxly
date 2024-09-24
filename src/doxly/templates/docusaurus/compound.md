---
{# https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#markdown-front-matter -#}
id: {{ compound.id }}
title: {{ compound.compoundname }} {{ compound.kind|capitalize }}
{% if compound.briefdescription.para -%}
description: {{ compound.briefdescription.para[0].valueOf_|trim }}
{% endif -%}
tags:
---
{% for para in compound.briefdescription.para %}{{ para|tomarkdown|trim }}{% endfor %}
{% for para in compound.detaileddescription.para %}{{ para|tomarkdown|trim }}{% endfor %}
