
// funcionalidades de crear usuarios y menus 
// 4 funcionalidades 
 
function mostrarFormulario() {
    console.log('Clic en "Crear Cliente"');
    var formulario = document.getElementById('formulario-crear-cliente');
    formulario.style.display = 'block';
}

function crearCliente() {
    var form = document.getElementById('cliente-form');
    var data = new FormData(form);

    // Enviar el formulario de manera asíncrona con AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Parsear la respuesta JSON
                var response = JSON.parse(xhr.responseText);

                // Mostrar los datos del cliente en la terminal
                var terminal = document.getElementById('terminal');
                terminal.innerHTML += '<p>Nuevo cliente creado:</p>';
                terminal.innerHTML += '<p>ID: ' + response.cliente.id + '</p>';
                terminal.innerHTML += '<p>Nombre: ' + response.cliente.nombre + '</p>';
                terminal.innerHTML += '<p>Teléfono: ' + response.cliente.telefono + '</p>';
                terminal.innerHTML += '<p>Dirección: ' + response.cliente.direccion + '</p>';

                // Ocultar el formulario después de enviar los datos
                var formulario = document.getElementById('formulario-crear-cliente');
                formulario.style.display = 'none';
            } else {
                // Manejar errores si la solicitud no fue exitosa
                console.error('Error en la solicitud AJAX:', xhr.status, xhr.statusText);
            }
        }
    };
    xhr.send(data);

    // Evitar que el formulario se envíe de forma tradicional
    return false;
}




