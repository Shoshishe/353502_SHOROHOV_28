let result = null;
while (result === null || Date.parse(result) || Date.parse(result) - Date.now() <= 0) {
    result = prompt("Enter your date of birth: ", "1970-01-01")
}
let date = Date.parse(result) - Date.now();
let years = Math.ceil(date / 1000 / 60 / 60 / 24 / 365);
if (years >= 18) {
    alert(new Date().toLocaleDateString('en-US', { weekday: 'long' }))
} else {
    alert("Oh no, you should ask your parents for permission!");
}

