

function sendServo(name, angle) {
	server = "http://192.168.8.102:5000/";
	console.log('hola');


	var xhr = new XMLHttpRequest();
	xhr.open('GET', server + "servo/"+name+"/"+angle, true);
	xhr.send();
	 
	xhr.onreadystatechange = processRequest;
		
}

function processRequest(e) {
	console.log(e);	 
}
