$(document).ready(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, (data) => {
      $('#hello').html(data.hello);
    });
  });
});
