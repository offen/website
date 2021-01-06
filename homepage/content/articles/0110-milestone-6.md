title: Packaging and testing
description: For Milestone 6 we have tested our app intensively and added several new installation options and tutorials for popular hosters.
date: 2020-09-14
slug: packaging-testing
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0110-milestone-6.jpg
author: Frederik Ring
bottom_cta: blog

# Episode Six — Packaging and testing

It feels a little surreal to write this, but: this post marks the end of Milestone 6, which is the last one defined in our initial product plan defining the scope of our support by the [NGI Zero PET initiative](https://nlnet.nl/thema/NGIZeroPET.html){: target="_blank"}.

In these last weeks we focused on packaging and testing, which - who would have thought - uncovered some issues we didn't know about yet. But it also felt very rewarding to see the work of the last ~9 months paying off, now that we and others can deploy and use Offen easily. Having designed Offen as a self hosted solution from the start, we managed to establish a unique characteristic when comparing Offen with other solutions out there: if you're looking to self host your analytics software, it won't get much easier. If you are unsure about that claim, check out the rest of this post to see what that actually means.

During Milestone 6 we have released the following versions:

- [v0.1.2](https://github.com/offen/offen/releases/tag/v0.1.2)
- [v0.1.3](https://github.com/offen/offen/releases/tag/v0.1.3)
- [v0.1.4](https://github.com/offen/offen/releases/tag/v0.1.4)
- [v0.1.5](https://github.com/offen/offen/releases/tag/v0.1.5)
- [v0.1.6](https://github.com/offen/offen/releases/tag/v0.1.6)

As always, you can download the latest release from [https://get.offen.dev](https://get.offen.dev) or pull it from Docker Hub.

---

## Achievements

### Offen runs almost everywhere

One of the design goals of Offen is to make it really easy to install. Nevertheless, using self hosted software can be daunting if you haven't done it before, or you are not well versed with using the CLI. To help people unsure about what to do getting started, we published a lot of options and contributed to community resources:

- There is a tutorial for installing Offen on [Uberspace](https://uberspace.de/){: target="_blank"}: [https://lab.uberspace.de/guide_offen.html](https://lab.uberspace.de/guide_offen.html){: target="_blank"}

- We packaged Offen for [YunoHost](https://yunohost.org/#/){: target="_blank"} (an operating system tailored towards self hosting): [https://github.com/offen/offen_ynh](https://github.com/offen/offen_ynh){: target="_blank"}

- We wrote a tutorial for how to host your static website alongside Offen: [https://github.com/hetzneronline/community-content/pull/257](https://github.com/hetzneronline/community-content/pull/257){: target="_blank"}

- You can deploy Offen to Heroku with a single click: [https://github.com/offen/heroku](https://github.com/offen/heroku)

- There is also a prebuilt image for DigitalOcean: [https://github.com/offen/digitalocean](https://github.com/offen/digitalocean)

- In case Docker is something you are using, here's our image: [https://hub.docker.com/r/offen/offen](https://hub.docker.com/r/offen/offen){: target="_blank"}

- Raspberry Pis can run Offen just fine: [https://docs.offen.dev/running-offen/downloads-distributions/#building-offen-for-architectures-other-than-amd64](https://docs.offen.dev/running-offen/downloads-distributions/#building-offen-for-architectures-other-than-amd64)

In case you know of another great target for installing Offen, let us know and we'll check out the option right away.

### deb package for easier setup

Installing Offen from our binary distributions hasn't been too complicated already, but starting with version 0.1.6 we now also ship Offen as a `deb` package. This means, installation on Ubuntu or Debian servers is now as easy as:

```bash
curl -sSL -o offen.deb https://get.offen.dev/deb
sudo dpkg -i offen.deb
sudo systemctl enable offen
sudo systemctl start offen
```

We also updated our [installation tutorials](https://docs.offen.dev/running-offen/tutorials/) to reflect this. Packaging code lives in the [offen/deb](https://github.com/offen/deb) repository. A nice side effect of this is that we'd be pretty much ready to set up a repository for people to install Offen using the `apt` package manager in case this is requested.

### Helping others to install and run Offen

While we've been doing a lot of test installations of Offen ourselves in the past weeks, we've also seen others starting to install of Offen. We've seen some expected teething troubles we've fixed along the way, but more importantly we've gained further insights on how people deploy and use Offen, allowing us to further optimize for the relevant use cases.

### Helping others to start contributing to Offen

Offen is free and open for everyone to use with no strigs attached. There is no business model like a hosted version or similar behind it. This is why it's important for us to open up the development of Offen to the community now that we've set the foundation. To kick this off, we will be participating in this year's [Hacktoberfest](https://hacktoberfest.digitalocean.com/){: target="_blank"}. Check out the [relevant issues on our repository](https://github.com/offen/offen/issues?q=is%3Aissue+is%3Aopen+label%3AHacktoberfest), forward this to whoever might be interested, or start hacking on Offen yourself right away. We are also happy about any kind of feedback on our [roadmap](https://github.com/offen/offen/projects/1).

---

## Next up

### Spreading the word

We've built a unique analytics software, and we sense the time is just about right for shifting paradigms when it comes to collecting and handling data. However, if noone knows about Offen, noone can use it. Now that we have a working beta, we can start marketing Offen more aggressively all across the internet. If you have ideas for a good fit in terms of audience, let us know.

### Performance improvements

Securing the data collected as much as possible has always been (and will always stay) the most important aspect when developing Offen. This makes having Offen perform well on large datasets (i.e. sites with a lot of traffic) is hard. While it's already usable in these scenarios - and it's an obvious tradeoff where we have a clear priority - there is still room for improvement.

This is why we'd like to look into ways of making Offen faster while still satisfying the strict privacy and security requirements we have. Check [this issue](https://github.com/offen/offen/issues/448) for ideas about how we plan to implement this.

### Defining the future of Offen

This post is closing Milestone 6 out of 6. This means we have successfully built and shipped a working beta version of Offen. It also means it's up to us to define what we want to do next.

The obvious path is further extending and maintaining Offen, which we will continue to do. Yet, we'd also like to work on ideas about how we can make the tech, and also the ethical principles that Offen is built upon available to the public. In the end, Offen is a lot more than just an analytics tool.

### Adding a second locale

Localizing software at an early stage is hard, so we developed Offen as English-only up until now. Luckily, we already placed all the hooks need for localizing Offen in our codebase. Now that Offen has become more stable and mature, we think it's a good time to start adding a second locale. In our case, German is the obvious choice, so we are planning to make Offen available in German as well in the next months. If you're interested in helping us localize Offen in the language of your choice, we'd be happy to hear from you [in the corresponding issue on GitHub](https://github.com/offen/offen/issues/453). Vielen Dank.

---

## Getting your hands dirty

### Packaging Offen as a snap

[Snapcraft](https://snapcraft.io/){: target="_blank"} is a relatively recent way of packaging apps for use across all Linux distributions. While it has also received its fair share of criticism, it also provides a really simple way of packaging and distributing apps like Offen.

To build a snap from Offen, first install `snapcraft`. If you're on Ubuntu or Debian, you can use `snap` to install it:

```bash
snap install snapcraft
```

Next, you can create an empty directory where we build the snap:

```bash
mdkir -p offen-snap && cd offen-snap
```

The snap is defined in a file called `snap/snapcraft.yaml` :

```bash
mkdir snap && touch snap/snapcraft.yaml
```

You can define the snap in `snap/snapcraft.yml` like this:

```yaml
name: offen
version: 0.1.5
summary: Offen
description: |
  Offen is an open alternative to common web analytics tools.
  Gain insights while your users have full access to their data.
  Lightweight, self hosted and free.
base: core18
confinement: strict
parts:
  offen:
    plugin: dump
    # this downloads the tarball from the official download URL
    source: https://get.offen.dev/v$SNAPCRAFT_PROJECT_VERSION
    source-type: tar
passthrough:
  # the layout connects the confined snap fs with the user's
  # default filesystem layout
  layout:
    /var/www/.cache: # this is the certificate cache
      bind: $SNAP/var/www/.cache
    /var/opt/offen: # this is where the database file will be stored
      bind: $SNAP/var/opt/offen
    /etc/offen/offen.env: # this is the configuration file
      bind-file: $SNAP/etc/offen/offen.env
apps:
  offen:
    command: offen-linux-amd64
```

The snap is now ready to be built:

```bash
$ snapcraft
Launching a VM.
snap "snapd" has no updates available                                           
...
Snapping |                                                                                
Snapped offen_0.1.5_amd64.snap
$
```

Now, you can install Offen on your system from the built file using the `snap` command (the dangerous flag is needed as we did not sign the package):

```bash
$ snap install --dangerous offen_0.1.5_amd64.snap
Installed offen 0.1.5
$ which offen
/snap/bin/offen
```

And that's it, your system is now ready to use Offen, but more importantly, this is another simple and discoverable way of installing it for less tech-savvy users. We'll keep our eyes open for when it's time to officially start publishing Offen as a snap.

---

## Feedback? Found a bug?

If you have any feedback, comment or bug report on this milestone release, we'd love to hear from you. [Open an issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de.](mailto:hioffen@posteo.de)
