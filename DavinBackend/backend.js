var cors = require('cors')


function send_data()
{
  let _name = document.getElementById("name").value;
  let _age = document.getElementById("age").value;
  let _gender= document.getElementById("gender").value;
  let _locality= document.getElementById("locality").value;
  let data = {
    name: _name,
    age: _age,
    gender: _gender,
    locality: _locality,
  };
  fetch("http://127.0.0.1:8000/data/api/", {
    method: 'POST',
    headers: {
        'Accept': 'text/plain',
        'Content-Type': 'text/plain',
        'Access-Control-Allow-Origin': '*',
    },
    mode:'cors',
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(response => console.log(JSON.stringify(response)))
}

function saveToDb() {


  let _name = document.getElementById("name").value;
  let _age = document.getElementById("age").value;
  let _gender= document.getElementById("gender").value;
  let _locality= document.getElementById("locality").value;
  let data = {
    name: _name,
    age: _age,
    gender: _gender,
    locality: _locality,
  };

  let xhr = new XMLHttpRequest();
  xhr.open("POST", "http://127.0.0.1:8000/data/api/");
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      console.log(xhr.status);
      console.log(xhr.responseText);
    }};

    data = JSON.stringify(data)

  xhr.send(data);
}