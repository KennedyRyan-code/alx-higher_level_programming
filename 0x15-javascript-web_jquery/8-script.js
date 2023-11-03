$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, textStatus) {
    $.each(data.results, function(i, item) {
        $('#list_movies').append('<li>' + item.title + '</li>')
    })
})
