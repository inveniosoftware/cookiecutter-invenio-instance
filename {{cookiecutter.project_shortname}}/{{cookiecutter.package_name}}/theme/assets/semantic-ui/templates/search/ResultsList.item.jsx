{%- include 'misc/header.js' %}{%- raw %}
import React from "react";
import { Item, List } from "semantic-ui-react";

const {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}ResultsListItem = ({ result, index }) => {
  const contributors = result.metadata.contributors || [];
  return (
    <Item key={index} href={`/records/${result.id}`}>
      <Item.Content>
        <Item.Header>{result.metadata.title}</Item.Header>
        <Item.Description>
          {contributors && (
            <List horizontal relaxed>
              {contributors.map((contributor, idx) => (
                <List.Item key={idx}>{contributor.name}</List.Item>
              ))}
            </List>
          )}
        </Item.Description>
      </Item.Content>
    </Item>
  );
};

export default {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}ResultsListItem;


{% endraw %}
