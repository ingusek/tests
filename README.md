# Node.js (REST API) + Vue.js/Nuxt.js (Frontend/Backend) + MySQL Boilerplate

This is a boilerplate project. The project contains Node.js REST API and frontend/backend developed by Vue.js with
BootstrapVue.

- API
  - Node.js, Express, Webpack, Express Validator, JWT, Bunyan, Promise MySQL, Node Mailer, Jest, Supertest, Nodemon, DB
    migrate
- Frontend - Vue.js
  - Vue.js, Vuex, Vue Router, Vue Draggable, Vuelidate, BootstrapVue, Jest, Cypress
- Backend
  - Vue.js, Vuex, Vue Router, Vuelidate, BootstrapVue, Jest, Cypress

## Demo

| Service            | Endpoint                                                                                                 |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| API                | [https://nvm-boilerplate.chrislee.kr/api/](https://nvm-boilerplate.chrislee.kr/api/)                     |
| Frontend - Vue.js  | [https://nvm-boilerplate.chrislee.kr/frontend/](https://nvm-boilerplate.chrislee.kr/frontend/)   |
| Backend            | [https://nvm-boilerplate.chrislee.kr/backend/](https://nvm-boilerplate.chrislee.kr/backend/)             |
| Mailhog            | [https://nvm-boilerplate.chrislee.kr/mailhog/](https://nvm-boilerplate.chrislee.kr/mailhog/)             |

## How to start in your local environment

```bash
$ docker-compose up -d
```

Once docker containers are up, then you can access services with below URL.

| Service            | Endpoint                                                         |
| ------------------ | ---------------------------------------------------------------- |
| API                | [http://todo.local/api](http://localhost/api)                     |
| Frontend - Nuxt.js | [http://todo.local/frontend-nuxt](http://localhost/frontend-nuxt) |
| Frontend - Vue.js  | [http://todo.local/frontend](http://localhost/frontend)   |
| Backend            | [http://todo.local/backend](http://localhost/backend)             |
| Mailhog            | [http://todo.local/mailhog](http://localhost/mailhog)             |
| MySQL              | mysql.local:3307                                                   |

There are three users in the database initially. You can use them to login Frontend/Backend.

| Service  | Username | Email                   | Password |
| -------- | -------- | ----------------------- | -------- |
| Backend  | admin    | admin@boilerplate.local | 123456   |
| Backend  | staff    | staff@boilerplate.local | 123456   |
| Frontend | user     | user@boilerplate.local  | 123456   |

### API

API docker container will be launched as development mode with nodemon. However, it won't detect any changes unless
uncomment volumes.

To enable live change for the API, simply uncomment following lines in `docker-compose.yml`

```text
  volumes:
    - ./api:/srv
```

Please make sure you run `npm install` in the `api` folder.

### Frontend & Backend

Currently, Frontend (Nuxt.js/Vue.js) and Backend docker container is configured to serve production mode due to the
limitation of setting development environment of Vue.js in sub directory.

If you want to have Hot Reload feature, then you should launch the Frontend separately by `npm run serve`.

```bash
cd frontend
npm run serve

# or

cd frontend-nuxt
npm run dev

# or

cd backend
npm run serve
```

Then access Frontend - Vue.js with `http://localhost:8080` and Backend
with `http://localhost:8081` via your browser.

### Mailhog

Currently, API is configured to point Mailhog to send an email. Any email sent by the API can be viewed in Mailhog web
interface.

Access via your browser `http://todo.local/mailhog`

### MySQL

MySQL port is mapped to 3307.

## Features

- API

  - Database migration

- Frontend - Vue.js

  - User registration
  - Confirm user email address
  - Reset user password
  - User login/logout
  - Manage todo
  - Manage account information

- Frontend - Nuxt.js

  - Support all features that "Frontend - Vue.js"
  - Server Side Render (SSR)

- Backend

  - Staff login/logout
  - Staff permission management
  - List todo
  - Manage users
  - Manage staffs
  - Manage settings

- CI/CD
  - Gitlab: .gitlab-ci.yml
  - Github: .github/workflows/main.yml

## Todo

- [x] Unit tests
- [x] E2E tests


## Docker
docker-compose -f docker-compose.yml -f docker-compose.tests.yml up -d  
docker exec -it selenium bash  


## Tests
/usr/bin/chromedriver --version
/opt/google/chrome/chrome --headless --no-sandbox --disable-gpu --disable-dev-shm-usage --window-size=1920,1080 --log-level=ALL
/opt/google/chrome/chrome --no-sandbox --disable-gpu --log-level=ALL --remote-debugging-port=9222 --window-size=1920,1080

Robot:
http://localhost:8080/vnc.html

Selenium:
http://localhost:7900/


## Add user
```
curl --location --request POST 'http://localhost/api/user/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "ingusek",
    "email": "ingus@wp.pl",
    "password": "test1234",
    "first_name": "Jan",
    "last_name": "Kowalski"
}
'
```

## Robot

### Configure Chrome WebDriver
```
	${args}    ChromeConfiguration.serviceargs
	${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
	Call Method    ${chrome_options}  add_argument  --no-sandbox
	Call Method    ${chrome_options}  add_argument  --headles
	
  # Create WebDriver   Chrome  chrome_options=${options}
	# ${chrome_options}    ChromeConfiguration.config
  # ${args}    ChromeConfiguration.serviceargs
	# Start Virtual Display    1920    1080
  Create WebDriver    Chrome    chrome_options=${chrome_options}    service_args=${args}
```

Run Test:  

Robot with Page Object:  
```
cd tests/e2e/robot-page-object
robot -d results tests/Registration.robot
```

Robot: 
```
cd tests/e2e/robot
robot -d results Registration.robot
```
