const URL = 'http://127.0.0.1:5000/addAppointment';
const METHOD = 'POST'
let request = {};

myForm.addEventListener('submit', event => {
    event.preventDefault()
    setBody();
    console.log(request);
    addAppointment();
})

function setBody() {
    request.name = nombre.value;
    request.phone = phone.value;
    request.email = email.value;
    request.location = ubicacion.value;
    request.symptom = symptom.value;
    request.date = date.value;
    request.time = time.value;

}

async function addAppointment() {
    try {
        const resp = await fetch(URL, {
            mode: 'cors', method: METHOD, headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }, body: JSON.stringify({ body: request })
        })
        console.log("todo ok");
        if(resp.status == 201){
        message.innerHTML = "sucess";
        message.style.clor = "green";
        }else{
            message.innerHTML = "error";
        }
    } catch (error) {
        message.innerHTML = "error";
        message.style.clor = "red";
    }

}