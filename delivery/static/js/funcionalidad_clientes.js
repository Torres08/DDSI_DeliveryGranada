
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

    data.append('accion', 'crear');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Intenta analizar la respuesta JSON
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
                console.error('Error en la solicitud AJAX:', xhr.status, xhr.statusText);

                // Muestra el mensaje de error en la consola
                var terminal = document.getElementById('terminal');
                terminal.innerHTML += '<p>Error en la solicitud AJAX: ' + xhr.statusText + '</p>';
            }
        }
    };
    xhr.send(data);

    return false;
}


function mostrarFormularioEliminar() {
    var formulario = document.getElementById('formulario-eliminar-cliente');
    formulario.style.display = 'block';
}

// Función para eliminar un cliente
function eliminarCliente() {
    var form = document.getElementById('eliminar-cliente-form');
    var data = new URLSearchParams(new FormData(form));

    data.append('accion', 'eliminar');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Intenta analizar la respuesta JSON
                var response = JSON.parse(xhr.responseText);

                // Mostrar el mensaje en la terminal
                var nombreCliente = document.getElementById('id_nombre_cliente').value;
                var terminal = document.getElementById('terminal');
                terminal.innerHTML += '<p>Se ha borrado el cliente ' + nombreCliente + '</p>';

            } else {
                console.error('Error en la solicitud AJAX:', xhr.status, xhr.statusText);

                // Muestra el mensaje de error en la consola
                var terminal = document.getElementById('terminal');
                terminal.innerHTML += '<p>Error en la solicitud AJAX: ' + xhr.statusText + '</p>';
            }
        }
    };
    xhr.send(data);

    return false;
}

















