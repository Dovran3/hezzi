# Your back will be like a blog [tproger.ru](https://tproger.ru/)

## It's just training for you, so we'll go step by step:

### 1. Posts (CRUD)

```http
GET http://localhost:3000/posts/all
```

```http
GET http://localhost:3000/posts/{:id}
```

```http
POST http://localhost:3000/posts
```

```http
PUT http://localhost:3000/posts/{:id}
```

```http
DELETE http://localhost:3000/posts/{:id}
```

### 2. Example of 'Post'

```json
{
    "id": "int",
    "user": "str",
    "user_image": "image_url",
    "content": "str",
    "content_title": "str",
    "content_image": "image_url",
    "views": "int",
    "likes": "int",
    "created_at": "str"
}
```

> ***I'll add other things, when you'll say done.***

![patient](./images/anticipation.jpeg)
