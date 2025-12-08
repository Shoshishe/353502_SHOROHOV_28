const customInputsContainer = document.querySelector('#custom-inputs');
const inputCreate = document.querySelector("#input-create");

let customInputs = localStorage.getItem("custom-inputs");
if (customInputs === null) {
    customInputs = '';
}

let customInputsArr = customInputs.split(/(?<=<article[^>]*>(.*?)<\/article>)/gis).filter((val, index) => {
    return val.includes("article") && index % 2 == 0
});

customInputsContainer.innerHTML = customInputsArr.join('');


let curIndex = 0;
let active = true;

Array.from(customInputsContainer.children).forEach((elem) => {
    elem.children.item(1).addEventListener('click', () => {
        let input = elem.children.item(0);
        let dataActive = elem.children.item(0).getAttribute('data-active')
        let active = dataActive === "true";

        active = !active
        if (!active) {
            elem.children.item(0).style.webkitTextSecurity = ''
        } else {
            elem.children.item(0).style.webkitTextSecurity = 'disc'
        }
        input.setAttribute('data-active', active.toString())
    })
    elem.children.item(2).addEventListener('click', () => {
        let forDeletion = document.querySelector(elem.children.item(2).getAttribute('data-row-id'))
        forDeletion.remove();
        customInputsArr = customInputsArr.filter((val) => {
            return !val.includes(forDeletion.id)
        })
    })
})

inputCreate.addEventListener('click', () => {
    let prevIndex = curIndex;

    let content = document.createElement('article')
    let curId = crypto.randomUUID();

    // content.id = "_".concat(curId.toString())
    content.style.border = '1px solid var(--text-color)';
    content.style.display = 'flex';
    content.style.justifyContent = 'space-around';
    content.style.alignItems = 'baseline';
    content.style.flexDirection = 'column';

    let input = document.createElement('input');
    input.setAttribute('type', 'tel');
    input.style.webkitTextSecurity = 'disc';

    let inputNameLabel = document.createElement('label');
    inputNameLabel.textContent = "Name";
    let inputName = document.createElement('input');
    inputName.addEventListener('input', (event) => {
        input.setAttribute('name', event.target.value)
        customInputsArr[prevIndex] = (inputWrapper.outerHTML)
    })

    let inputReadonlyLabel = document.createElement('label');
    inputReadonlyLabel.textContent = "Readonly";
    let inputReadonly = document.createElement('input');
    inputReadonly.type = 'checkbox';
    inputReadonly.addEventListener('click', (event) => {
        if (event.target.checked) {
            input.readOnly = true;
        } else {
            input.readOnly = false;
        }
        customInputsArr[prevIndex] = (inputWrapper.outerHTML)
    })

    let inputRequiredLabel = document.createElement('label');
    inputRequiredLabel.textContent = "Required";
    let inputRequired = document.createElement('input')
    inputRequired.type = 'checkbox'
    inputRequired.addEventListener('click', (event) => {
        if (event.target.checked) {
            input.required = true;
        } else {
            input.required = false;
        }
        customInputsArr[prevIndex] = (inputWrapper.outerHTML)
    })

    let inputPlaceholderLabel = document.createElement('label');
    inputPlaceholderLabel.textContent = "Placeholder";
    let inputPlaceholder = document.createElement('input');
    inputPlaceholder.addEventListener('input', (event) => {
        input.setAttribute('placeholder', event.target.value);
        customInputsArr[prevIndex] = (inputWrapper.outerHTML);

    })

    let inputValueLabel = document.createElement('label');
    inputValueLabel.textContent = "Value";
    let inputValue = document.createElement('input');
    inputValue.addEventListener('input', (event) => {
        input.setAttribute('value', event.target.value);
        customInputsArr[prevIndex] = (inputWrapper.outerHTML);

    })


    let inputMaxLengthLabel = document.createElement('label');
    inputMaxLengthLabel.textContent = "Max length";
    let inputMaxLength = document.createElement('input');
    inputMaxLength.type = 'number';
    inputMaxLength.addEventListener('input', (event) => {
        input.maxLength = parseInt(event.target.value, 10);
        customInputsArr[prevIndex] = (inputWrapper.outerHTML);
    })

    let inputLabel = document.createElement("label");
    inputLabel.textContent = "Input:"

    let inputWrapper = document.createElement('article');
    inputWrapper.style.cssText = 'position: relative; width: 300px;'
    let button = document.createElement('button')
    button.style.position = 'absolute';
    button.style.top = '50%';
    button.style.transform = 'translateY(-50%)';
    button.style.right = '50%'
    button.addEventListener('click', () => {
        let dataActive = input.getAttribute('data-active')
        let active = dataActive === "true";
        active = !active
        if (!active) {
            input.style.webkitTextSecurity = ''
        } else {
            input.style.webkitTextSecurity = 'disc'
        }
        input.setAttribute('data-active', active.toString())
        customInputsArr[prevIndex] = (inputWrapper.outerHTML);
    })
    inputWrapper.append(input, button);
    let deleteButton = document.createElement('button')
    deleteButton.textContent = "Delete";
    deleteButton.style.alignSelf = 'flex-end';
    deleteButton.setAttribute('data-row-id', "#_".concat(curId.toString()));
    deleteButton.addEventListener('click', () => {
        let forDeletion = document.querySelector("#_".concat(curId.toString()))
        forDeletion.remove();
        customInputsArr.filter((val) => {
            return !val.includes(forDeletion.id)
        })
    })

    inputWrapper.appendChild(deleteButton);
    inputWrapper.id = "_".concat(curId.toString());

    content.append(inputNameLabel, inputName, document.createElement('br'), inputReadonlyLabel, inputReadonly, document.createElement('br'), inputRequiredLabel, inputRequired, document.createElement('br'), inputPlaceholderLabel, inputPlaceholder, document.createElement('br'), inputValueLabel, inputValue, document.createElement('br'), inputMaxLengthLabel, inputMaxLength, document.createElement('br'), inputLabel, inputWrapper);
    customInputsContainer.appendChild(content);

    customInputsArr.push(inputWrapper.outerHTML)
    curIndex++;
})

window.onbeforeunload = function () {
    this.localStorage.setItem("custom-inputs", customInputsArr.join(''))
}
