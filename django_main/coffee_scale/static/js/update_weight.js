$(document).ready(function () {
    setInterval(function () {
        $.ajax({
            url: 'get_weight/',  // URL of your Django view
            type: 'GET',
            success: function (data) {
                $('#value').text(data);  // Update the value in the HTML element with id 'value'
            },
            error: function () {
                console.log('An error occurred while updating the value.');
            }
        });
    }, 1000);  // Update the value every 1 second (adjust as needed)
});
