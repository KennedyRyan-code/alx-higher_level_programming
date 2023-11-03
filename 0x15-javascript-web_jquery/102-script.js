$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    if (languageCode) {
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
