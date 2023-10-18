<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style_index.css') }}">
    <title>მთავარი მენიუ</title>
</head>
<body>


<div class="menu_block">
    <div class="first_line_block">
        <div class="menu_element_block">
            <div class="el">
                <a href="/all">
                <img src="/static/images/all.webp" alt="Изображение"></a>
                <label>სია</label>
            </div>

            <div class="el">
                <a href="#" onclick="openAddModal()">
                    <img src="/static/images/add.webp" alt="Изображение">
                </a>
                <label>დამატება</label>
            </div>

            <div class="el">
                <a href="/storage">
                <img src="/static/images/storage.webp" alt="Изображение"></a>
                <label>საწყობი</label>
            </div>
        </div>

    </div>
    <div class="last_line_block">
        <div class="menu_element_block">
                <div class="el2">
                    <a href="#" onclick="openReservationModal()">
                        <img src="/static/images/booking.webp" alt="Изображение">
                    </a>
                    <label>ჯავშანი</label>
                </div>
                <div class="el2">
                    <a href="#" onclick="openModal()">
                        <img src="/static/images/blanks.png" alt="Изображение"></a>
                    <label>ბლანკები</label>
                </div>
                <div class="el2">
                    <a href="/logout">
                    <img src="/static/images/exit.webp" alt="Изображение"></a>
                    <label>გასვლა</label>
                </div>
        </div>  
    </div>
</div>


{% for cat, msg in get_flashed_messages(True) %}
<div class='flash {{cat}}'>{{msg}}</div>
{% endfor %}
<script>
// Скрыть все сообщения через 4 секунд
setTimeout(function() {
    var messages = document.querySelectorAll('.flash');
    for (var i = 0; i < messages.length; i++) {
        messages[i].style.display = 'none';
    }
}, 3000);
</script>


<!-- Модальное окно -->
<div id="myModal" class="modal-blanks-select">
    <div class="modal-blanks-content">
        <span class="close" onclick="closeModal()">&times;</span>
        <h2>ამოირჩიეთ გაგზავნის თარიღი</h2>
        <input type="date" id="datepicker">
        <label for="citySelect">ქალაქი:</label>
        <select id="citySelect">
            <option value="Санкт-Петербург">სანქტ-პეტერბურგი</option>
            <option value="Москва">მოსკოვი</option>
        </select>
        <button onclick="redirectToPage()">გადასვლა</button>
    </div>
</div>  


<!-- Модальное окно -->
<div id="ModalAdd" class="modal-add-select">
    <div class="modal-add-content">
        <span class="close" onclick="closeAddModal()">&times;</span>
        <h2>ამოირჩიეთ გაგზავნის თარიღი</h2>
        <input type="date" id="datepickerAdd">
        <button onclick="redirectAddPage()">გადასვლა</button>
    </div>
</div>  




<div id="reservationModal" class="modal-reservation">
    <div class="modal-reservation-content">
        <span class="close" onclick="closeReservationModal()">&times;</span>
        <h2>ამოირჩიეთ თარიღი და მარშრუტი</h2>
        <input type="date" id="reservationDate">
        <label for="routeSelect">მარშრუტი:</label>
        <select id="routeSelect">
            <option value="1">თბილისი-მოსკოვი</option>
            <option value="2">მოსკოვი-თბილისი</option>
        </select>
        <button onclick="redirectToReservationPage()">გადასვლა</button>
    </div>
</div>






<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/ru.js"></script>


<script>
function openModal() {
    const modal = document.getElementById('myModal');
    modal.style.display = 'block';

    // Инициализация календаря с использованием flatpickr
    const datepicker = flatpickr("#datepicker", {
        dateFormat: "d-m-Y", // Формат даты
        locale: "ru", // Установка русского языка
    });

    // Добавляем обработчик события на клавишу "Esc"
    window.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            closeModal();
        }
    });

    // Добавляем обработчик события на клик вне модального окна
    modal.addEventListener('click', function (event) {
        if (event.target === modal) {
            closeModal();
        }
    });
}

// Функция закрытия модального окна
function closeModal() {
    const modal = document.getElementById('myModal');
    modal.style.display = 'none';
}

// Функция перенаправления на страницу /list с выбранной датой
function redirectToPage() {
    const selectedDate = document.getElementById('datepicker').value;
    const selectedCity = document.getElementById('citySelect').value;
    
    if (selectedDate) {
        // Передаем выбранную дату и город в URL
        window.location.href = `/list?date=${selectedDate}&where_from=${selectedCity}`;
    }
}


</script>



