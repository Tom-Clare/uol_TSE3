$(document).ready(function() {

    $("#article_form").submit(function(event) {
        var content = $('input[name=article_content]').val();
        if (content == "") {
            showerror("Please include the article content.")
            event.preventDefault();
            return;
        }

        var formData = {
            'content' : $('input[name=article_content]').val(),
        };

        $.ajax({
            type    : 'POST',
            url     : 'http://ec2-18-130-208-115.eu-west-2.compute.amazonaws.com:5000/target',
            data    : formData,
            dataType: 'json',
            encode  : true,
            success: function(response) {
                ajaxsuccess(response);
            },
            error: function() {
                console.log("We could not reach the server at this time");
                showerror("We could not reach the server at this time");
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

    function showerror(errortext) {
        console.log(errortext);
        $('#error-area').html(errortext);
    }

    function hideerror() {
        $('#error-area').html("");
    }
    
    $('input[name=article_content]').on('input', function() {
        if($(this).val() != '') {
            hideerror();
        }
    });
});