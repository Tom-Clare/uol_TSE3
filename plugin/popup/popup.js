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
                response = '{"verdict": "true", "confidence": "0.1"}';
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

        if (data.verdict == 'true') {
            $('.bool-result').html("This news is <b>likely</b> to be true.");
        }
        else if(data.verdict == 'false') {
            $('.bool-result').html("This news is <b>likely</b> to be false.");
        }
        var displayPercentage = 'p' + data.confidence*100;
        $('.percentage-replace').addClass(displayPercentage);
        $('.number-replace').text(data.confidence*100 + "%");
    }
});