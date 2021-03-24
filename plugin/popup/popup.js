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
                ajaxsuccess(response);
            },
            error: function(response) {
                response = '{"verdict": "true", "confidence": "0.78"}';
                ajaxsuccess(response);
            }
        });

        event.preventDefault();

    });

    function ajaxsuccess(results) {
        var data = JSON.parse(results);

        console.log(data);
        $('#main-page').hide();
        $('#result-page').show();

        $('.bool-result').text(data.verdict);
    }
});