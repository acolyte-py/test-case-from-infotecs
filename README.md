# Тестовое Задание от компании infotecs 📄
Данное задание на позицию стажера Автотестирование (Python) г. Томск.
В этом тест кейсе я старался сделать как можно больше, ну и конечно как понимаю. Не скажу, что работа
сделана идеально. Много минусов и пробелов на самом деле, которые должны были быть решены.
Я очень старался, так как хочу попасть к Вам на стажировку. Большое спасибо за эту возможность, и интересное задание 😊

# Getting Started ✅
Для разработки этого проекта использовалась ОС Windows. Данная настройка работает исключительно для ОС Windows.

### Installing 🔨
Установка проекта выполнится следующей командой:
```
git clone https://github.com/acolyte-py/test-case-from-infotecs.git
```
После установки в ваш каталог, необходимо установить зависимости.
```
pip install -r requirements.txt
```
Данный проект использует фреймворк Allure. Ссылка на его док:
``
https://docs.qameta.io/allure/#_get_started
``

Так же используется Docker:
``
https://docs.docker.com/desktop/install/windows-install/#install-docker-desktop-on-windows
``

# Running the tests 🐾
Для того чтобы запустить тесты, вы должны были выполнить пункт Installing.

### Pytest and Allure 🔴
Команда запустит тесты, и создаст директорию для Allure, там будет много json файлов не пугайтесь, это нужно
для красивого вывода в html формате. В пункте {YOU_DIR} укажите название директории, она будет в корне проекта.
```
pytest -v --alluredir={YOU_DIR}
```
После того как тесты прошли, результат не важен. Вы можете запустить в красивом формате вывод тестов, для глубого и удобно анализа тестов, командой:
```
allure serve {YOU_DIR}
```
У вас должен появится адрес, на html страницу. Пример адреса:
``
<http://192.168.188.1:51611/>
``

![chrome_3AC8plJMHt](https://user-images.githubusercontent.com/75732226/180754462-75520abb-a488-4f86-8c66-57ce2496895c.png)

![chrome_u6EtwBo6lA](https://user-images.githubusercontent.com/75732226/180754750-e44a3f30-7dc5-46e2-b3b4-351b736aa968.png)

### Pytest and Docker 🔵
В данном проекте есть готовый Dockerfile. С помощью которого вы можете запустить тесты
с помощью докера. Важная ремарка: "Docker Desktop должен быть установлен, и запущен".

Запустим следующую команду:
```
docker build -t {NAME_CONTAINER} .
```

После успешного созданного контейнера, мы можем его запустить командой:
```
docker run {NAME_CONTAINER}
```

В результате команды, мы должны увидеть вывод тестов.

## In Future 📌
Если бы мне задали вопрос, о будущем этого проекта, ну допустим, а что можно было бы сделать ещё?
Мой ответ был бы таков:
* Добавить возможность запуск Allure с Docker.
* Минимизировать размер контейнера.
* Ещё раз декомпозировать задачу, вдруг я упустил какую то не решенную логику в тестах.
* Улучшить имеющиеся тесты. В плане скорости выполнения и отлова ошибок (Негативных тестов).
* Добавить функционал CI например (GitLab-CI).

## Built With 🔧
* [Allure](https://docs.qameta.io/allure/) - Для отчетов о тестировании.
* [Pytest](https://docs.pytest.org/en/7.1.x/) - Для тестирования приложения.
* [Docker](https://docs.docker.com/) - Для автоматического запуска тестов.

## Authors 🗿

* **Миронов Миша** - *Изначальная работа* - [vk](https://vk.com/spikedt).

## License ©

Данный проект использует лицензию MIT - [LICENSE](LICENSE) для деталей.
