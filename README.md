# **TalkMachine Backend**

_Будет дорабатываться  впроцессе реализации проекта_

## Содержание

* Ошибки и сообщения
    * Атомарное сообщение
    * Классификация кодов сообщений
    * Ошибки форм

* API

## Ошибки и сообщения

### Атомарное сообщение
Все сообщения и ошибки ошибки в конечном счете состоят из комбинации (или только из самой одной) атомарных ошибок. Атомарная ошибка характеризуется тремя параметрами: **кодом**,  **текстом** и **данными**.

```javascript
// atomic message object (AEO)
{
    'c': 1234, // 'c' - Code - код сообщения. Всего одна буква, т.к. таких сообщений очень много, поэтому есть смысл сэкономить объем
    't': 'Message text' // 't' - Text - текст сообщения.
    'd': 'tolstoy@lev.ru' // 'd' - Data (Данные). Опционально, если, например, это поле заполнено корректно и нам нужно сохранить его значение
}
```

### Классификация кодов сообщений

// TODO:

Здесь пока ничего нет, но идея такова: сообщения AJAX будут в одном диапазоне значений, а сообщения Websocket в другом диапазоне.

Также в кажом диапазоне есть поддиапазоны для информационных сообщений, сообщений об ошибке и (возможно) сообщений об успешном заверешнии

Пример:

```
[-------------- AJAX -------------][----------- Websocket -----------]
 [-- suc --][-- log --][-- err --]  [-- suc --][-- log --][-- err --]
```

Код до 2х байт:

Маска
```
[ , ] [ , ] [ , , , ] [ , , , , , , , ]
 код   рез.   тема         подтема
```
* Код
    * 00 - AJAX
    * 01 - WS
* Рез. (результат) _использование всех кодов, конечно, под вопросом) но пусть лучше будет_
    * 00 - Success
    * 01 - Info
    * 10 - Error
    * 11 - Warning

### Ошибки форм

```javascript
{
    // ошибки формы в целом
    'global': [
        {}, {}, {} // list of AEO
    ],
    // ошбики к каждому полю конкретно
    'fields': [
        'fieldname': [
            {}, {}, {} // list of AEO
        ],
        // ...
        'last_field': [
            {}, {}, {} // list of AEO
        ]
    ]
}
```

### Сообщения

**Ошибки**

```javascript
// incorrect email format
{
    'c': 000, // TODO:
    't': 'Incorrect email format'
}
```

```javascript
// Email already in use
{
    'c': 000, // TODO:
    't': 'Email already in use'
}
```

```javascript
// Nickname already in use
{
    'c': 000, // TODO:
    't': 'Nickname already in use'
}
```


```javascript
// Incorrect password length
{
    'c': 000, // TODO:
    't': 'Minimum length 8 characters'
}
```

```javascript
// Passwords do not match
{
    'c': 000, // TODO:
    't': 'Passwords do not match'
}
```

```javascript
// Incorrect email or password
{
    'c': 000, // TODO:
    't': 'Incorrect email or password'
}
```

```javascript
// Required field
{
    'c': // TODO:
    't': 'Required field'
}
```

```javascript
// Logout error
{
    'c': 000, // TOOD:
    't': 'Can not log out'
}
```

```javascript
// User deleted
{
    'c': // TODO:
    't': 'User deleted'
}
```

```javascript
// User deleted
{
    'c': // TODO:
    't': 'Message deleted'
}
```

## API

---

### **GET Me**

**URL** `/user/me`

**RESPONCE 200**
```javascript
{
    'nickname': 'Nagibator',
    'name': 'Lev Tolstoy'
    'email': 'lev.tolstoy@ya.ru'
    'avatar': '/avatar/url' // url аватара
    'bio': 'A Russian writer who is regarded as one of the greatest authors of all time'
}
```

---

### **GET User Details**

**URL** `/user/[nickname]/details`

[nickname] - никнейм пользователя, о котором запрашивается информция

