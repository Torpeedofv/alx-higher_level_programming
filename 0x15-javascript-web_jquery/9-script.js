$('document').ready(function () {
    $.ajax({
        method: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        jsonp: 'callback', dataType: 'jsonp',
        cors: true,
        corb: true,
        success: function (data) {
          $('#hello').html(data.hello)
      },
    })

})