<script>
    // Функция открытия модального окна
    function openReservationModal() {
        const modal = document.getElementById('reservationModal');
        modal.style.display = 'block';

        // Инициализация календаря с использованием flatpickr
        const datepicker = flatpickr("#reservationDate", {
            dateFormat: "Y-m-d", // Формат даты
            locale: "ru", // Установка русского языка
        });

        // Добавляем обработчик события на клавишу "Esc"
        window.addEventListener('keydown', function (event) {
            if (event.key === 'Escape') {
                closeReservationModal();
            }
        });

        // Добавляем обработчик события на клик вне модального окна
        modal.addEventListener('click', function (event) {
            if (event.target === modal) {
                closeReservationModal();
            }
        });
    }

    // Функция закрытия модального окна
    function closeReservationModal() {
        const modal = document.getElementById('reservationModal');
        modal.style.display = 'none';
    }

    // Функция перенаправления на страницу в зависимости от выбора
    function redirectToReservationPage() {
        const selectedDate = document.getElementById('reservationDate').value;
        const selectedRoute = document.getElementById('routeSelect').value;

        let destination = '/error'; // По умолчанию, если дата не подходит
        if (selectedDate) {
            if (selectedRoute === '1') {
                if (isThursday(selectedDate)) {
                    destination = '/reservation?date=' + selectedDate + '&route=1';
                } else if (isSunday(selectedDate)) {
                    destination = '/reservation_big?date=' + selectedDate + '&route=1';
                }
            } else if (selectedRoute === '2') {
                if (isWednesday(selectedDate)) {
                    destination = '/reservation_big?date=' + selectedDate + '&route=2';
                } else if (isSunday(selectedDate)) {
                    destination = '/reservation?date=' + selectedDate + '&route=2';
                }
            }

            // Перенаправляем пользователя на выбранную страницу
            window.location.href = destination;
        }
    }

    // Функция проверки, является ли день четвергом
    function isThursday(dateString) {
        const date = new Date(dateString);
        return date.getDay() === 4; // 4 представляет четверг (0 - воскресенье, 1 - понедельник, и так далее)
    }

    // Функция проверки, является ли день средой
    function isWednesday(dateString) {
        const date = new Date(dateString);
        return date.getDay() === 3; // 3 представляет среду
    }

    // Функция проверки, является ли день воскресеньем
    function isSunday(dateString) {
        const date = new Date(dateString);
        return date.getDay() === 0; // 0 представляет воскресенье
    }
</script>








<!--  -->


<script>
// Функция открытия второго модального окна
function openAddModal() {
    const modal = document.getElementById('ModalAdd');
    modal.style.display = 'block';

    // Инициализация календаря с использованием flatpickr
    const datepicker = flatpickr("#datepickerAdd", {
        dateFormat: "Y-m-d", // Формат даты
        locale: "ru", // Установка русского языка
    });

    // Добавляем обработчик события на клавишу "Esc"
    window.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            closeAddModal();
        }
    });

    // Добавляем обработчик события на клик вне модального окна
    modal.addEventListener('click', function (event) {
        if (event.target === modal) {
            closeAddModal();
        }
    });
}

// Функция закрытия второго модального окна
function closeAddModal() {
    const modal = document.getElementById('ModalAdd');
    modal.style.display = 'none';
}

function redirectAddPage() {
    const selectedDate = document.getElementById('datepickerAdd').value;
    console.log('Selected Date:', selectedDate);

    if (selectedDate) {
        // Преобразование даты в формат "год-месяц-день"
        const formattedDate = formatDate(selectedDate);

        // Перенаправление пользователя на страницу `/add` с выбранной датой
        window.location.href = '/add?date=' + formattedDate;
    }
}

// Функция форматирования даты в "год-месяц-день"
function formatDate(selectedDate) {
    const dateObject = new Date(selectedDate);
    const year = dateObject.getFullYear();
    const month = (dateObject.getMonth() + 1).toString().padStart(2, '0');
    const day = dateObject.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
}
</script>


<!--  -->






<div class="footer">
    <div class="footer-block">
        <h3>სამუშაო გრაფიკები:</h3>
        <p><strong>თბილისი:</strong></p>
        <p>ორშ-შაბ: 10:00 - 18:00</p>
        <p>კვირა: 10:00 - 17:00</p>
        <p><strong>ბათუმი:</strong></p>
        <p>ორშ-შაბ: 10:00 - 18:00</p>
        <p>კვირა: დაკტილია</p>
    </div>
    <div class="footer-block">
        <h3>თანამშრომელბის დასვენების გრაფიკი:</h3>
        <p><strong>გიორგი:</strong> ორშ & პარ</p>
        <p><strong>ჯემალი:</strong> სამშაბათი </p>
        <p><strong>დიმა:</strong> ხუთშაბათი</p>
        <p><strong>ერეკლე:</strong> კვირა</p>
        <p><strong>ზურა:</strong> კვირა </p>
    </div>
    <div class="footer-block">
        <h3>უკუკავშირი და შეცდომების გასწორება:</h3>
        <p>თუ თქვენ გაქვთ კითხვები, შეთავაზებები ან თქვენ იპოვეთ შეცდომა საიტზე, გთხოვთ, დაგვიკავშირდეთ:</p>
        <p>ტელეფონი: +995571181762</p>
        <p>Email: <a href="mailto:hardinhell@gmail.com">hardinhell@gmail.com</a></p>
    </div>
    <div class="footer-block">
        <h3>უსაფრთხოების პოლიტიკები და პროცედურები:</h3>
        <p>ჩვენ ვაფასებთ მონაცემების უსაფრთხოებას. გთხოვთ, არ გადასცეთ თქვენი აქაუნთის მონაცემები მესამე პირებს.</p>
        <p>შემთხვევაში თუ, ვინმემ როგორღაც გაიგო თქვენი აქაუნთის  მონაცემები, გთხოვთ დაუკავშირდით ადმინისტრატორს მონაცემების შესაცვლელად.</p>
    </div>
    <div class="footer-block">
        <p>&copy; 2023  -  "VIP-TOUR საერთაშორისო სატრანსპორტო კომპანია."</p>
        <p>ბოლო განახლება 17.10.2023</p>
    </div>
</div>


</body>

</html>
