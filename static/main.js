const server = 'http://localhost:5000/'

$('#begin').on('click', function () {
    $.ajax({
        url: server + "api/intro",
        method: 'GET',
        datatype: 'json'
    }).done(function (result) {
        $('#begin').hide();
        $('#main').show();
        let texts = result.texts
        counter = 0,
            timer = setInterval(function () {
                displayText(texts[counter]);
                counter++
                if (counter === texts.length) {
                    $('#yes-no-song').show()
                    clearInterval(timer);
                }
            }, 2000)
        
    })
})

$('#no-song').on('click', function () {
    $('#yes-no-song').hide();
    $('#main').html(`<p>Well, well then! Looks like you'll need a Poke, lil' whippersnapper!</p>`)
    chooseType();
})

function displayText(text) {
    $('#main').append(`<p>${text}</p>`);
}

function chooseType() {
    $.ajax({
        url: server + "api/type-list",
        method: 'GET',
        datatype: 'json'
    }).done(function (result) {
        types = result.types
        timer = setInterval(function () {
            displayText("Which Poke do you choose?");
            $('#poke-choice-buttons').show();
            types.forEach(type => {
                $('#poke-choice-buttons').append(`<button type='button' class="choose-type" id="type" value="${type}">${type}</button>`);
            });
            clearInterval(timer);
        }, 2000)
    })
};

let poke_type;
function promptName(type) {
    $.ajax({
        url: server + "api/prompt-name",
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({"type": type}),
        dataType: 'json'
    }).done(function (result) {
        texts = result.texts
        counter = 0,
            timer = setInterval(function () {
                displayText(texts[counter]);
                counter++
                if (counter === texts.length) {
                    $('#name-input').show()
                    clearInterval(timer);
                }
            }, 2000)
        
    })
};

$('#poke-choice-buttons').on('click', '.choose-type', function(){
    poke_type = this.value;
    $('#poke-choice-buttons').hide();
    $('#main').html("")
    promptName(poke_type);
})