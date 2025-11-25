// frontend/scripts/books.js

async function loadBooks() {
    try {
        const books = await apiGet("/books");

        const table = document.getElementById("booksTable");
        table.innerHTML = "";

        books.forEach(book => {
            // genres pode ser lista de objetos {id, name}
            const genres = (book.genres || []).map(g => g.name || g).join(", ");
            const available = (book.copies_available && book.copies_available > 0) ? "Sim" : "Não";

            const row = `
                <tr class="hover:bg-gray-100">
                    <td class="p-3">${book.id}</td>
                    <td class="p-3">${book.title}</td>
                    <td class="p-3">${book.author}</td>
                    <td class="p-3">${genres}</td>
                    <td class="p-3">${available}</td>
                </tr>
            `;
            table.innerHTML += row;
        });

    } catch (err) {
        console.error("Erro ao carregar livros:", err);
        alert("Erro ao carregar livros. Veja o console para detalhes.");
    }
}

async function searchByGenre() {
    const genre = document.getElementById("genreInput").value.trim();
    if (!genre) { alert("Digite um gênero para buscar."); return; }

    try {
        // backend implementado com /books?genre=... ou /books/genre/{name}
        // Teste qual função seu backend expõe; aqui uso query param:
        const books = await apiGet(`/books?genre=${encodeURIComponent(genre)}`);

        const table = document.getElementById("booksTable");
        table.innerHTML = "";

        if (!books || books.length === 0) {
            table.innerHTML = `<tr><td class="p-3 text-center text-gray-500" colspan="5">Nenhum livro encontrado.</td></tr>`;
            return;
        }

        books.forEach(book => {
            const genres = (book.genres || []).map(g => g.name || g).join(", ");
            const available = (book.copies_available && book.copies_available > 0) ? "Sim" : "Não";
            const row = `
                <tr class="hover:bg-gray-100">
                    <td class="p-3">${book.id}</td>
                    <td class="p-3">${book.title}</td>
                    <td class="p-3">${book.author}</td>
                    <td class="p-3">${genres}</td>
                    <td class="p-3">${available}</td>
                </tr>
            `;
            table.innerHTML += row;
        });

    } catch (err) {
        console.error("Erro ao buscar livros por gênero:", err);
        alert("Erro ao buscar livros. Veja o console para detalhes.");
    }
}

window.onload = () => {
    loadBooks();
};
