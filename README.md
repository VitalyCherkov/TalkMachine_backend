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
        `id`: 1234
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

### **GET Conversation info**

**URL** `/conversations/[id]`

**RESPONCE 200**

```javascript
{
    'id': 1234
    'user': {
        'nickname': 'Nagibator',
        'name': 'Lev Tolstoy',
        'avatar': '/avatar/url'
    },
    'last_message': {
        'text': 'Kek kek kek kek kek ...'
        'author': 'AuthorNickname',
        'created': '20-12-2017'
    }
}
```

---

### **GET Conversation messages**

**URL** `/conversations/[id]/messages/page/[pageNumber]`

[id] - id диалога

[pageNumber] - номер страницы получаемых сообщений - на странице до 25 сообщений

**RESPONCE 200**

```javascript
[
    {
        'id': 12345
        'author': 'AuthorNickname',
        'created': '20-12-2017',
        'text': 'Kek kek kek kek kek', 
        'parent_id': 1012, // ID родительского сообщения. 0 - если корневое
        'edited': 'False', // Редактировалось ли данное сообщение
        'voted': 'True' // Добавлял ли текущий пользователь это сообщение в избранное
        'votes': 2
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
        'id': 1234,
        'name': 'Writers',
        'avatar': '/avatar/url',
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

### TODO: **GET Chat details**

**URL** `/chats/[id]/details`

**RESPONCE 200**

```javascript
{
    'id': 1234,
    'name': 'Writers',
    'avatar': '/avatar/url',
    'users_count': 12,
    'admin': 'AdminsNickname',
    'muted': 'True' // Если текущий пользователь замутил чат 
}
```

---

### TOOD: **GET Chat users**

**URL** `/chats/[id]/users`

**RESPONCE 200**

```javascript
[
    {
        'nickname': 'Nagibator',
        'name': 'Lev Tolstoy',
        'avatar': '/avatar/url'
        'inviter': 'InviterNickname',
        'canDelete': 'False' // Является ли данный пользователь дочерним по отношению к текущему в этом чате
    }
    // ... 
    { }
]
```

---

### TODO: **GET Chat messages**

**URL** `/chats/[id]/messages/page/[pageNumber]`

до 25 сообщений на страницу

**RESPONCE 200**

```javascript
[
    {
        'id': 12345
        'author': 'AuthorNickname',
        'created': '20-12-2017',
        'text': 'Kek kek kek kek kek', 
        'parent_id': 1012, // ID родительского сообщения. 0 - если корневое
        'edited': 'False', // Редактировалось ли данное сообщение
        'voted': 'True' // Добавлял ли текущий пользователь это сообщение в избранное
        'votes': 2
    },
    // ...
    {
        // ...
    }
]
```

---

### TODO: **POST Invite user to chat**

**URL** `/user/[id]/invite/[chatId]`

**RESPONCE 200** - empty

---

### TODO: **POST Edit chat**

**URL** `/chats/[id]/edit`

**REQUEST**

Принцип такой же, как и с редактирование пользователя

```javascript
{
    'name': 'New chat name',
}
```

**RESPONCE 200**

То же, что и в `/chats/[id]/details`

---

### TOOD: **POST Leave chat**

**URL** `/chats/[id]/leave`

**RESPONCE 200** - empty

---

### TODO: **POST Exclude user from chat**

**URL** `/chats/[id]/exclude/[userId]`

**RESPONCE 200** - empty

---

### TODO: **GET Voted messages** 

**URL** ``

**RESPONCE 200**

```javascript
```

---

### TODO: **GET Message**

**URL** `/message/[id]/details`

**RESPONCE 200**

```javascript
{
    'id': 12345,
    'text': 'message text',
    'author': {
        'nickname': 'AuthorNickname',
        'name': 'Lev Tolstoy'
    },
    'created': '20-11-2017',
    'votes': 12,
    'voted': 'False',
    'edited': 'True',
    'parent_id': 123,
    'conversation_id': 1245
    // или 'chat_id': 1234,
    // 'chat_name': 'Chat name' - если все-таки 'chat_id'
}
```

---

### TODO: **POST Cahnge vote for message**

**URL** `/message/[id]/vote`

**RESPONCE 200**

```javascript
{
    'votes': 10,
    'voted': 'False'
}
```

---

### TODO: **POST Edit message**

**URL** `/message/[id]/edit`

**REQUEST**

Такой же принцип как и при редактировании всего остального

```javascript
{
    'text': 'New message text',
    'parent_id': 10 // ID родительского сообщения
}
```

**RESPONCE 200**

Ананлогично `/message/[id]/details`

---

### TODO: **POST Delete message**

**URL** `/message/[id]/delete`

**RESPONCE 200** - empty

---