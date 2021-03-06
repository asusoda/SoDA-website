//script to expand and hide cards 

$(document).ready(function () {
    $('.hideMe').first().removeClass('hideMe').addClass('showMe');
    $('.card-button').first().addClass('dontShow');
    $('.card-button').click(function () {
        $('.card-button').parent().siblings('.mdl-card__supporting-text').children('.showMe').not(this).each(function () {
            $(".card-button").parent().siblings('.mdl-card__supporting-text').children('.showMe').removeClass("showMe").addClass("hideMe");
            $(".card-button").removeClass('dontShow');
        });
        if ($(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').length) {
            $(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').removeClass('hideMe').addClass('showMe');
            $(this).addClass('dontShow');
        }
        $('main').animate({
            scrollTop: $(this).closest('section')[0].offsetTop - 100
        }, 800);

    });
})