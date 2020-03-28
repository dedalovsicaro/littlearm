

function sendServo(name, angle) {
	console.log('hola');


	var xhr = new XMLHttpRequest();
	xhr.open('GET', "http://192.168.8.102:5000/servo/base/5", true);
	xhr.send();
	 
	xhr.onreadystatechange = processRequest;
		
}

function processRequest(e) {
	console.log(e);	 
}
