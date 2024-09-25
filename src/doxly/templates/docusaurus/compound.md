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

{% for section in compound.sectiondef|selectattr('kind', 'eq', 'public-static-func') %}
## Public Static Functions
{% for member in section.memberdef %}
{{ member.type }}
{{ member.argstring }}
{{ member.qualifiedname }}
{% endfor %}
{% endfor %}

{#
      <xsd:enumeration value="user-defined" />
      <xsd:enumeration value="public-type" />
      <xsd:enumeration value="public-func" />
      <xsd:enumeration value="public-attrib" />
      <xsd:enumeration value="public-slot" />
      <xsd:enumeration value="signal" />
      <xsd:enumeration value="dcop-func" />
      <xsd:enumeration value="property" />
      <xsd:enumeration value="event" />
      <xsd:enumeration value="public-static-func" />
      <xsd:enumeration value="public-static-attrib" />
      <xsd:enumeration value="protected-type" />
      <xsd:enumeration value="protected-func" />
      <xsd:enumeration value="protected-attrib" />
      <xsd:enumeration value="protected-slot" />
      <xsd:enumeration value="protected-static-func" />
      <xsd:enumeration value="protected-static-attrib" />
      <xsd:enumeration value="package-type" />
      <xsd:enumeration value="package-func" />
      <xsd:enumeration value="package-attrib" />
      <xsd:enumeration value="package-static-func" />
      <xsd:enumeration value="package-static-attrib" />
      <xsd:enumeration value="private-type" />
      <xsd:enumeration value="private-func" />
      <xsd:enumeration value="private-attrib" />
      <xsd:enumeration value="private-slot" />
      <xsd:enumeration value="private-static-func" />
      <xsd:enumeration value="private-static-attrib" />
      <xsd:enumeration value="friend" />
      <xsd:enumeration value="related" />
      <xsd:enumeration value="define" />
      <xsd:enumeration value="prototype" />
      <xsd:enumeration value="typedef" />
      <xsd:enumeration value="enum" />
      <xsd:enumeration value="func" />
      <xsd:enumeration value="var" />
#}
