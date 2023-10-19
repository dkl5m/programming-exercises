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

    // Flipping cards
    function flipCard(){
        var cardId = this.getAttribute('data-id')
        cardsChosen.push(cardArray[cardId].name)
        cardsChosenId.push(cardId)
        this.setAttribute('src', cardArray[cardId].img)
        if(cardsChosen.length == 2){
            setTimeout(checkForMatch, 500)
        }
    }

    createBoard()
})