
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

    // Mostrar los datos en la terminal
    var terminal = document.getElementById('terminal');
    terminal.innerHTML += '<p>Nuevo cliente creado:</p>';
    terminal.innerHTML += '<p>Nombre: ' + data.get('Nombre') + '</p>';
    terminal.innerHTML += '<p>Teléfono: ' + data.get('Telefono') + '</p>';
    terminal.innerHTML += '<p>Dirección: ' + data.get('Direccion') + '</p>';

    console.log("Nuevo cliente creado:");
    console.log("Nombre:", data.get('Nombre'));
    console.log("Teléfono:", data.get('Telefono'));
    console.log("Dirección:", data.get('Direccion'));

    // Ocultar el formulario después de enviar los datos
    var formulario = document.getElementById('formulario-crear-cliente');
    formulario.style.display = 'none';

    // Evitar que el formulario se envíe de forma tradicional
    return true;
}



