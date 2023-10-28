document.addEventListener('DOMContentLoaded', () => {

    // references
    const dino = document.querySelector('.dino')
    const grid = document.querySelector('.grid')
    const body = document.querySelector('body')
    const alert = document.getElementById('alert')

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
            // Falling
            if(count == 15){
                clearInterval(timerId)
                let downTimerId = setInterval(function(){
                    if(count == 0){
                        clearInterval(downTimerId)
                        jumping = false
                    }
                    dinopy -= 5
                    count--
                    dinopy = dinopy * gravity
                    dino.style.bottom = dinopy + 'py'
                }, 20)
            }
            // Going up
            dinopy += 30
            count ++
            dinopy = dinopy * gravity
            dino.style.bottom = dinopy + 'px'
        }, 20)
    }

    function generateObstacle(){
        let randomTime = Math.random()*4000
        let obstaclepx = 1000
        const obstacle = document.createElement('div')

        // Creating copies
        if(!gameo) obstacle.classList.add('obstacle')
        grid.appendChild(obstacle)
        obstacle.style.left = obstaclepx + 'px'

        // Game logic + obstacle moviment
        let timerId = setInterval(function() {
            // Player colision
            if(obstaclepx > 0 && obstaclepx < 60 && dinopy < 60){
                clearInterval(timerId)
                alert.innerHTML = 'Game Over'
                gameo = true
                // Removing copies
                body.removeChild(body.firstChild)
                while(grid.firstChild){
                    grid.removeChild(grid.lastChild)
                }
            }
            // Obstacle moviment to the left
            obstacle -= 10
            obstacle.style.left = obstaclepx = 'px'
        }, 20)

        if(!gameo) setTimeout(generateObstacle, randomTime)
    }

    generateObstacle()
})