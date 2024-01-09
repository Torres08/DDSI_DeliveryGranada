
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

                // Mostrar mensaje en la terminal
                var terminal = document.getElementById('terminal');
                terminal.innerHTML += '<p>Nuevo cliente creado:</p>';
                terminal.innerHTML += '<p>ID: ' + response.cliente.id + '</p>';
                terminal.innerHTML += '<p>Nombre: ' + response.cliente.nombre + '</p>';
                terminal.innerHTML += '<p>Teléfono: ' + response.cliente.telefono + '</p>';
                terminal.innerHTML += '<p>Dirección: ' + response.cliente.direccion + '</p>';

                // Restablecer el formulario
                form.reset();

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

                // Eliminar la opción del cliente eliminado del select
                var selectElement = document.getElementById('id_nombre_cliente');
                var optionToRemove = selectElement.querySelector('option[value="' + nombreCliente + '"]');
                if (optionToRemove) {
                    selectElement.removeChild(optionToRemove);
                }


                // Limpiar el formulario después de eliminar el cliente
                form.reset();
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


function mostrarFormularioModificar() {
    var formularioModificar = document.getElementById('formulario-modificar-cliente');
    formularioModificar.style.display = 'block';
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function modificarCliente() {
    var form = document.getElementById('modificar-cliente-form');
    var nombreCliente = document.getElementById('id_nombre_cliente_modificar').value;
    var nuevoNombre = document.getElementById('id_nuevo_nombre').value;
    var nuevoTelefono = document.getElementById('id_nuevo_telefono').value;
    var nuevaDireccion = document.getElementById('id_nueva_direccion').value;

    var data = new FormData();
    data.append('accion', 'modificar');
    data.append('Nombre', nombreCliente);
    data.append('NuevoNombre', nuevoNombre);
    data.append('NuevoTelefono', nuevoTelefono);
    data.append('NuevaDireccion', nuevaDireccion);


    var csrftoken = getCookie('csrftoken');  // Asegúrate de tener una función para obtener el valor del token CSRF
    var xhr = new XMLHttpRequest();

    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('X-CSRFToken', csrftoken);  // Agrega el token CSRF a la solicitud

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Intenta analizar la respuesta JSON
                var response = JSON.parse(xhr.responseText);

                // Mostrar el mensaje en la terminal
                var terminal = document.getElementById('terminal');
                terminal.innerHTML += '<p>Cliente modificado: ' + nombreCliente + '</p>';
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






























