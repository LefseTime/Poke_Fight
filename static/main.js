const server = 'http://localhost:5000/'
let textSpeed = 500
let poke_type;
let poke_name;
let sad_sound;
let happy_sound;
let moves = ['Attack', 'Defend and Regenerate HP', 'Flail Helplessly', 'Choose for Itself'];

function displayText(text) {
    $('#main').append(`<p>${text}</p>`);
}

function timeout(texts, htmlement) {
    counter = 0,
        timer = setInterval(function () {
            displayText(texts[counter]);
            counter++
            if (counter === texts.length) {
                $(`${htmlement}`).show()
                clearInterval(timer);
            }
        }, textSpeed)
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
        }, textSpeed)
    })
};

function promptName(type) {
    $.ajax({
        url: server + "api/prompt-name",
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "type": type }),
        dataType: 'json'
    }).done(function (result) {
        texts = result.texts
        timeout(texts, "#name-input")
    })
};

function promptSad(poke_name) {
    $.ajax({
        url: server + "api/prompt-sad",
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "name": poke_name }),
        dataType: 'json'
    }).done(function (result) {
        texts = result.texts
        timeout(texts, '#sad-input')
    })
};

function promptHappy(poke_name) {
    $.ajax({
        url: server + "api/prompt-happy",
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "name": poke_name }),
        dataType: 'json'
    }).done(function (result) {
        texts = result.texts;
        timeout(texts, '#happy-input')
    })
};

function encounterWild() {
    $.ajax({
        url: server + "api/initialize-user",
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "type": poke_type, "name": poke_name, "happy": happy_sound, "sad": sad_sound }),
        dataType: 'json'
    }).done(function (result) {
        texts = result.texts
        user = result.user
        wild = result.wild
        counter = 0,
            timer = setInterval(function () {
                displayText(texts[counter]);
                counter++
                if (counter === texts.length + 1) {
                    clearInterval(timer);
                    displayHPChooseMove(user, wild)
                }
            }, textSpeed)
    })
}

function displayHPChooseMove(user, wild){
    $('#hp-status').show();
    $('#main').html("");
    $('#user-status').text(`${user.name}: ${user.hp}`)
    $('#wild-status').text(`${wild.name}: ${wild.hp}`)

    $('#move-choices').show();
    counter = 0
    moves.forEach(move => {
        counter++
        $('#move-choices').append(`<button type='button' class="choose-move" id="type" value="${counter}">${move}</button>`);
    });
}

function makeMove(move) {
    $.ajax({
        url: server + "api/round",
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "move": move }),
        dataType: 'json'
    }).done(function (result) {
        console.log(result)
    })
}

$('#begin').on('click', function () {
    $.ajax({
        url: server + "api/intro",
        method: 'GET',
        datatype: 'json'
    }).done(function (result) {
        $('#begin').hide();
        $('#main').show();
        let texts = result.texts
        timeout(texts, "#yes-no-song");
    })
})

$('#no-song').on('click', function () {
    $('#yes-no-song').hide();
    $('#main').html(`<p>Well, well then! Looks like you'll need a Poke, lil' whippersnapper!</p>`)
    chooseType();
})

$('#poke-choice-buttons').on('click', '.choose-type', function () {
    poke_type = this.value;
    $('#poke-choice-buttons').hide();
    $('#main').html("")
    promptName(poke_type);
})

$('#name-input-button').on('click', function () {
    poke_name = $('#name-input-text').val();
    $('#name-input').hide();
    $('#main').html("")
    promptSad(poke_name);
})

$('#sad-input-button').on('click', function () {
    sad_sound = $('#sad-input-text').val();
    $('#sad-input').hide();
    $('#main').html("")
    promptHappy(poke_name);
})

$('#happy-input-button').on('click', function () {
    happy_sound = $('#happy-input-text').val();
    $('#happy-input').hide();
    $('#main').html("")
    encounterWild();
})

$('#move-choices').on('click', '.choose-move', function () {
    move = this.value;
    $('#move-choices').hide();
    $('#main').html("")
    makeMove(move);
})