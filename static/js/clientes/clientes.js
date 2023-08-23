$(document).ready(function () {
    clientes()
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

// function montaTabela(data) {
//     const tabela = document.getElementById("tabela-cliente");
//     const tbody = tabela.querySelector("tbody");

//     data.forEach(cliente => {
//         const veiculo = cliente.veiculo__modelo + " - " + cliente.veiculo__placa;

//         const newRow = document.createElement("tr");
//         newRow.innerHTML = `
//             <td>${cliente.nome}</td>
//             <td>${cliente.telefone}</td>
//             <td>${cliente.email}</td>
//             <td>${cliente.veiculo__modelo}</td>
//             <td>${cliente.veiculo__placa}</td>
//             <td>
//             <a class="cliente-detalhe" href="#" data-toggle="modal" data-target="#clienteModal ${cliente.id} ">
//                 <i class="fas fa-eye ml-2" title="Ver detalhes"></i>
//             </a>
//             </td>
//         `;

//         tbody.appendChild(newRow);
//     });
// }

$(document).ready(function() {
    var clientsPerPage = 10; // Número de clientes por página
    var currentPage = 1;     // Página inicial

    function showClientsOnPage(page) {
        var startIndex = (page - 1) * clientsPerPage;
        var endIndex = startIndex + clientsPerPage;

        $('#clientesTable tbody tr').hide(); // Oculta todas as linhas
        $('#clientesTable tbody tr').slice(startIndex, endIndex).show(); // Mostra as linhas da página atual

        currentPage = page;
        updatePaginationControls();
    }

    function updatePaginationControls() {
        // ... (seu código para atualizar os botões de página anterior/próxima)
    }

    // Inicialização: mostrar os clientes na primeira página
    showClientsOnPage(currentPage);

    // Controle de clique para a página anterior
    $('#prevPage').click(function() {
        if (currentPage > 1) {
            showClientsOnPage(currentPage - 1);
        }
    });

    // Controle de clique para a próxima página
    $('#nextPage').click(function() {
        showClientsOnPage(currentPage + 1);
    });
});

document.getElementById('searchInput').addEventListener('input', function () {
    const searchText = this.value.toLowerCase();
    const tableRows = document.querySelectorAll('#clientesTable tbody tr');

    tableRows.forEach(row => {
        const rowData = row.textContent.toLowerCase();
        if (rowData.includes(searchText)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});


const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
searchButton.addEventListener('click', () => {
  const inputValue = searchInput.value;
  alert(inputValue);
});