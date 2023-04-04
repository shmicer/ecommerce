$('.delivery_hide').addClass('collapse');

//on change hide all divs linked to select and show only linked to selected option
$('#delivery').change(function(){
    //Saves in a variable the wanted div
    var selector = '.delivery_' + $(this).val();

    //hide all elements
    $('.delivery_hide').collapse('hide');

    //show only element connected to selected option
    $(selector).collapse('show');
});