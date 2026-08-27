function goToStep2() {
    const cursoSelecionado = document.querySelector('input[name="curso"]:checked');

    if (!cursoSelecionado) {
        alert("Por favor, selecione um curso!");
        return;
    }

    document.getElementById("form-step-1").classList.remove("active");
    document.getElementById("form-step-2").classList.add("active");
}

function goToStep3() {
    const serieSelecionada = document.querySelector('input[name="serie"]:checked');

    if (!serieSelecionada) {
        alert("Por favor, selecione a sua série!");
        return;
    }

    document.getElementById("form-step-2").classList.remove("active");
    document.getElementById("form-step-3").classList.add("active");
}

function goToStep1() {
    document.getElementById("form-step-2").classList.remove("active");
    document.getElementById("form-step-1").classList.add("active");
}

function goToStep2From3() {
    document.getElementById("form-step-3").classList.remove("active");
    document.getElementById("form-step-2").classList.add("active");
}

function finalizarCadastro() {
    alert("Cadastro concluído com sucesso!");
}