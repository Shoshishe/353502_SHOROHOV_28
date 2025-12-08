const selectedTable = document.querySelector("#bought-fur")

const tableRows = selectedTable.querySelectorAll(".bought-row")
let currentPage = 0;
let perPage = 3;
let countOfPages = Math.ceil((tableRows.length) / perPage);
const paginationContainer = document.querySelector("#pagination-container")


function showPage(tableRows, currentPage) {
    const tbody = selectedTable.querySelector('tbody');
    tbody.innerHTML = ''
    tableRows.forEach((row, index) => {
        if (!((index < currentPage * perPage) || (index >= currentPage * perPage + perPage))) {
            tbody.appendChild(row);
        }
    });
}

showPagination(tableRows, countOfPages);

function showPagination(tableRows, countOfPages) {
    paginationContainer.innerHTML = '';
    for (let i = 0; i < countOfPages; i++) {
        const pageButton = document.createElement('button');
        pageButton.textContent = i + 1;
        pageButton.addEventListener('click', () => {
            currentPage = i;
            showPage(tableRows, currentPage);
        });
        paginationContainer.appendChild(pageButton);
    }
    showPage(tableRows, currentPage);
}