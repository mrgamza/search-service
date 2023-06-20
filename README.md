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
NAVER_CLIENT_ID={YOU}
NAVER_CLIENT_SECRET={YOU}
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
### Search
URL
```
GET {domain}/search?query={query_string}
```
Response
```
{
    "resultCode": string,
    "resultMessage": string,
    "items": [
        {
            "title": string,
            "link": string,
            "description": string,
            "bloggername": string,
            "bloggerlink": string,
            "postdate": string
        }
        ...
    ]
}
```
---
## Author
- Donghyuk Lee, mrgamza@gmail.com
---
## License
- MIT license.
