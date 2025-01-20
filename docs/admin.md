**API Документация для административной панели Alimon Warehouse**


# Управление товарными запасами:
## 1 - Добавление товара
Пользователь добавляет новый товар в ассортимент
### `POST` /api/v1/admin/products/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Request Data
```json
{
    "sku": 1234567890,
    "title": "Название товара",
    "description": "Описание товара",
    "price": 1200.00,
    "stock_quantity": 5,
    "is_active": true,
    "unit_id": 1,
    "category_id": 1
}
```
#### Responses
##### 201
```json
{
    "message": "Товар создан",
    "data":  {
        "sku": 1234567890,
        "title": "Название товара",
        "description": "Описание товара",
        "price": 1200.00,
        "stock_quantity": 5,
        "is_active": true,
        "unit": {
            "title": "шт"
        },
        "category": {
            "name": "Категория"
        }
    }
}
```
##### 400
```json
{
    "message": "Некорректные данные",
    "data": {
            "price":  "Поле должено содержать только числа",
            "stock_quantity": "Поле должено содержать только числа",
            "is_active": "Поле должно содержать только логическое значение",
            ...
    }
}
```
##### 409
```json
{
    "message": "Ошибка запроса 404",
    "data": {
            "unit_id":  "Единицы измерения с ID={unit_id} нет в системе",
            "category_id": "Категории с ID={category_id} нет в системе"
        }
}
```
## 2 - Обновление информации о товаре 
Пользователь обновляет информацию о товаре
### `PUT` /api/v1/admin/products/{product_id}/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Request Data 
```json
{
    "sku":1234567890,
    "title":"Наименование товара",
    "description":"Описание товара",
    "price":1200.00,
    "stock_quantity": 10,
    "is_active":true,
    "unit_id":1,
    "category_id":2
}
```
#### Responses 
##### 200
```json
{
    "message": "Информация о товаре обновлена.",
    "data": {
        "id": 1,
        "sku": 1234567890,
        "title": "Наименование товара",
        "description": "Описание товара",
        "price": 1200.00,
        "stock_quantity": 10,
        "is_active": true,
        "unit": {
            "title": "шт",
            ...
        },
        "category": {
            "name": "Категория",
            ...
        }
    }   
    
}
```
##### 400
```json
{
    "message": "Некорректные данные",
    "data": {
            "price":  "Поле должено содержать только числа",
            "stock_quantity": "Поле должено содержать только числа",
            "is_active": "Поле должно содержать только логическое значение",
            ...
        }
}
```
##### 404
```json
{
    "message": "Такого товара нет в системе",
    "data": [
        "id": 1
    ]
}
```
## 3 - Удаление товара 
Пользователь удаляет товар из системы
### `DELETE` /api/v1/admin/products/{product_id}/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Responses 

##### 204
```json
No content
```
##### 404
```json
{
    "message": "Такого товара нет в системе",
    "data": [
        "id": 1
    ]
}
```
## 4 - Добавление категории
### `POST` /api/v1/admin/categories/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Request Data
```json
{
    "title": "Наименование категории",
    "description": "Описание категории"
}
```
#### Responses
##### 201
```json
{
    "message": "Категория успешно создана",
    "data": {
        "id": 1,
        "title": "Наименование категории",
        "description": "Описание категории",
        "slug": "naimenovanie-categorii"
    }
}
```
##### 400
```json
{
    "message": "Данные введены некорректно",
    "data": {
        "title": "Поле не должно быть пустым",
        ...
    }
}
```
## 5 - Получение списка категорий
### `GET`   /api/v1/admin/categories/
#### Headers
```json
{
    "Authorization": "Bearer {access_token}"
}
```
#### Request Query Params
```
{
    "page": 1,
    "size": 24
}
```
#### Responses
#### 200
```json
{
    "message": "Категории успешно получены",
    "page": 1,
    "size": 24,
    "data": [
        {
        "id": 1
        "title": "Наименование категории",
        "slug": "naimenovanie-kategorii"
        }, 
        ...
    ]
}
```
## 6 - Обновление информации о карегории
### `PUT` /api/v1/admin/categories/{category_id}/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Request Data
```json
{
    "title": "Наименование категории",
    "description": "Описание катогрии"
}
```
#### Responses
##### 200
```json
{
    "message": "Данные успешно обновлены",
    "data": {
        "id": 1,
        "title": "Наименование категории",
        "description": "Описание катогрии",
        "slug": "naimenovanie-kategorii"
    }
}
```
##### 400
```json
{
    "message": "Данные введены некорректно",
    "data": {
        "title": "Поле не должно быть пустым",
        ...
    }
}
```
##### 404
```json
{
    "message": "Такой категории нет в системе",
    "data": {
        "id": 2
    }
}
```
## 7 - Удаление карегории
### `DELETE` /api/v1/admin/categories/{cateogry_id}/
#### Headers 
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Responses 
##### 204
```json
No content
```
##### 404
```json
{
    "message": "Такой категории нет в системе",
    "data": {
        "id": 2
    }
}
```
## 9 - Создание единицы измерения
### `POST` /api/v1/admint/units/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Request Data
```json
{
    "title": "шт"
}
```
#### Responses
#### 201
```json
{
    "message": "Единица измерения успешно сохдана",
    "data": {
        "title": "шт",
        "id": 1
    }
}
```
#### 400
```json
{
    "message": "Данные введены некорректно",
    "data":{
        "title": "Поле не дожно быть пустым"
    }
}
```
## 10 - Обновление информации о единице измерения
### `PUT` /api/v1/admin/units/{unit_id}/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Request Data
```json
{
    "title": "шт"
}
```
#### Responses
#### 200
```json
{
    "message": "Единица измерения успешно изменениа",
    "data": {
        "title": "шт",
        "id": 1
    }
}
```
#### 400
```json
{
    "message": "Данные введены некорректно",
    "data":{
        "title": "Поле не дожно быть пустым"
    }
}
```
### 404 
```json
{
    "message": "Такой единицы измерения нет в системе",
    "data": {
        "id": 1
    }
}
```
## 11 - Удаление единицы измерения
### `DELETE` /api/v1/units/{unit_id}/
#### Headers
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {access_token}"
}
```
#### Responses
#### 204
```json
No content
```
### 404 
```json
{
    "message": "Такой единицы измерения нет в системе",
    "data": {
        "id": 1
    }
}
```
# 2. Отслеживание остатков на складе
## 1 - Получение текущих остатков товаров
### `GET` /api/v1/admin/stocks/
## 2 - Резервирование товаров при оформлении заказов
### `GET` /api/v1/admin/reserves/
## 3 - Списание товаров при отгрузке
### `POST` /api/v1/admin/word-downs/
# 3. Обработка поступлений и списаний
## 1 - Регистрация поступлений товаров на склад
### `POST` /api/v1/admin/receipts/
## 2 - Списание товаров при продаже или утилизации
### `POST` /api/v1/admin/receipts/
## 3 - Корректировка остатков (инвентаризация)
# 4. Интеграция с другими сервисами
## 