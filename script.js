const API_URL = "http://127.0.0.1:5000/users"; // URL base da API

// Elementos do DOM
const userList = document.getElementById("user-list");
const createForm = document.getElementById("create-form");
const editForm = document.getElementById("edit-form");
const editSection = document.getElementById("edit-section");

// Funções de Validação
function validateName(name) {
    if (!name || name.trim() === "") {
        return "Name is required and must be between 1 and 80 characters.";
    }
    if (name.length > 80) {
        return "Name is required and must be between 1 and 80 characters.";
    }
    return null; // Sem erros
}

function validateEmail(email) {
    if (!email || email.trim() === "") {
        return "Email is required and must be no longer than 50 characters.";
    }
    if (email.length > 50) {
        return "Email must be no longer than 50 characters.";
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        return "Invalid email format.";
    }
    return null; // Sem erros
}

// Exibir mensagens de erro
function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    if (message) {
        errorElement.textContent = message;
    } else {
        errorElement.textContent = "";
    }
}

// Função para buscar e exibir usuários
async function fetchUsers() {
    const response = await fetch(API_URL);
    const users = await response.json();

    userList.innerHTML = ""; // Limpa a lista antes de atualizá-la
    users.forEach(user => {
        const userDiv = document.createElement("div");
        userDiv.className = "list-group-item d-flex flex-column";
        userDiv.innerHTML = `
            <div>
                <strong>ID:</strong> ${user.id} |
                <strong>Nome:</strong> ${user.name} |
                <strong>Email:</strong> ${user.email} |
                <strong>Criado em:</strong> ${user.created_at} |
                <strong>Atualizado em:</strong> ${user.updated_at || "N/A"}
            </div>
            <div class="mt-2 d-flex gap-2">
                <button class="btn btn-warning btn-sm" onclick="editUser(${user.id}, '${user.name}', '${user.email}')">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="deleteUser(${user.id})">Excluir</button>
            </div>
        `;
        userList.appendChild(userDiv);
    });
}

// Função para criar usuário
createForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("create-name").value;
    const email = document.getElementById("create-email").value;

    // Validações
    const nameError = validateName(name);
    const emailError = validateEmail(email);

    showError("create-name-error", nameError);
    showError("create-email-error", emailError);

    // Interrompe o envio se houver erros
    if (nameError || emailError) {
        return;
    }

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email }),
    });

    if (response.ok) {
        alert("Usuário criado com sucesso!");
        fetchUsers();
        createForm.reset();
    } else {
        const errorData = await response.json();
        alert(`Erro: ${errorData.error}`);
    }
});

// Função para excluir usuário
async function deleteUser(id) {
    const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });

    if (response.ok) {
        alert("Usuário excluído com sucesso!");
        fetchUsers();
    } else {
        const errorData = await response.json();
        alert(`Erro: ${errorData.error}`);
    }
}

// Função para exibir o formulário de edição com os dados do usuário
function editUser(id, name, email) {
    document.getElementById("edit-id").value = id;
    document.getElementById("edit-name").value = name;
    document.getElementById("edit-email").value = email;

    editSection.style.display = "block"; // Exibe o formulário de edição
}

// Função para cancelar a edição
function cancelEdit() {
    editSection.style.display = "none"; // Oculta o formulário
    editForm.reset(); // Reseta os campos do formulário
}

// Função para salvar alterações no usuário
editForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const id = document.getElementById("edit-id").value;
    const name = document.getElementById("edit-name").value;
    const email = document.getElementById("edit-email").value;

    // Validações
    const nameError = validateName(name);
    const emailError = validateEmail(email);

    showError("edit-name-error", nameError);
    showError("edit-email-error", emailError);

    // Interrompe o envio se houver erros
    if (nameError || emailError) {
        return;
    }

    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email }),
    });

    if (response.ok) {
        alert("Usuário atualizado com sucesso!");
        fetchUsers();
        cancelEdit();
    } else {
        const errorData = await response.json();
        alert(`Erro: ${errorData.error}`);
    }
});

// Carrega a lista de usuários ao iniciar
fetchUsers();
