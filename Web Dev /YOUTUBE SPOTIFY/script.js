const incrementbtn = document.querySelector('#increment')

const decrementbtn = document.querySelector('#decrement')

let counter = 0

function incrementcounter(){
    const counterEl = document.getElementById('counter')
    counter++
    counterEl.innerText = counter
}

function decrementcounter(){
    if(counter === 0){
        return 0
    }
    const counterEl = document.getElementById('counter')
    counter--
    counterEl.innerText = counter
}

incrementbtn.addEventListener('click', incrementcounter)
decrementbtn .addEventListener('click', decrementcounter)