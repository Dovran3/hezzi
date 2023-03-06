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

### 3. Athorization and Authentication

Now it's time to work with JWT (JSON Web Token)

- First of all read about it https://dev.to/kcdchennai/how-jwt-json-web-token-authentication-works-21e7
- And of course watch the videos about it
- Try to understand (read and watch many times)
- And when you'll think, that you're ready - it's time to write

#### Tasks
1. Sign Up
```http
POST http://localhost:3000/sign_up
```

```json
{
    "username": "nickname",
    "password": "password"
}
```

Find user from database and compare password.
If not sucess -> Bad response

```json
{
    "message": "Invalid username or password"
}
```

Else

2. Create access token and send to client

```json
{
    "access_token": "123oasidnunaybsd.98jda8dxm17h12cciaushdn128.lkasd812enbcby1y27e712n2y1gey"
}
```

3. Use middleware function to check the access token
    - Client stores the access token in - Request -> Headers -> Authorization -> Bearer "access_token"
    - You need to get it (Try to solve it yourself. If you can't I'll explain)
    - Check this token with your secret key (it's used when creating access token)
    - If success, DONE. (ADDITIONAL: if you need some data from token, like user_id or etc, for
      your handler (f. e. want to find user from database with user_id), you can add the data
      to request. It works like this:
        a) First hanler (mmiddleware function) takes request and check the token
        b) First handlaer (mmiddleware function) set the new data to request.
           Request is like dictionary, you can add another property, but can used
           only once, cause every request is new.
        c) The second handler take the data from request

      In NodeJS I write like this -> req.data, in FastAPI might be the same, check it)
4. If access token is invalid, throw status code 401 (Unauthorized)

> ***I'll add other things, when you'll say done.***

![patient](https://www.memesmonkey.com/images/memesmonkey/s_2a/2a0e698c17bba4ac458a43eb6ff3dc0d.jpeg)
