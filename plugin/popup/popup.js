$(document).ready(function() {

    $("#article_form").submit(function(event) {
        var formData = {
            'title' : $('input[name=article_title]').val(),
            'content' : $('input[name=article_content]').val(),
        };

        $.ajax({
            type    : 'POST',
            url     : '../testing/target.html',
            data    : formData,
            dataType: 'json',
            encode  : true
        }).done(function(data) {
            console.log(data);
        });

        event.preventDefault();

    });
});