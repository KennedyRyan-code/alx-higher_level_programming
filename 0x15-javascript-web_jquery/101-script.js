$(document).ready(function () {
  $("#add_item").click(function () {
    const newItem = $("<li>Item</li>");
    $("ul.my_list").append(newItem);
  });

  $("#remove_item").click(function () {
    const list = $("ul.my_list");
    const lastItem = list.find("li:last");
    lastItem.remove();
  });

  $("#clear_list").click(function () {
    $("ul.my_list").empty();
  });
});
