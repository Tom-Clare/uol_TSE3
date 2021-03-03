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
            success: function(data) {
                ajaxcomplete(data);
            },
            error: function(data) {
                data = '{"verdict": "not working", "likelihood": "high"}';
                ajaxcomplete(data);
            }
        }).done(function(data) {
            
        });

        event.preventDefault();

    });

    function ajaxcomplete(results) {
        console.log(results);
        $('#main-page').hide();
        $('#result-page').show();
    }
});