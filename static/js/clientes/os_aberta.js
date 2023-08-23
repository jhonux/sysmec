$(document).ready(function () {
    ordem_lista()
})

function ordem_lista() {    
    const url = `/clientes/ordem_lista/`;
    const init = {
        method: `GET`,
        headers: {
            "content-Type": "appliccation/json",
            "Accept": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        }
    };

    fetch(`${url}`, init)
    .then(response => response.json())      
    .then(response =>{
        console.log(response)
        qtOrdem(response.result_query.length);
    });
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function qtOrdem(qtdOrdem) {
    const qtdOrdemSpan  = document.getElementById('qtdOrdem');
    qtdOrdemSpan .textContent = qtdOrdem;
    console.log(qtdOrdem)
}