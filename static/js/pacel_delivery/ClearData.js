document.getElementById('clearButton').addEventListener('click', function () {
    // Очищаем таблицу
    const tableBody = document.getElementById('parcelTableBody');
    tableBody.innerHTML = ''; // Удаляем все строки таблицы

    // Очищаем поле поиска по трекингу
    const trackingInput = document.getElementById('trackingInput');
    trackingInput.value = ''; // Очищаем поле "Трекинг"

    // Очищаем поле поиска по имени
    const nameInput = document.getElementById('nameInput');
    nameInput.value = ''; // Очищаем поле "Имя"

    // Очищаем поле "Получатель"
    const recipientInput = document.getElementById('recipient');
    if (recipientInput) recipientInput.value = ''; // Очищаем поле "Получатель"

    // Очищаем поле паспорта
    const passportInput = document.getElementById('passport');
    passportInput.value = ''; // Очищаем поле паспорта

    // Снимаем выделение с радио-кнопок
    const citizenshipRadios = document.querySelectorAll('input[name="citizenship"]');
    citizenshipRadios.forEach(radio => radio.checked = false); // Снимаем выбор с радио-кнопок

    // Снимаем выделение с чекбоксов (если они были выбраны)
    const checkboxes = document.querySelectorAll('#parcelTableBody input[type="checkbox"]');
    checkboxes.forEach(checkbox => checkbox.checked = false); // Снимаем выделение с чекбоксов

    // Снимаем выделение с чекбокса "Выбрать все"
    const selectAllCheckbox = document.getElementById('selectAll');
    selectAllCheckbox.checked = false; // Снимаем выделение с чекбокса "Выбрать все"
});
