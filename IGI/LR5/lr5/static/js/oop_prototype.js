// 28. Дан массив объектов, содержащий сведения о пассажирах авиакомпании: фамилия,
// имя, отчество пассажира, номер рейса. Выяснить, имеются ли на данном рейсе
// однофамильцы, если да, то указать их ФИО.

const FullName = {
    surname: '',
    name: '',
    set propName(value) {
        this.name = value;
    },
    get propName() {
        return this.name;
    },
    propSurname(value) {
        this.surname = value;
    },
    get propSurname() {
        return this.surname;
    },
    constructor(pName, pSurname) {
        this.name = pName;
        this.surname = pSurname;
    }
}

const personsOutput = document.querySelector("#oop-data")

const full = Object.create(FullName);

let Person = {
    __proto__: full,
    flight: '',
    constructor(name, surname, flight) {
        super(name, surname);
        this.flight = flight;
    },

    set propFlight(value) {
        this.flight = value;
    },
    get propFlight() {
        return this.flight;
    },

    outputHtml() {
        let table = document.createElement("table");
        let thead = document.createElement('thead');
        let th = document.createElement('th');
        th.textContent = "Name";
        thead.appendChild(th);
        th = document.createElement('th');
        th.textContent = "Surname";
        thead.appendChild(th);
        th = document.createElement('th');
        th.textContent = "Flight";
        thead.appendChild(th);
        table.appendChild(thead)

        let tbody = document.createElement('tbody')
        persons.forEach((person) => {
            let tr = document.createElement('tr')
            let td = document.createElement('td')
            td.textContent = person.propName
            tr.appendChild(td)
            td = document.createElement('td')
            td.textContent = person.propSurname
            tr.appendChild(td)

            td = document.createElement('td')
            td.textContent = person.propFlight
            tr.appendChild(td)
            tbody.appendChild(tr)
        })
        table.appendChild(tbody);
        personsOutput.innerHTML = '';
        personsOutput.appendChild(table);

        let filter = document.createElement('input')
        filter.setAttribute('type', "text")
        filter.addEventListener('input', (event) => {
            this.outputFiltered(event.target.value);
        })
        personsOutput.appendChild(filter)
    },

    outputFiltered(flight) {
        let surnames = new Set()
        let personsOnBoard = persons.filter((person) => person.propFlight === flight)
        for (let i = 0; i < personsOnBoard.length; i++) {
            for (let j = i; j < personsOnBoard.length; j++) {
                if (personsOnBoard[i].propSurname === personsOnBoard[j].propSurname) {
                    surnames.add(personsOnBoard[i].propSurname);
                }
            }
        }
        const filteredSection = document.querySelector("#oop-filtered");
        filteredSection.innerHTML = '';
        let list = document.createElement('ul');
        surnames.forEach((surname) => {
            let li = document.createElement('li');
            li.textContent = surname;
            list.appendChild(li);
        })
        filteredSection.appendChild(list);
    },

    createFromForm() {
        let surname = document.querySelector("#oop-surname");
        let name = document.querySelector("#oop-name");
        let flight = document.querySelector("#oop-flight");

        persons.push(new Person(name.value, surname.value, flight.value));
        this.outputHtml()
    }
}

let formSubmit = document.querySelector('#oop-submit');
formSubmit.addEventListener('click', () => {
    Person.createFromForm();
})

let persons = [new Person("Aliaksandr", "Klochko", "ab7"), new Person("Misha", "Klochko", "ab7"), new Person("Darya", "Minich", "nb6")];
Person.outputHtml()
