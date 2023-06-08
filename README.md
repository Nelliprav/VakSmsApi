# VakSmsApi - Документация

Установка самого модуля

```shell
pip install VakSmsApi
```

Устанавливаем ещё одну библиотеку для работы модуля

```shell
pip install requests
```

[Список сервисов](https://vak-sms.com/api/vak/#serviceCodeList1)

[Список стран и операторов](https://vak-sms.com/api/vak/#countryOperatorList1)

Аргументы инфо:

- `service` - Код сайта, сервиса, соц. сети
- `country` - Код страны номера телефона
- `operator` - Необязательный параметр. Имя оператора
- `tel` - Номер телефона на который ранее был получен код из СМС
- `idNum` - ID операции
  - `status="send"` - Еще СМС
  - `status="end"` - Отмена номера
  - `status="bad"` - Номер уже использован, забанен

Варианты ошибок:

```json
{"error": "apiKeyNotFound"}  # Неверный API ключ.
{"error": "noService"}  # Данный сервис не поддерживается, свяжитесь с администрацией сайта.
{"error": "noNumber"}  # Нет номеров, попробуйте позже.
{"error": "noMoney"}  # Недостаточно средств, пополните баланс.
{"error": "noCountry"}  # Запрашиваемая страна отсутствует.
{"error": "noOperator"}  # Оператор не найден для запрашиваемой страны.
{"error": "badStatus"}  # Неверный статус.
{"error": "idNumNotFound"}  # Неверный ID операции.
{"error": "badService"}  # Неверный код сайта, сервиса, соц. сети.
{"error": "badData"}  # Отправлены неверные данные.
```

Пример кода:

```python
from VakSmsApi import *

api = VakSmsApi(api_key="API КЛЮЧ")

# Баланс пользователя, в рублях
balance = api.get_balance()
print(balance)

# Получить информацию об сервисе
get_count_num = api.get_count_number(service="СЕРВИС", country="СТРАНА", operator="ОПЕРАТОР")
print(get_count_num)

# Получение временного номера
get_num = api.get_number(service="СЕРВИС", country="СТРАНА", operator="ОПЕРАТОР")
print(get_num)

# Продление полученного ранее номера
get_progl = api.prolongNumber(service="СЕРВИС", tel="НОМЕР ТЕЛЕФОНА")
print(get_progl)

# Изменение статуса
status_change = api.change_status

(idNum="ID временного номера", status="Статус")
print(status_change)

# Получить SMS
sms = api.get_sms(idNum="ID временного номера")
print(sms)
```
