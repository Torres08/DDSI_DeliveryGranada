let listElements = document.querySelectorAll('.list_button--click');

listElements.forEach(listElement => {
    listElement.addEventListener('click', () => {
        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;

        // Corregir el error tipográfico: cambiar "clienteHeight" a "clientHeight"
        if (menu.clientHeight === 0) {
            height = menu.scrollHeight;
        }

        menu.style.height = height + "px";
    });
});