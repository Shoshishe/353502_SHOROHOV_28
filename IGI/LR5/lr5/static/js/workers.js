const selectedTable = document.querySelector("#contacts-table")
const tableRows = selectedTable.querySelectorAll(".contact-info")

const tableHeaders = selectedTable.querySelectorAll('th');

const paginationContainer = document.querySelector(".pagination-container")
let currentPage = 0;
let perPage = 3;
let countOfPages = Math.ceil((tableRows.length) / perPage);

function addHeaderSorting(tableRows) {
    tableHeaders.forEach((header, index) => {
        header.addEventListener('click', () => {
            const tbody = selectedTable.querySelector('tbody');
            let rows = Array.from(tableRows).slice(currentPage * perPage, currentPage * perPage + perPage);

            rows.sort((a, b) => {
                return a.children.item(index).textContent.localeCompare(b.children.item(index).textContent)
            });

            tbody.innerHTML = '';
            rows.forEach(row => { tbody.appendChild(row); addRowCallback(row) });
        });
    });
}

function showPage(tableRows, currentPage) {
    const tbody = selectedTable.querySelector('tbody');
    tbody.innerHTML = ''
    tableRows.forEach((row, index) => {
        if (!((index < currentPage * perPage) || (index >= currentPage * perPage + perPage))) {
            tbody.appendChild(row);
            let cloned = row.children.item(4).children.item(0).cloneNode(true);
            row.children.item(4).replaceChild(cloned, row.children.item(4).children.item(0));
            row.children.item(4).children.item(0).addEventListener('change', (event) => {
                if (event.target.checked) {
                    addAwarded(row);
                } else {
                    removeAwarded(row);
                }
            })
            addRowCallback(row);
        } else {

        }
    });
    addHeaderSorting(tableRows);
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


const filterSubmit = document.querySelector('#contacts-filter');
const filterText = document.querySelector('#contacts-filter-data')

filterSubmit.addEventListener('click', () => {
    let rows = Array.from(tableRows);
    let keep = []
    const filtered = filterText.value
    rows.forEach((row) => {
        for (let i = 0; i < row.children.length; i++) {
            if (row.children.item(i).textContent.includes(filtered)) {
                keep.push(row);
                break;
            }
        }
    })

    const tbody = selectedTable.querySelector('tbody');
    tbody.innerHTML = '';
    keep.forEach((row) => {
        tbody.appendChild(row)
        addRowCallback(row);
    })
    showPagination(keep, Math.ceil(keep.length / perPage))
})

const descriptionField = document.querySelector("#contact-description")

const descriptionHead = document.createElement('thead')
function initDescriptionHead() {
    let th = document.createElement('th');
    th.textContent = 'Name';
    descriptionField.appendChild(th);
    th = document.createElement('th');
    th.textContent = 'Phone number';
    descriptionField.appendChild(th);
    th = document.createElement('th');
    th.textContent = 'Email';
    descriptionField.appendChild(th);
    th = document.createElement('th');
    th.textContent = 'Description';
    descriptionField.appendChild(th);
    th = document.createElement('th');
    th.textContent = 'Photo';
    descriptionField.appendChild(th);
}

function addRowCallback(row) {
    row.addEventListener('click', () => {
        descriptionField.innerHTML = '';
        initDescriptionHead();
        let tr = descriptionField.appendChild(document.createElement('tr'))
        let td = document.createElement('td')
        Array.from(row.children).forEach((child, index) => {
            if (!child.innerHTML.includes('input')) {
                td = document.createElement('td')
                td.style.verticalAlign = 'middle'
                td.innerHTML = child.innerHTML;
                tr.appendChild(td);
            }
        })
    })
}

function checkEvent() {

}


const addFormButton = document.querySelector("#addForm")
const addFormContainer = document.querySelector("#addFormContainer")

addFormButton.addEventListener('click', () => {
    let form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("enctype", "multipart/form-data");
    form.setAttribute("action", "js_test");

    let fullName = document.createElement("input");
    fullName.setAttribute("type", "text");
    fullName.setAttribute("name", "username");
    fullName.setAttribute("placeholder", "Full Name");

    let email = document.createElement("input");
    email.setAttribute("type", "text");
    email.setAttribute("name", "email");
    email.setAttribute("placeholder", "email@example.com");

    let phone = document.createElement("input");
    phone.setAttribute("type", "tel");
    phone.setAttribute("name", "phone");
    phone.setAttribute("placeholder", "+375291486733");

    phone.addEventListener('input', (event) => {
        const phoneInput = event.target.value;
        if (!validatePhone(phoneInput)) {
            phone.style.border = "2px solid var(--red)"
            phone.style.color = "var(--pink)"
        } else {
            phone.style.border = ""
            phone.style.color = ""
        }
    })

    let description = document.createElement("input");
    description.setAttribute("type", "url");
    description.setAttribute("name", "description");
    description.setAttribute("placeholder", "https://rnd-name-havent-thought/index.php");

    description.addEventListener('input', (event) => {
        const descriptionInput = event.target.value;
        if (!/^http(s)?:\/\/.*(\.php|\.html)$/.test(descriptionInput)) {
            description.style.border = "2px solid var(--red)"
            description.style.color = "var(--pink)"
        } else {
            description.style.border = '';
            description.style.color = '';
        }
    })

    let photo = document.createElement("input");
    photo.setAttribute("type", "file");
    photo.setAttribute("accept", "image/*");
    photo.setAttribute("name", "photo");

    let submit = document.createElement("input");
    submit.setAttribute("type", "submit");
    submit.disabled = true;

    form.appendChild(fullName);
    form.appendChild(email);
    form.appendChild(phone);
    form.appendChild(description)
    form.appendChild(photo)
    form.appendChild(submit)

    const fields = [fullName, email, phone, description];
    photo.addEventListener('change', () => {
        let filled = true;
        for (const field of fields) {
            if (field.value.trim() === '') {
                filled = false;
                break;
            }
        }
        if (!validatePhone(phone.value) || (!/^http(s)?:\/\/.*(\.php|\.html)$/.test(description.value))) {
            submit.disabled = true;
            return
        }
        submit.disabled = !filled;
    })
    fields.forEach((field) => {
        field.addEventListener('input', () => {
            let filled = true;
            for (const field of fields) {
                if (field.value.trim() === '') {
                    filled = false;
                    break;
                }
            }
            if (!validatePhone(phone.value) || (!/^http(s)?:\/\/.*(\.php|\.html)$/.test(description.value))) {
                submit.disabled = true;
                return
            }
            submit.disabled = !filled;
        })
    })

    addFormContainer.appendChild(form)

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        let isValid = true;
        const phoneInput = phone.value;
        const descriptionInput = description.value;
        if (!validatePhone(phoneInput)) {
            isValid = false;
        }
        if (!/^http(s)?:\/\/.*(\.php|\.html)$/.test(descriptionInput)) {
            isValid = false;
        }
        if (isValid) {
            form.submit();
        }
    })
})

function validatePhone(phone) {
    return /^((\+375)|8)((\((0)?\d{2}\))|( (0)?\d{2} )|((0)?\d{2})|( \((0)?\d{2}\) ))((\d{7})|(\d{3}-\d{2}-\d{2})|(\d{3} \d{2} \d{2}))$/.test(phone)
}

const awardedSection = document.querySelector('#contact-awarded')
let awarded = []

function addAwarded(row) {
    awarded.push((row.children).item(0).textContent)
    awardedSection.innerHTML = `Awarded workers are: ${awarded.join(',')}`
}

function removeAwarded(row) {
    let i = awarded.findIndex((elem) => {
        return elem === (row.children).item(0).textContent
    })
    awarded.splice(i, 1);
    if (awarded.length === 0) {
        awardedSection.innerHTML = ''
        return
    }
    awardedSection.innerHTML = `Awarded workers are: ${awarded.join(',')}`
}