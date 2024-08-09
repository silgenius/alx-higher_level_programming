$(document).ready(function () {
  $('#add_item').click(function () {
    const newList = $('<li>').text('Item');
    $('ul.my_list').append(newList);
  });
});
