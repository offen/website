[![CircleCI](https://circleci.com/gh/offen/website/tree/master.svg?style=svg)](https://circleci.com/gh/offen/website/tree/master)

# website

## The www.offen.dev website

This repository contains the source code for the <https://www.offen.dev> website.

---

### Developing the application

The development setup requires `docker` and `docker-compose` to be installed.

After cloning the repository, you can build the containers and install dependencies using:

```sh
$ make setup
```

You can test your setup by starting the application:

```sh
$ make up
```

which should enable you to access the homepage at <http://localhost:8000/>.

### License

MIT © [offen](https://www.offen.dev)
