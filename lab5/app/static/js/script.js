$(document).ready(function () {
    $(".progress-bar").circularProgress({
        color: "#222",
        line_width:15,
        height:"1280px",
        width:"1920px",
        percent:0,
            }).circularProgress('animate', 100, 2500);
});    
$(window).on('load', function (){
	var $preloader = $('.progress-bar')
	$preloader.delay(4500).fadeOut('slow');
});