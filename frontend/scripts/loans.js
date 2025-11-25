// =======================================
//  CARREGAR EMPRÉSTIMOS ATIVOS
// =======================================

async function loadLoans() {
    try {
        const loans = await apiGet("/loans");

        const table = document.getElementById("loansTable");
        table.innerHTML = "";

        if (loans.length === 0) {
            table.innerHTML = `
                <tr>
                    <td colspan="5" class="p-4 text-center text-gray-500">Nenhum empréstimo ativo.</td>
                </tr>
            `;
            return;
        }

        loans.forEach(loan => {
            const row = `
                <tr class="hover:bg-gray-100">
                    <td class="p-3">${loan.id}</td>
                    <td class="p-3">${loan.book_title}</td>
                    <td class="p-3">${loan.user}</td>
                    <td class="p-3">${loan.date}</td>

                    <td class="p-3">
                        <button 
                            onclick="finishLoan(${loan.id})"
                            class="bg-green-500 hover:bg-green-700 text-white px-3 py-2 rounded">
                            Devolver
                        </button>
                    </td>
                </tr>
            `;
            table.innerHTML += row;
        });

    } catch (err) {
        console.error("Erro ao carregar empréstimos:", err);
        alert("Erro ao carregar empréstimos.");
    }
}

// =======================================
//  REALIZAR EMPRÉSTIMO
// =======================================

async function createLoan() {
    const bookId = document.getElementById("loanBookId").value.trim();
    const user = document.getElementById("loanUser").value.trim();

    if (!bookId || !user) {
        alert("Preencha todos os campos.");
        return;
    }

    try {
        await apiPost("/loans", {
            book_id: parseInt(bookId),
            user: user
        });

        alert("Empréstimo registrado com sucesso!");
        loadLoans();

    } catch (err) {
        console.error(err);
        alert("Erro ao registrar empréstimo.");
    }
}

// =======================================
//  FINALIZAR EMPRÉSTIMO
// =======================================

async function finishLoan(id) {
    if (!confirm("Confirmar devolução?")) return;

    try {
        await apiPut(`/loans/${id}/finish`, {});

        alert("Devolução registrada!");
        loadLoans();

    } catch (err) {
        console.error(err);
        alert("Erro ao finalizar empréstimo.");
    }
}

// =======================================
//  AUTOLOAD QUANDO A PÁGINA ABRE
// =======================================

window.onload = () => {
    loadLoans();
};
