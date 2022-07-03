// Dropdown menu
$('#dropdown_menu_link').on('click', function(){
    if ($('#dropdown_menu').hasClass('dropped')){
        $('#dropdown_menu').removeClass('dropped');
    }
    else{
        $('#dropdown_menu').addClass('dropped');
    }
});

// Refactoring recommendations
$('#save_recommendations_link').on('click', function(event){
    $('#save_recommendations_form').submit();

    event.preventDefault();
});

// File upload
$('#file_upload').click(function(){
    $("#file_upload_input").trigger('click');
});

$("#file_upload_input").change(function(){
    $('#uploaded_file').text(this.value.replace(/C:\\fakepath\\/i, ''));
});