**RESPONCE 200**
```javascript
{
    'nickname': 'Nagibator',
    'name': 'Lev Tolstoy',
    'avatar': '/avatar/url' // url аватара
    'bio': 'A Russian writer who is regarded as one of the greatest authors of all time',
    'last_seen': '20:11 15-11-2017'
}
```

---

### **GET User Short**

**URL** `/user/[nickname]/short`

[nickname] - никнейм пользователя, о котором запрашивается информция

**RESPONCE 200**
```javascript
{
    'nickname': 'Nagibator',
    'name': 'Lev Tolstoy',
    'avatar': '/avatar/url'
}
```

**RESPONCE  with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

---

### **POST Add user to contacts**

**URL** `/user/[nickname]/add`

[nickname] - никнейм пользователя, о котором запрашивается информция

**REQUEST** - empty

**RESPONCE 200** - empty 

**RESPONCE  with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

---

### **POST Remove user form contacts**

**URL** `/user/[nickname]/remove`

[nickname] - никнейм пользователя, о котором запрашивается информция

**REQUEST** - empty

**RESPONCE 200** - empty 

**RESPONCE  with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

---

### **POST Login**

**URL** `/user/login`

**REQUEST**

```javascript
{
    'email': 'example@example.com',
    'password': 'qwerty123'
}
```

**RESPONCE** 200 - аналогично `/user/me`

**RESPONCE  with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

---

### **POST Registration**

**URL** `/user/register`

**REQUEST**

```javascript
{
    'email': 'lev.tolstoy@ya.ru',
    'nickname': 'Lyova',
    'password': 'qwerty123'
}
```

**RESPONCE 200** - аналогично `/user/me`

**RESPONCE with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

---

### **POST Logout**

**URL** `/user/logout`

**REQUEST** - empty

**RESPONCE 200**

```javascript
{
    'c': 000, // TODO:
    't': 'Logged out successfully'
}
```

**RESPONCE with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

---

### **POST Edit User**

**URL** `/user/edit`

**REQUEST**

Если поле не редактируется, то его нет в JSON, если поле затирается, например, хочется удалить bio, то просто его значением передается пустая строка: `'bio': ''`

```javascript
{
    'password': 'new_password123',
    'nickname': 'newNickname',
    'bio': 'New bio',
    'name': 'Sanya Pushkin'
}
```

**RESPONCE 200** - аналогично `/user/me`

**RESPONCE with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

--- 

### **GET Contacts**

**URL** `/contacts/page/[pageNumber]`

[pageNumber] - номер страницы получаемых контактов. На одной странице по 25 контактов.

**RESPONCE 200**

```javascript
[
    {
        'nickname': 'Nagibator',
        'name': 'Lev Tolstoy',
        'avatar': '/avatar/url'
    },
    // ...
    {
        'nickname': 'BabkasKiller',
        'name': 'Raskolnikov R',
        'avatar': '/avatar/url'
    }
]
```

**RESPONCE with errors**

Ошибки согласно формату ошибки форм и сообщениям согласно задекларированным

---

### **GET Convesations list**

**URL** `/conversations/page/[pageNumber]`

[pageNumber] - номер страницы получаемых диалогов. На одной странице 25 диалогов.

**RESPONCE 200**

```javascript
[
    {
        'user': {
            'nickname': 'Nagibator',
            'name': 'Lev Tolstoy',
            'avatar': '/avatar/url'
        },
        'last_message': {
            'text': 'Kek kek kek kek kek ...'
            'sender': 'SenderNickname',
            'created': '20-12-2017'
        }
        
    },
    // ...
    {
        // ...
    }
]
```

---

### **GET Chats list**

**URL** `/chats/page/[pageNumber]`

[pageNumber] - номер страницы получаемых чатов. На одной странице 25 чатов.

**RESPONCE 200**

```javascript
[
    {
        'chat': {
            'Namve': 'Writers',
            'avatar': '/avatar/url'
        },
        'last_message': {
            'text': 'Kek kek kek kek kek ...'
            'sender': 'SenderNickname',
            'created': '20-12-2017'
        }
        
    },
    // ...
    {
        // ...
    }
]
```
