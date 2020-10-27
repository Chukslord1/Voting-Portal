// JavaScript Document

jQuery(document).ready(function($) {
    
    var d = $('.header');
	d.scrollToFixed({
		zIndex: 999
	});

	
	$(".menu_icon").click(function(e){
		e.preventDefault();
        $(".menu").animate({
            height: "toggle"
    });
	($(".menu_text").text() === "CLOSE") ? $(".menu_text").text("MENU") : $(".menu_text").text("CLOSE");
    });    
	$(".menubtn").on("click", function() {
		$(this).toggleClass('is_active');
		$('.menu').slideToggle('slow');
	});
		
	
	
});
