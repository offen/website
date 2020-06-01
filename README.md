<a href="https://offen.dev/">
    <img src="https://offen.github.io/press-kit/offen-material/gfx-GitHub-Offen-logo.svg" alt="Offen logo" title="Offen" width="150px"/>
</a>

# Website
[![CircleCI](https://circleci.com/gh/offen/website/tree/master.svg?style=svg)](https://circleci.com/gh/offen/website/tree/master)

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

The content of this website itself is licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0) License][cc-by-4], and the underlying source code used to format and display that content is licensed under the [GNU Affero General Public License v3.0][license].

[cc-by-4]: https://creativecommons.org/licenses/by/4.0/
[license]: https://github.com/offen/website/blob/development/LICENSE
