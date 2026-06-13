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