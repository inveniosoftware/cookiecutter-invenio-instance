{%- include 'misc/header.js' %}{%- raw %}
import React from "react";
import { Card, List } from "semantic-ui-react";

export const {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}ResultsGridItem = ({ result, index }) => {
    const contributors = result.metadata.contributors || [];
    return (
      <Card fluid key={index} href={`/records/${result.id}`}>
        <Card.Content>
          <Card.Header>{result.metadata.title}</Card.Header>
          <Card.Description>
            {contributors && (
              <List horizontal relaxed>
                {contributors.map((contributor, idx) => (
                  <List.Item key={idx}>{contributor.name}</List.Item>
                ))}
              </List>
            )}
          </Card.Description>
        </Card.Content>
      </Card>
    );
  };

export default {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}ResultsGridItem;

{% endraw %}
