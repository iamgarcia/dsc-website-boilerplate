document.addEventListener("DOMContentLoaded", function () {
	$('.preloader-background').delay(1000).fadeOut('slow');

	$('.preloader-wrapper')
		.delay(1000)
		.fadeOut();
});

$(document).ready(function () {
	$('.sidenav').sidenav({
		draggable: true
	});

	$('.scrollspy').scrollSpy({
		scrollOffset: 64
	});

	$("#owl-demo").owlCarousel({
		loop: true,
		dots: false,
		items: 1,
		autoplay: true,
		autoplayTimeout: 5000
	});
});