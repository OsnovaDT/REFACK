$('#navbarDropdownMenuLink').on('click', function(){
    if ($('#navbarDropdownMenu').hasClass('opened_block')){
        $('#navbarDropdownMenu').removeClass('opened_block');
    }
    else{
        $('#navbarDropdownMenu').addClass('opened_block');
    }
});