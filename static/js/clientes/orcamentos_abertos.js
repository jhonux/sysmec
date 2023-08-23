// $(document).ready(function () {
//     orcamentos_lista()
// })

// function getCookie(name) {
//     const value = `; ${document.cookie}`;
//     const parts = value.split(`; ${name}=`);
//     if (parts.length === 2) return parts.pop().split(';').shift();
// }

// function orcamentos_lista() {    
//     const url = `/clientes/orcamentos_lista/`;
//     const init = {
//         method: `GET`,
//         headers: {
//             "content-Type": "appliccation/json",
//             "Accept": "application/json",
//             "X-CSRFToken": getCookie("csrftoken"),
//         }
//     };

//     fetch(`${url}`, init)
//     .then(response => response.json())      
//     .then(response =>{
//         const orcamentos = response.orcamentos;

//         const tabelaOrcamentos = document.getElementById("tabela-orcamentos");

//         orcamentos.forEach(orcamento => {
//             const newRow = tabelaOrcamentos.insertRow();

//             newRow.innerHTML = `
//                 <td>${orcamento.cliente__nome}</td>
//                 <td>${orcamento.cliente__cpf}</td>
//                 <td>${orcamento.cliente__telefone}</td>
//                 <td>${orcamento.cliente__email}</td>
//                 <td>${orcamento.cliente__veiculo__modelo}</td>
//                 <td>${orcamento.cliente__veiculo__placa}</td>
//                 <td>${orcamento.valor_estimado}</td>
//                 <td>
//                     <button class="excluir-orcamento" data-id="${orcamento.id}">
//                         Excluir
//                     </button>
//                 </td>
//             `;
//         });
//     });
//     tabelaOrcamentos.addEventListener('click', function(event) {
//         const botaoExcluir = event.target;
//         if (botaoExcluir.classList.contains('excluir-orcamento')) {
//             const orcamentoId = botaoExcluir.getAttribute('data-id');
//             if (confirm('Tem certeza de que deseja excluir este orçamento?')) {
//                 excluirOrcamento(orcamentoId);
//             }
//         }
//     });
// }



// function excluirOrcamento(orcamentoId) {
//     // Faz uma solicitação HTTP ao seu backend para excluir o orçamento
//     fetch(`/clientes/orcamentos/${orcamentoId}/excluir/`, {
//       method: `DELETE`,
//       headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": getCookie("csrftoken"),
//       }
//     })
//     .then(response => response.json())
//     .then(response => {
//       // Se a solicitação for bem-sucedida, remove a linha da tabela
//       if (response.status === 200) {
//         const linhaOrcamento = document.querySelector(`tr[data-id="${orcamentoId}"]`);
//         linhaOrcamento.remove();
//       } else {
//         // Se a solicitação não for bem-sucedida, exibe uma mensagem de erro
//         alert("Ocorreu um erro ao excluir o orçamento.");
//       }
//     });
//   }
  
//   tabelaOrcamentos.addEventListener('click', function(event) {
//     const botaoExcluir = event.target;
//     if (botaoExcluir.classList.contains('excluir-orcamento')) {
//       const orcamentoId = botaoExcluir.getAttribute('data-id');
//       if (confirm('Tem certeza de que deseja excluir este orçamento?')) {
//         excluirOrcamento(orcamentoId);
//       }
//     }
//   });



function aprovarOrcamento(orcamentoId) {
    $.ajax({
        url: `/clientes/os_aberta/${orcamentoId}/`,
        method: 'GET',
        success: function(data) {
            // Atualize a tabela ou exiba uma mensagem de sucesso
            alert('Orçamento aprovado e transferido para a Ordem de Serviço Aberta.');
        },
        error: function(error) {
            alert('Ocorreu um erro ao aprovar o orçamento.');
        }
    });
}

setTimeout(function() {
    var messages = document.querySelectorAll('.message');
    messages.forEach(function(message) {
        message.style.display = 'none';
    });
}, 5000);
