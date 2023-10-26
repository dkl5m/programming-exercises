document.addEventListener('DOMContentLoaded', () => {

    // references
    const dino = document.querySelector('.dino')
    const grid = document.querySelector('.grid')
    const body = document.querySelector('.body')
    const alert = document.querySelector('.alert')

    // vars
    let jumping = false
    let gravity = 0.9
    let gameo = false // game over
    let dinopy = 0 // dino position-y

    // data input
    document.addEventListener('keyup', jumpcontrol)

    // jump control
    function jumpcontrol(e){
        if(e.keyCode == 32){
            if(!jumping){
                jumping = true
                jump()
            }
        }
    }
    
    function jump(){
        let count = 0
        let timerId = setInterval(function(){
            // Going up
            dinopy += 30
            count ++
            dinopy = dinopy * gravity
            dino.style.bottom = dinopy + 'px'
        }, 20)
    }

})