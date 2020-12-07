import { createSearchAppInit } from "@js/invenio_search_ui";
import { MysiteSearchBarElement } from "./search_app_customizations";

const initSearchApp = createSearchAppInit({
  "ResultsList.item": null, // Just pass null to overwrite it with the JSX components declared in the templates/search folder
  "ResultsGrid.item": null,
  "SearchBar.element": MysiteSearchBarElement,
});
