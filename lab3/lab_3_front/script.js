function SquareArea() {
	xhr = new XMLHttpRequest()
	url = 'http://127.0.0.1:8000/SquareArea/'
	
	data = {input_value: document.getElementById('input').value}

	xhr.open('POST', url)
	xhr.setRequestHeader('Content-Type', 'application/json')

	xhr.onload = function() {
		response = JSON.parse(xhr.response)
		document.getElementById('output').innerHTML = 'Output: ' + response.output_value.toString()

	}

	xhr.send(JSON.stringify(data))
}