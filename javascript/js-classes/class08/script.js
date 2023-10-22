document.addEventListener('DOMContentLoaded', () => {
    
    // Loading cards
    const cardArray = [
        {
            name: 'ganhou',
            img: 'images/ganhou.png'
        },
        {
            name: 'correndo',
            img: 'images/correndo.png'
        },
        {
            name: 'direita',
            img: 'images/direita.png'
        },
        {
            name: 'esquerda',
            img: 'images/esquerda.png'
        },
        {
            name: 'tras',
            img: 'images/tras.png'
        },
        {
            name: 'pulo',
            img: 'images/pulo.png'
        },{
            name: 'ganhou',
            img: 'images/ganhou.png'
        },
        {
            name: 'correndo',
            img: 'images/correndo.png'
        },
        {
            name: 'direita',
            img: 'images/direita.png'
        },
        {
            name: 'esquerda',
            img: 'images/esquerda.png'
        },
        {
            name: 'tras',
            img: 'images/tras.png'
        },
        {
            name: 'pulo',
            img: 'images/pulo.png'
        }
    ]

    cardArray.sort(() => 0.5 - Math.random())

    const grid = document.querySelector('.grid')
    const resultDisplay = document.querySelector('#result')
    var cardsChosen = []
    var cardsChosenId = []
    var pairs = []

    // Creating game screen
    function createBoard(){
        for(let i=0; i<cardArray.length; i++){
            var card = document.createElement('img')
            card.setAttribute('src', 'images/card.png')
            card.setAttribute('data-id', i)
            card.addEventListener('click', flipCard)
            grid.appendChild(card)
        }
    }

    // Checking pairs
    function checkforMatch(){
        var cards = document.querySelectorAll('img')
        const optionOneId = cardsChosenId[0]
        const optionTwoId = cardsChosenId[1]

        // Click twice in the same card
        if(optionOneId == optionTwoId){
            cards[optionOneId].setAttribute('src', 'images/card.png')
            cards[optionTwoId].setAttribute('src', 'images/card.png')
            alert("You clicked on the same image!")
        }

        // Making a pair
        else if(cardsChosen[0] == cardsChosen[1]){
            alert("You made a pair!")
            cards[optionOneId].setAttribute('src', 'images/white.png')
            cards[optionTwoId].setAttribute('src', 'images/white.png')
            cards[optionOneId].removeEventListener('click', flipCard)
            cards[optionTwoId].removeEventListener('click', flipCard)
            pairs.push(cardsChosen)
        }
        // Doesn't made a pair
        else {
            cards[optionOneId].setAttribute('src', 'images/card.png')
            cards[optionTwoId].setAttribute('src', 'images/card.png')
            alert("Ops! Play again :)")
        }
        cardsChosen = []
        cardsChosenId = []
        resultDisplay.textContent = pairs.length

        if(pairs.length == cardArray.length/2){
            resultDisplay.textContent = "Congratulations! You found all the pairs!"
        }
    }

    // Flipping cards
    function flipCard(){
        var cardId = this.getAttribute('data-id')
        cardsChosen.push(cardArray[cardId].name)
        cardsChosenId.push(cardId)
        this.setAttribute('src', cardArray[cardId].img)
        if(cardsChosen.length == 2){
            setTimeout(checkforMatch, 500)
        }
    }

    createBoard()
})