function goToStep2() {

    const cursoSelecionado = document.querySelector(
        'input[name="curso"]:checked'
    );

    if (!cursoSelecionado) {
        alert("Por favor, selecione um curso!");
        return;
    }

    document.getElementById("form-step-1")
        .classList.remove("active");

    document.getElementById("form-step-2")
        .classList.add("active");
}


function goToStep3() {

    const cursoSelecionado = document.querySelector(
        'input[name="curso"]:checked'
    );

    const serieSelecionada = document.querySelector(
        'input[name="serie"]:checked'
    );

    if (!cursoSelecionado) {
        alert("Por favor, selecione um curso!");
        return;
    }

    if (!serieSelecionada) {
        alert("Por favor, selecione a sua série!");
        return;
    }

    const curso = cursoSelecionado.value;
    const serie = serieSelecionada.value;

    fetch(`/api/cursos/${curso}/disciplinas/?serie=${serie}`)
        .then(response => {

            if (!response.ok) {
                throw new Error("Erro ao buscar disciplinas.");
            }

            return response.json();
        })
        .then(disciplinas => {

            const lista = document.getElementById(
                "lista-disciplinas"
            );

            lista.innerHTML = "";

            if (disciplinas.length === 0) {

                lista.innerHTML = `
                    <p>
                        Nenhuma disciplina encontrada para
                        este curso e série.
                    </p>
                `;

            } else {

                disciplinas.forEach(disciplina => {

                    lista.innerHTML += `
                        <label class="course-balloon">

                            <input
                                type="checkbox"
                                name="disciplinas"
                                value="${disciplina.id}"
                            >

                            <div class="balloon-content">

                                <span>
                                    ${disciplina.nome}
                                </span>

                            </div>

                        </label>
                    `;

                });
            }

            document.getElementById("form-step-2")
                .classList.remove("active");

            document.getElementById("form-step-3")
                .classList.add("active");

        })
        .catch(error => {

            console.error(error);

            alert("Erro ao carregar as disciplinas.");

        });
}


function goToStep1() {

    document.getElementById("form-step-2")
        .classList.remove("active");

    document.getElementById("form-step-1")
        .classList.add("active");
}


function goToStep2From3() {

    document.getElementById("form-step-3")
        .classList.remove("active");

    document.getElementById("form-step-2")
        .classList.add("active");
}


function finalizarCadastro() {

    const nome = document.getElementById(
        "nome-usuario"
    ).value;

    const email = document.getElementById(
        "email-usuario"
    ).value;

    const senha = document.getElementById(
        "senha-usuario"
    ).value;

    const cursoSelecionado = document.querySelector(
        'input[name="curso"]:checked'
    );

    const serieSelecionada = document.querySelector(
        'input[name="serie"]:checked'
    );

    const disciplinasSelecionadas = document.querySelectorAll(
        'input[name="disciplinas"]:checked'
    );

    if (!cursoSelecionado) {
        alert("Selecione um curso.");
        return;
    }

    if (!serieSelecionada) {
        alert("Selecione uma série.");
        return;
    }

    const formData = new FormData();

    formData.append(
        "nome",
        nome
    );

    formData.append(
        "email",
        email
    );

    formData.append(
        "senha",
        senha
    );

    formData.append(
        "curso",
        cursoSelecionado.value
    );

    formData.append(
        "serie",
        serieSelecionada.value
    );

    disciplinasSelecionadas.forEach(
        function(disciplina) {

            formData.append(
                "disciplinas",
                disciplina.value
            );

        }
    );

    console.log("NOME:", nome);
    console.log("EMAIL:", email);
    console.log("CURSO:", cursoSelecionado.value);
    console.log("SÉRIE:", serieSelecionada.value);
    console.log(
        "DISCIPLINAS:",
        Array.from(disciplinasSelecionadas).map(
            disciplina => disciplina.value
        )
    );

    fetch("/cadastro/", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    })
    .then(response => {

        if (response.redirected) {

            window.location.href = response.url;

        } else {

            return response.text()
                .then(() => {

                    alert(
                        "Não foi possível concluir o cadastro."
                    );

                });

        }

    })
    .catch(error => {

        console.error(error);

        alert(
            "Erro ao realizar o cadastro."
        );

    });
}


function getCookie(name) {

    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {

        const cookies =
            document.cookie.split(";");

        for (let cookie of cookies) {

            cookie = cookie.trim();

            if (
                cookie.startsWith(
                    name + "="
                )
            ) {

                cookieValue =
                    decodeURIComponent(
                        cookie.substring(
                            name.length + 1
                        )
                    );

                break;
            }
        }
    }

    return cookieValue;
}