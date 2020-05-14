{%- include 'misc/header.js' %}{%- raw %}
import React from "react";
import { overrideStore } from "react-overridable";
import { Card, Input, Item, List } from "semantic-ui-react";

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

overrideStore.add("ResultsList.item", {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}ResultsListItem);

const {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}ResultsGridItem = ({ result, index }) => {
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

overrideStore.add("ResultsGrid.item", {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}ResultsGridItem);

const {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}SearchBarElement = ({
  placeholder: passedPlaceholder,
  queryString,
  onInputChange,
  executeSearch,
}) => {
  const placeholder = passedPlaceholder || "Search";
  const onBtnSearchClick = () => {
    executeSearch();
  };
  const onKeyPress = (event) => {
    if (event.key === "Enter") {
      executeSearch();
    }
  };
  return (
    <Input
      action={{
        icon: "search",
        onClick: onBtnSearchClick,
        color: "orange",
        className: "invenio-theme-search-button",
      }}
      placeholder={placeholder}
      onChange={(event, { value }) => {
        onInputChange(value);
      }}
      value={queryString}
      onKeyPress={onKeyPress}
    />
  );
};

overrideStore.add("SearchBar.element", {% endraw -%}{{cookiecutter.datamodel_extension_class}}{%- raw %}SearchBarElement);
{% endraw %}
