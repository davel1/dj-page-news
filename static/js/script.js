$(document).ready(function(){
  $(window).scroll(function() {
    if($(this).scrollTop() >= 149) {
	$('#menu').css('position','fixed');
	$('#menu').css('width','100%');
	$('#menu').css('top','0'); 
    } else {
	$('#menu').css('position','relative');
	$('#menu').css('width','100%');
	$('#menu').css('top','0');
    }
  }); 
});
