// Secondary functions

function getErrorForHtmlDisplay(error){
    return `Ошибка: <span class="error_code">${error}</span>`;
}

// Menu

$('#dropdown_menu_link').on('click', function(){
    $('#dropdown_menu').toggle();
});

// Buttons

$('#login_button').on('click', function(){
    $('form').submit();
});

// File code paste

$('#paste_code_from_file_button').on('click', function(){
    $("#paste_code_from_file").trigger('click');
});

function pasteFileCodeToInput(input){
    const fileWithCode = input.files[0];

    let reader = new FileReader();

    reader.readAsText(fileWithCode);

    reader.onload = function() {
        $('#source_code').val(reader.result);
    };

    reader.onerror = function() {
        $('#source_code').val(reader.error);
    };
}

// Refactoring

function addCodeAndRecommendationToSaveRecommendationForm(response){
    const code = $("textarea[name='code']").val();

    let recommendationsForDisplayInHtml = "";
    for (const [rule, code_item] of Object.entries(response.recommendations)){
        recommendationsForDisplayInHtml += `${rule}: <span class="code_item">${code_item}</span><br><br>`;
    }

    $("input[name='code']").val(code);
    $("input[name='recommendation']").val(recommendationsForDisplayInHtml);
};

function addResultsToFilesDownloadForm(response){
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

function showRefactoringRecommendations(response){
    $('#recommendations').empty();

    if (response.error){
        const error = getErrorForHtmlDisplay(response.error);

        $('#recommendations').append(error);
    }
    else{
        for (const [rule, code_item] of Object.entries(response.recommendations)){
            let recommendation = `<p>${rule}: <span class="code_item">${code_item}</span></p>`;

            $('#recommendations').append(recommendation);
        };
    };
};

// Recommendations saving

function saveRefactoringRecommendations(response){
    if (response.error){
        $('#recommendations').empty();
        $('#recommendations').prepend(getErrorForHtmlDisplay(response.error));
    }
    else{
        $('#save_recommendations_link').hide();
    }
}

$('#save_recommendations_link').on('click', function(event){
    $('#save_recommendations_form').submit();

    event.preventDefault();
});
