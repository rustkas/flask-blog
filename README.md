`pip install python-dotenv`

`flask run`

## GitHub notes
```
git pull origin main --rebase
git push -u origin main
```

## Remove folder from GitHub
```
# Удаляем из индекса (напрямую указываем путь к папке)
git rm -r --cached .
git add .
git commit -m "Удалена папка __pycache__ из отслеживания"
git push
```

## Working with forms
`pip install flask-wtf`
`pip install email-validator`
python
import secrets
secrets.token_hex(16)

## DB
`pip install flask-sqlalchemy`

```
python
from flaskblog import app, db
with app.app_context():
   db.create_all()

from flaskblog import app, db, User

# Весь код работы с БД должен быть здесь
with app.app_context():
    user_1 = User(username='Corey', email='C@demo.com', password='password')
    db.session.add(user_1)
    db.session.commit()
    print("Пользователь добавлен!")

... # Весь код работы с БД должен быть здесь
... with app.app_context():
...     user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
...     db.session.add(user_2)
...     db.session.commit()
...     print("Пользователь добавлен!")
...     
Пользователь добавлен!
>>> with app.app_context():
...     User.query.all()
...     
[User('Corey', 'C@demo.com', 'default.jpg'), User('JohnDoe', 'jd@demo.com', 'default.jpg')]
>>> with app.app_context():
...     User.query.first()
...     
User('Corey', 'C@demo.com', 'default.jpg')
>>> with app.app_context():
...     User.query.filter_by(username='Corey').all()
...     
[User('Corey', 'C@demo.com', 'default.jpg')]
with app.app_context():
    user = User.query.first()
    print(user.posts)  # Здесь всё работает, так как сессия активна

>>> with app.app_context():
...     user = User.query.first()
...     post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
...     post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
...     db.session.add(post_1)
...     db.session.add(post_2)
...     db.session.commit()
...     user.posts
...     
[Post('Blog 1', '2026-06-13 12:41:31.773040'), Post('Blog 2', '2026-06-13 12:41:31.773040')]

>>> with app.app_context():
...     user = User.query.first()
...     for post in user.posts:
...         print(post.title)
>>> with app.app_context():
...     post = Post.query.first()
...     
>>> post
Post('Blog 1', '2026-06-13 12:41:31.773040')
>>> with app.app_context():
...     post = Post.query.first()
...     post.user_id
>>> with app.app_context():
...     post = Post.query.first()
...     post.author
...     
User('Corey', 'C@demo.com', 'default.jpg')

>>> with app.app_context():
...     db.drop_all()
...     
>>> 
>>> with app.app_context():
...    db.create_all()
...    
>>> with app.app_context():
...    User.query.all()
...    
[]
```