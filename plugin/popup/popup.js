$(document).ready(function() {

    $("#article_form").submit(function(event) {
        var formData = {
            'title' : $('input[name=article_title]').val(),
            'content' : $('input[name=article_content]').val(),
        };

        $.ajax({
            type    : 'POST',
            url     : 'http://localhost:5000/target',
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
        console.log(results);
        $('#main-page').hide();
        $('#result-page').show();

        $('#result-single').html(results.verdict)
        var confidence = parseFloat(results.confidence)
        var displayPercentage = 'p' + confidence*100;
        $('.percentage-replace').addClass(displayPercentage);
        $('.number-replace').text(confidence*100 + "%");
    }
});