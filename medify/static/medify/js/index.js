$(document).ready(function () {
    $('#clearbtn').click(function () {
        clearCards();
    });
    $('select').material_select();
    var typingTimer;
    
    $('#deepsbtn').click(function() {
		$('#deepsval').val("true");
		search();
	});

    function search() {
        var substring = $("#product_name").val();
        var deep_s =  $("#deepsval").val();
        $('#deepsval').val("false");
        CC().done(
            function () {
                $.get("/medify/search", {
                    search: substring,
                    deep_search: deep_s
                }).done(function (resp) {
                    $.each(resp.approved_medication, function (k, v) {
                        addItem(v, true);
                    });
                    $.each(resp.illegal_medication, function (k, v) {
                        addItem(v, false);
                    });
                    
                    if(resp.approved_medication.length==0 && resp.illegal_medication.length==0 && resp.approved_devices.length==0){
						$('#modal1').openModal();
					}
                });
            });
    }

    // Trigger search after not typing for 1s
    $("#product_name").keyup(function (e) {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(search, 1000);
    });
    $("#product_name").keydown(function (e) {
        clearTimeout(typingTimer);
    });
});

function addItem(data, approved) {
    if (approved) {
        var div =
            '<div class="col s4">' +
            '    <div class="card small">' +
            '        <div class="card-content">' +
            '            <span class="card-title black-text"><p>' + data.product_name + '</p></span>' +
            '            <p class="grey-text text-darken-2">' + data.active_ingredients + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.manufacturer + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.country + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.f_class + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.dosage_form + ', ' + data.route + '</p>' +
            '        </div>' +
            '       <div class="card-action green lighten-2">' +
            '    </div>' +
            '</div>';
    } else {
        var div =
            '<div class="col s4">' +
            '    <div class="card small">' +
            '        <div class="card-content">' +
            '            <span class="card-title black-text"><p>' + data.product_name + '</p></span>' +
            '            <p class="grey-text text-darken-2">' + data.adulterant_type + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.manufacturer + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.country + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.remarks + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.dosage_form_colour + ', ' + data.dosage_form_shape + ', ' + data.dosage_form + '</p>' +
            '        </div>' +
            '       <div class="card-action red darken-1">' +
            '    </div>' +
            '</div>';
    }
    $('#results').append(div);
}

var CC = function clearCards() {
     var def = new $.Deferred();
    $('#results').fadeOut(400, function () {
        $('#results').empty()
    });
    $('#results').fadeIn(100);
    setTimeout(function () {
    def.resolve();
  }, 500);

    return def;
}
