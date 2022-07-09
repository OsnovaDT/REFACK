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

function updateRecommendationsBlock(response){
    $('#recommendations').empty();

    if (response.error){
        let error = `Ошибка: <span class="error">${response.error}</span>`;

        $('#recommendations').append(error);
    }
    else{
        for (const [rule, code_item] of Object.entries(response.recommendations)){
            let recommendation = `<p>${rule}: <span class="code_item">${code_item}</span></p>`;

            $('#recommendations').append(recommendation);
        };
    };
};

// File upload
$('#file_upload').click(function(){
    $("#file_upload_input").trigger('click');
});

$("#file_upload_input").change(function(){
    $('#uploaded_file').text(this.value.replace(/C:\\fakepath\\/i, ''));
});

// Login

$('#login_button').on('click', function(){
    $('form').submit();
});
