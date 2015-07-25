$(document).ready(function() {
    $('select').material_select();
	var typingTimer;
	function search () {
		var substring = $("#product_name").val();
		$.get("/medify/search", {
			search: substring,
		}).done(function(resp) {
			//TODO: Create cards
			console.log(resp);
		});
	}

	// Trigger search after not typing for 1s
	$("#product_name").keyup(function(e) {
		clearTimeout(typingTimer);
		typingTimer = setTimeout(search, 1000);
	})
	$("#product_name").keydown(function(e) {
		clearTimeout(typingTimer);
	})
});