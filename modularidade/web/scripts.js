var tela = '';

function mostrarMensagem(){
    var nome = document.getElementById("nome").value;
    alert('Boa noite, ' + nome + "!");
}

function apertarBotao(num){
    var telaElem = document.getElementById('tela');
    tela = telaElem.value + num;
    telaElem.value = tela; 
}