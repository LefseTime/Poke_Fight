const server = 'http://localhost:5000/'

$('#begin').on('click', function () {
    $.ajax({
        url: server + "api/intro",
        method: 'GET',
        datatype: 'json'
    }).done(function (result) {
        console.log(result)
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
            }, 3000)
        
    })
})

$('#no-song').on('click', function () {
    $('#yes-no-song').hide();
    $('#main').html(`<p>Well, well then! Looks like you'll need a Poke, lil' whippersnapper!</p>`)
    chooseType();
})

$('.choose-type').on('click', function(){
    console.log('yooo')
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
            displayText("Which Poke do you choose?")
            types.forEach(type => {
                displayText(`<button class="choose-type" value="${type}">${type}</button>`);
            });
            clearInterval(timer);
        }, 2000)
    })
};