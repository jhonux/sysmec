$(document).ready(function () {
    servicos();
    configurarFormulario();
})

function configurarFormulario() {
    const select = document.getElementById("cliente-select");
    const buscarButton = document.getElementById("buscar-button");

    buscarButton.addEventListener("click", function () {
        const selectedClientId = select.value;
        if (selectedClientId) {
            // Realize ações com o ID do cliente selecionado, como enviar para o servidor
            console.log("Cliente selecionado:", selectedClientId);
        } else {
            console.log("Nenhum cliente selecionado");
        }
    });
}

function servicos() {    
    const url = `/servicos/get_clientes_lista/`;
    const init = {
        method: `GET`,
        headers: {
            "content-Type": "application/json",
            "Accept": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        }
    };

    fetch(`${url}`, init)
    .then(response => response.json())      
    .then(response =>{
        console.log(response)
        qtClientes(response.clientes_com_carro);
        
        // lista_clientes(response['lista'])
    });


}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}




