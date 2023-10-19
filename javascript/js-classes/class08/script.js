document.addEventListener('DOMContentLoaded', () => {
    // Loading cards
    const cardArray = [
        {
            name: 'ganhou',
            img: 'images/ganhou.png'
        },
        {
            name: 'ganhou',
            img: 'images/ganhou.png'
        },
        {
            name: 'correndo',
            img: 'images/correndo.png'
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
            name: 'direita',
            img: 'images/direita.png'
        },
        {
            name: 'ganhou',
            img: 'images/ganhou.png'
        },
        {
            name: 'ganhou',
            img: 'images/ganhou.png'
        },
    ]

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

    createBoard()
})