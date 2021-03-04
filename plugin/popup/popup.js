$(document).ready(function() {

    $("#article_form").submit(function(event) {
        var formData = {
            'title' : $('input[name=article_title]').val(),
            'content' : $('input[name=article_content]').val(),
        };

        $.ajax({
            type    : 'POST',
            url     : 'http://localhost:8000/target.html',
            data    : formData,
            dataType: 'json',
            encode  : true,
            success: function(response) {
                ajaxcomplete(response);
            },
            error: function(response) {
                response = '{"verdict": "not working", "likelihood": "high"}';
                ajaxcomplete(response);
            }
        });

        event.preventDefault();

    });

    function ajaxcomplete(results) {
        console.log(results);
        $('#main-page').hide();
        $('#result-page').show();
    }
});