$(document).ready(function () {
    clientes();
    contarOrcamentos();
})

function clientes() {    
    const url = `/clientes/clientes_lista/`;
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
        qtClientes(response.clientes_com_carro.length);
        
        // lista_clientes(response['lista'])
    });
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function qtClientes(qtdClientes) {
    const qtdClientesSpan = document.getElementById('qtdClientes');
    qtdClientesSpan.textContent = qtdClientes;
    console.log(qtdClientes)
}


function contarOrcamentos() {
    const url = `clientes//contar-orcamentos/`;  // Substitua pela URL correta
    const init = {
        method: `GET`,
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        }
    };

    fetch(url, init)
    .then(response => response.json())      
    .then(data => {
        const totalOrcamentos = data.total_orcamentos;
        console.log(totalOrcamentos)
        exibirTotalOrcamentos(totalOrcamentos);
    })
    .catch(error => {
        console.error('Erro ao obter o número de orçamentos:', error);
    });
}

function exibirTotalOrcamentos(totalOrcamentos) {
    const totalOrcamentosElement = document.getElementById('totalOrcamentos');  // Substitua pelo ID correto
    totalOrcamentosElement.textContent = totalOrcamentos;
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
