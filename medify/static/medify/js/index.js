$(document).ready(function () {
    $('#clearbtn').click(function () {
        CC(); //clearCards()
    });

    $('#advancedbtn').click(function () {
        advanced();
    });

    $('#filterbtn').click(function () {
        clearFilter();
    });
    $('#filter_am').click(function () {
        filterType(0);
    });
    $('#filter_im').click(function () {
        filterType(1);
    });
    $('#filter_ad').click(function () {
        filterType(2);
    });

    $('select').material_select();
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15 // Creates a dropdown of 15 years to control year
    });

    var typingTimer;

    $('#deepsbtn').click(function () {
        $('#deepsval').val("true");
        search();
    });


    function advanced() {
        CC().done(
            function () {
                showLoadingCircle();
                $.get("/advanced_search", {
                    name: $("#product_name_advanced").val(),
                    manufacturer: $("#manufacturer_advanced").val(),
                    active_ingredient: $("#active_ingredient_advanced").val(),
                    f_class: $("#f_class").val(),
                    fromdate: $("#fromdate").val(),
                    todate: $("#todate").val()
                }).done(function (resp) {
                    hideLoadingCircle();
                    if (resp.approved_medication.length === 0) {
                        Materialize.toast('No results found!', 4000);
                    } else if (resp.approved_medication.length === 1) {
                        Materialize.toast('1 result found!', 4000);
                    } else {
                        Materialize.toast(resp.approved_medication.length + ' results found!', 4000);
                    }
                    $.each(resp.approved_medication, function (k, v) {
                        addItem(v, 0);
                    });
                });
            });
    }

    function search() {
        var substring = $("#product_name").val();
        var deep_s = $("#deepsval").val();
        $('#deepsval').val("false");
        CC().done(
            function () {
                showLoadingCircle();
                $.get("/search", {
                    search: substring,
                    deep_search: deep_s
                }).done(function (resp) {
                    hideLoadingCircle();

                    $.each(resp.approved_medication, function (k, v) {
                        addItem(v, 0);
                    });
                    $.each(resp.illegal_medication, function (k, v) {
                        addItem(v, 1);
                    });
                    $.each(resp.approved_devices, function (k, v) {
                        addItem(v, 2);
                    });

                    if (resp.approved_medication.length === 0 && resp.illegal_medication.length === 0 && resp.approved_devices.length === 0) {
                        if (deep_s === "false") {
                            $('#modal1').openModal();
                        }
                    }
                });
            });
    }

    // Trigger search after not typing for 1s
    $("#product_name").keyup(function (e) {
        if (e.keyCode == 13) {
            clearTimeout(typingTimer);
            search();
        } else {
            clearTimeout(typingTimer);
            if (!!$("#product_name").val().trim())
                typingTimer = setTimeout(search, 1000);
        }
    });
    $("#product_name").keydown(function (e) {
        clearTimeout(typingTimer);
    });
});

function addItem(data, type) {
    var div;
    if (type === 0) {
        div =
            '<div class="col s4 t0">' +
            '    <div class="card small">' +
            '        <div class="card-content">' +
            '            <span class="card-title black-text"><p>' + data.product_name + '</p></span>' +
            '            <p class="grey-text text-darken-2">' + data.active_ingredients + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.manufacturer + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.country + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.f_class + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.dosage_form + ', ' + data.route + '</p>' +
            '        </div>' +
            '       <div class="card-action type-marker green lighten-2">' +
            '       Approved Medicine' +
            '       </div>' +
            '    </div>' +
            '</div>';
    } else if (type === 1) {
        div =
            '<div class="col s4 t1">' +
            '    <div class="card small">' +
            '        <div class="card-content">' +
            '            <span class="card-title black-text"><p>' + data.product_name + '</p></span>' +
            '            <p class="grey-text text-darken-2">' + data.adulterant_type + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.manufacturer + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.country + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.remarks + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.dosage_form_colour + ', ' + data.dosage_form_shape + ', ' + data.dosage_form + '</p>' +
            '        </div>' +
            '       <div class="card-action type-marker red darken-1">' +
            '       Illegal Medicine' +
            '       </div>' +
            '    </div>' +
            '</div>';
    } else if (type === 2) {
        div =
            '<div class="col s4 t2">' +
            '    <div class="card small">' +
            '        <div class="card-content">' +
            '            <span class="card-title black-text"><p>' + data.device_name + '</p></span>' +
            '            <p class="grey-text text-darken-2">' + data.description + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.product_owner_short_name + '</p>' +
            '            <p class="grey-text text-darken-2">' + data.speciality + '</p>' +
            '        </div>' +
            '       <div class="card-action type-marker green lighten-2">' +
            '       Approved Device' +
            '       </div>' +
            '    </div>' +
            '</div>';
    }
    $('#results').append(div);
}

var CC = function clearCards() {
    var def = new $.Deferred();
    $('#results').fadeOut(400, function () {
        $('#results').empty();
    });
    $('#results').fadeIn(100);
    setTimeout(function () {
        def.resolve();
    }, 500);

    return def;
};

function clearForms() {
    $(this).find("input").val('');
}

function filterType(type) {
    $('#results > div.col.s4').not('.t' + type).hide(250, function () {
        $('#results > div.col.s4.t' + type).show(250);
    });
}

function clearFilter() {
    $('#results > div.col.s4').show(400);
}

function showLoadingCircle() {
    $('div#loading-circle').show();
}

function hideLoadingCircle() {
    $('div#loading-circle').hide();
}
