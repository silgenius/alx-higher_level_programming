$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json',
    success: function (data) {
      $.each(data.results, function (i, result) {
        const title = $('<li>').text(result.title);
        $('#list_movies').append(title);
      });
    }
  });
});
