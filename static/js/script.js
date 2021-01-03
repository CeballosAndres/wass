
jQuery(document).ready(function ($) {

    $(".clickable-row").click(function () {

        window.location = $(this).data("href");

    });

});

window.setTimeout(function () {
    $(".alert").fadeTo(500, 0).slideUp(500, function () {
        $(this).remove();
    });
}, 2000);