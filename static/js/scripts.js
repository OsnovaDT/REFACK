$('#navbarDropdownMenuLink').on('click', function(){
    if ($('#navbarDropdownMenu').hasClass('opened_block')){
        $('#navbarDropdownMenu').removeClass('opened_block');
    }
    else{
        $('#navbarDropdownMenu').addClass('opened_block');
    }
});

$('#save_recommendations_link').on('click', function(e){
    $('#save_recommendations_form').submit();
    e.preventDefault();
});

$('#code_upload_button').click(function(){
    $("#code_upload_input").trigger('click');
});

$("#code_upload_input").change(function(){
    $('#uploaded_code').text(this.value.replace(/C:\\fakepath\\/i, ''))
});
