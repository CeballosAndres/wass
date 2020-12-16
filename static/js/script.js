
 console.log('si funciona la webada jsjs');

jQuery(document).ready(function($) {

    $(".clickable-row").click(function() {

        window.location = $(this).data("href");

    });

});