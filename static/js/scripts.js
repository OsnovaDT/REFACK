// Dropdown menu

$('#dropdown_menu_link').on('click', function(){
    $('#dropdown_menu').toggle();
});

// Save recommendations link

$('#save_recommendations_link').on('click', function(event){
    $('#save_recommendations_form').submit();

    event.preventDefault();
});

function updateSaveRecommendationFormData(response){
    let code = $("textarea[name='code']").val();
    let recommendations = Object.entries(response.recommendations);

    $("input[name='code']").val(code);
    $("input[name='recommendation']").val(recommendations);
};

function updateResultsForFileDownload(response){
    results = "{";

    for (const [rule, code_item] of Object.entries(response.recommendations)){
        results += `"${rule}": "${code_item}",`;
    };

    if (results.slice(-1) == ','){
        results = results.substring(0, results.length - 1);
    };

    results += "}"

    $("input[name='results']").val(results);
};

function updateRecommendationsBlock(response){
    $('#recommendations').empty();

    if (response.error){
        let error = `Ошибка: <span class="error_code">${response.error}</span>`;

        $('#recommendations').append(error);
    }
    else{
        for (const [rule, code_item] of Object.entries(response.recommendations)){
            let recommendation = `<p>${rule}: <span class="code_item">${code_item}</span></p>`;

            $('#recommendations').append(recommendation);
        };
    };
};

// Refactoring

function pasteCodeFromFileToTextarea(input){
    let reader = new FileReader();
    let codeFile = input.files[0];

    reader.readAsText(codeFile);

    reader.onload = function() {
        $('#source_code').val(reader.result);
    };

    reader.onerror = function() {
        $('#source_code').val(reader.error);
    };
}

$('#file_upload').click(function(){
    $("#file_upload_input").trigger('click');
});

// Login

$('#login_button').on('click', function(){
    $('form').submit();
});
