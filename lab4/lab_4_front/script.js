DjangoUrl = 'http://127.0.0.1:8000/beer/'

function ReadAll() {
	xhr = new XMLHttpRequest()
	xhr.open('GET', DjangoUrl)
	xhr.responseType = 'json'
	xhr.setRequestHeader('Content-Type', 'application/json')

	xhr.onload = function() {
		if (xhr.status >=400) {
			console.log(xhr.response)
		} else {
			element = document.getElementById("deductedlist")
			data = xhr.response
			text = ''
			for (let key of data.keys())
				text += 'id: '+data[key]['id']+'<br>'+
			"Name of company: "+data[key]['nameofcompany']+'<br>'+
			"type of beer: "+data[key]['typeofbeer']
			element.innerHTML = text
		}
	}
	xhr.send()
}

function ById() {
	element = document.getElementById('get_id').value
	xhr = new XMLHttpRequest()
	xhr.open('GET', DjangoUrl+'?id='+element)
	xhr.responseType = 'json'
	xhr.setRequestHeader('Content-Type', 'application/json')
	xhr.onload = function() {
		if (xhr.status >= 400) {
			console.log(xhr.response)
		} else {
			console.log(xhr.response)
			element = document.getElementById("by_id")
			data = xhr.response
			text = 'id: '+data['id']+'<br>'+
			"Name of company': "+data['nameofcompany']+'<br>'+
			"Type of beer: "+data['typeofbeer']
			element.innerHTML=text
		}
	}
	xhr.send()
}

function Add() {
	nameofcompany = document.getElementById('nameofcompany').value
	typeofbeer = document.getElementById('typeofbeer').value

	body = {
		nameofcompany: nameofcompany,
		typeofbeer: typeofbeer
	}

	xhr = new XMLHttpRequest()
	xhr.open('PUT', DjangoUrl)
	xhr.responseType = 'json'
	xhr.setRequestHeader('Content-Type', 'application/json')
	xhr.onload = function() {
		if (xhr.status >= 400) {
			console.log(xhr.response)
		} else {
			console.log(xhr.response)
		}
	}
	xhr.send(JSON.stringify(body))
}

// function Update() {
// 	nameofcompany = document.getElementById('upnameofcompany').value
// 	typeofbeer = document.getElementById('uptypeofbeer').value
	
//     body = {
// 		nameofcompany: nameofcompany,
// 		typeofbeer: typeofbeer
// 	}

// 	xhr = new XMLHttpRequest()
// 	xhr.open('POST', DjangoUrl)
// 	xhr.responseType = 'json'
// 	xhr.setRequestHeader('Content-Type', 'application/json')
// 	xhr.onload = function() {
// 		if (xhr.status >= 400) {
// 			console.log(xhr.response)
// 		} else {
// 			console.log(xhr.response)
// 		}
// 	}
// 	xhr.send(JSON.stringify(body))
// }

function Delete_all() {
	id = document.getElementById("delete_id").value

	body = {id: id}

	xhr = new XMLHttpRequest()
	xhr.open('DELETE', DjangoUrl)
	xhr.responseType = 'json'
	xhr.setRequestHeader('Content-Type', 'application/json')
	xhr.onload = function() {
		if (xhr.status >= 400) {
			console.log(xhr.response)
		} else {
			console.log(xhr.response)
		}
	}
	xhr.send(JSON.stringify(body))
}