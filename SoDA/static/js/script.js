$(document).ready(function () {
    $('.hideMe').first().removeClass('hideMe').addClass('showMe');
    $('.card-button').first().addClass('hideMe');
    $('.mdl-card__supporting-text').first().css('margin','18px');

    hideShow();
})

function windowResize() {
    if ($(window).width() <= 1000) {
    	$('.mdl-layout__drawer-button').removeClass('hideMe').addClass('showMe');
        $('.desktop-header').removeClass('showMe').addClass('hideMe');
       
    }
    else {
    	$('.mdl-layout__drawer-button').removeClass('showMe').addClass('hideMe');
        $('.desktop-header').removeClass('hideMe').addClass('showMe');
    }
}

function hideShow() {
    $('.card-button').click(function () {
        $('.card-button').parent().siblings('.mdl-card__supporting-text').children('.showMe').not(this).each(function () {
            $(".card-button").parent().siblings('.mdl-card__supporting-text').children('.showMe').removeClass("showMe").addClass("hideMe");
            $('.card-button').parent().siblings('.mdl-card__supporting-text').css('margin','0px');           
            $(".card-button").removeClass('hideMe');
        });
        if ($(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').length) {
            $(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').removeClass('hideMe').addClass('showMe');
            $(this).parent().siblings('.mdl-card__supporting-text').css('margin','18px');
            $(this).addClass('hideMe');
        }
        $('main').animate({
            scrollTop: $(this).closest('section')[0].offsetTop - 100
        }, 800);

    });
}

