import React from "react";
import { overrideStore } from "react-overridable";
import { Card, Item, List } from "semantic-ui-react";

const {{datamodel_extension_class}}ResultsListItem = ({ result, index }) => {
  const contributors = result.metadata.contributors || [];
  return (
    <Item key={index} href={`/records/{{ result.id }}`}>
      <Item.Content>
        <Item.Header>{result.metadata.title}</Item.Header>
        <Item.Description>
          {contributorsList && (
            <List horizontal relaxed>
              {contributors.map((contributor) => (
                <List.Item>{contributor.name}</List.Item>
              ))}
            </List>
          )}
        </Item.Description>
      </Item.Content>
    </Item>
  );
};

overrideStore.add("ResultsList.item", {{datamodel_extension_class}}ResultsListItem);

const {{datamodel_extension_class}}ResultsGridItem = ({ result, index }) => {
  const contributors = result.metadata.contributors || [];
  return (
    <Card fluid key={index} href={`/records/{{ result.id }}`}>
      <Card.Content>
        <Card.Header>{result.metadata.title}</Card.Header>
        <Card.Description>
          {contributorsList && (
            <List horizontal relaxed>
              {contributors.map((contributor) => (
                <List.Item>{contributor.name}</List.Item>
              ))}
            </List>
          )}
        </Card.Description>
      </Card.Content>
    </Card>
  );
};

overrideStore.add("ResultsGrid.item", {{datamodel_extension_class}}ResultsGridItem);
