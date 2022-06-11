$('#navbarDropdownMenuLink').on('click', function(){
    if ($('#navbarDropdownMenu').hasClass('opened_block')){
        $('#navbarDropdownMenu').removeClass('opened_block');
    }
    else{
        $('#navbarDropdownMenu').addClass('opened_block');
    }
});

$('#save_recomendations_link').on('click', function(e){
    $('#save_recomendations_form').submit();
    e.preventDefault();
});
