# search-service
Simple search service use Naver api.

## Install
### pip install -r requirements.txt
---
## Environment
### add .env file
```
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=1
```
---
## Start server
### Flask
```
flask run
```
### Gunicorn
```
gunicorn --bind 0:5000 "app:create_app()"
```
--
## Endpoints
### Root
URL
```
GET {domain}/
```
---
## Author
- Donghyuk Lee, mrgamza@gmail.com
---
## License
- MIT license.
