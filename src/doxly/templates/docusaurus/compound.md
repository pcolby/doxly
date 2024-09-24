---
{# https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#markdown-front-matter -#}
id: {{ compound.refid }}
title: {{ compound.compoundname }} {{ compound.kind|capitalize }}
{% if compound.briefdescription.para -%}
description: {{ compound.briefdescription.para[0].valueOf_|trim }}
{% endif -%}
tags:
---

