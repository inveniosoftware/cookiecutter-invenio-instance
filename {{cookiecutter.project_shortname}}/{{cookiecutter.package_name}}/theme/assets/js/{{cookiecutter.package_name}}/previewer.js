import $ from "jquery";

$("#files")
  .find(".preview-link")
  .on("click", function(event) {
    $("#preview").show();
    $("#preview-iframe").attr("src", $(event.target).data("url"));
  });
