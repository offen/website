# website
[![CircleCI](https://circleci.com/gh/offen/website/tree/master.svg?style=svg)](https://circleci.com/gh/offen/website/tree/master)

> The www.offen.dev website

This repository contains the source code for the <https://www.offen.dev> website, as well as the code needed for running and extending an instance of `offen/offen` on the same domain.

---

### Developing the application

The development setup requires `docker` and `docker-compose` to be installed.

After cloning the repository, you can build the containers and install dependencies using:

```sh
$ make setup
```

Next seed the database for the `server` application:

```sh
$ make bootstrap
```

You can test your setup by starting the application:

```sh
$ make up
```

which should enable you to access the homepage at <http://localhost:8000/> and use the wrapped `auditorium` at <http://localhost:8000/auditorium>

### License

MIT © [offen](https://www.offen.dev)
