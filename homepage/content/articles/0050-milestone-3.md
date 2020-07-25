title: Displaying data
description: Our milestone 3 achievements include an improved UX, a Heroku deploy option and full Safari support.
date: 2020-04-13
slug: displaying-data
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0050-milestone-3.jpg
author: Frederik Ring

# Episode Three — Displaying data

In the middle of strange times Milestone 3 - "Displaying Data" - is done. This means we focused on how we aggregate and display the data Offen collects in a way that operators can use it to improve their services and users can understand what is being collected and what it means for their privacy.

As we are now cutting official alpha releases already, we have also changed the format of our project updates. Instead of one pull request per milestone, we now have an update that spans across multiple releases. During Milestone 3 we have released the following versions:

- [v0.1.0-alpha.2](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.2)
- [v0.1.0-alpha.3](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.3)
- [v0.1.0-alpha.4](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.4)
- [v0.1.0-alpha.5](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.5)

As always, you can download the latest release from [https://get.offen.dev](https://get.offen.dev) or pull it from Docker Hub.

---

## Achievements

### Improved and annotated Auditorium

The Auditorium is where both users and operators access and manage usage data. Operators want to gain insights in how their services are being used, users want to understand what data Offen is collecting and manage this data.

The user facing Auditorium is now annotated with explanations for each metric and also explains analytics-specific terms and answers frequently asked questions. This has been implemented in [PR 339](https://github.com/offen/offen/pull/339).

<img class="screencast mt3 mb2" alt="browser setup" src="/theme/images/offen-blog-0050-explainer.gif"/> 

In addition to that we added new metrics and improved the overall user experience for both users and operators alike. Relevant PRs are [331](https://github.com/offen/offen/pull/331), [328](https://github.com/offen/offen/pull/328), [327](https://github.com/offen/offen/pull/327), [324](https://github.com/offen/offen/pull/324), [319](https://github.com/offen/offen/pull/319), [317](https://github.com/offen/offen/pull/317), [291](https://github.com/offen/offen/pull/291)

### Account Management fundamentals

Operators that are using Offen to improve their services are likely to work in teams. This is why the application needs tools for managing user logins and accounts for segmenting usage data. In a first draft we added basic versions of these features so that the absence of such capabilities doesn't further prevent the adoption of Offen. This initiative has been started in [PR 288](https://github.com/offen/offen/pull/288) and will be refined further during Milestone 4.

### In-Browser setup

The command line can seem daunting when you don't use it regularly. This is why we added an in-browser setup screen for Offen. Instead of performing the initial setup using the `offen setup` command from the CLI, operators who prefer to do so can now use their browser to navigate to the `/setup` URL of their installation and perform the initial setup there. We hope this helps us gaining further traction with semi-technical users that want to use privacy friendly tools. This has been implemented in [PR 299](https://github.com/offen/offen/pull/299).

<img class="screencast mt3 mb2" alt="browser setup" src="/theme/images/offen-blog-0050-browserSetup.gif"/> 

### Goodbye, Choo

We started out with using Choo as our frontend framework and it was a great choice as it allowed us to build dynamic UIs very rapidly. But as Offen's Auditorium was growing over the last few months we noticed its lack of mechanisms for breaking interfaces into components was starting to slow us down significantly and made simple changes cumbersome to implement.

This is why - before starting work on the annotated Auditorium - we migrated the application to use Preact in [PR 289](https://github.com/offen/offen/pull/289). Preact is a great choice as it allows us to use modern paradigms for programming interfaces without having to buy into a Facebook-dominated ecosystem. The library is distributed under a MIT license.

### Signed binary downloads

As we start to target more and more distribution channels, ensuring the integrity of what people actually download is very important for an application like Offen. With [PR 338](https://github.com/offen/offen/pull/338) we started signing our binaries with a GPG key. Downloaders can now verify that a binary they are planning to use is the one we intend to distribute:

```bash
gpg --keyserver pgp.mit.edu --recv F20D4074068C636D58B53F46FD60FBEDC90B8DA1
gpg --verify offen-linux-amd64.asc offen-linux-amd64
```

### Safari Support

Offen generates client side keys for encrypting data for each user. At the end of Milestone 2 we noticed issues where the Safari browser would not store these keys properly which means users would lose access to their user data. We fixed this in [PR 282](https://github.com/offen/offen/pull/282) by adding a fallback mechanism that Safari can use. Keys are guaranteed to be safe from third party access in both implementations.

### 1-Click Deploy

Self hosted software is a great fit for privacy focused software like Offen. Yet, it can seem daunting to non-technical users and make them stick to established SaaS solutions longer than needed. This is why we put a lot of effort into finding easy "1-click" options to deploy an Offen instance. In Milestone 3 we have created a 1-click solution for deploying Offen to Heroku: [https://github.com/offen/heroku](https://github.com/offen/heroku). Using free resources only, people interested in running Offen can now deploy a production ready instance to Heroku in less than 1 minute. We hope this encourages website operator to consider self-hosted software and Offen as a real option. Required changes for this were implemented in [PR 287](https://github.com/offen/offen/pull/287).

<img class="screencast mt3 mb2" alt="browser setup" src="/theme/images/offen-blog-0050_oneClickDeploy.gif"/> 

To offer even more options we are also looking into building a 1-click option for other platforms like YunoHost and DigitalOcean very soon.

---

## Next up

Milestone 4 is up next and is called "Managing Data". This means we will focus on features that allow operators and users to manage their usage data and Offen instances.

This is also *where we will have a slight deviation from the original product plan*: We originally had an item called "Selective Data deletion for users", yet as we have moved to focus on self-hosting more and more, this feature does not make too much sense anymore. Instead we will allow users to delete their data tied to an instance entirely and *will make it easy to follow how deletion works and what the implications are*.

### Account management

In addition to the basic account management features Offen already offers, we'll work on implementing more fine grained access control mechanisms so that teams that are using Offen can easily and safely share access to an instance. In addition to that we will also revisit existing features and try to make them easier to use and more accessible.

### Collecting and implementing real world user feedback

We are still labeling Offen as `alpha` right now, but we think the next weeks could be the right time to slough that potentially scary label off and attract more users by going `beta`.

Before we do so though, we would like to collect feedback from people that are brave enough to deploy the existing alpha version and use it for a while. Luckily there are some, so that's a good start, but in case you do know of people who might be interested in deploying and testing Offen, we'd be happy if you could spread the word. Documentation for running Offen is readily available at [https://docs.offen.dev/running-offen/](https://docs.offen.dev/running-offen/)

---

## Getting your hands dirty

### Installing Offen as a systemd service

We're eager to get people to install Offen and send us their feedback and tell us about their experience, so instead of adding features to the software itself, we will today look at how Offen can be installed on a Linux system that supports `systemd`.

### Download the binary

First, download and unpack the tarball containing latest release and verify its signature:

```bash
mkdir -p /tmp/offen-download && cd /tmp/offen-download
curl -sSL https://get.offen.dev/v0.1.0-alpha.5 | tar -xvz
gpg --keyserver pgp.mit.edu --recv F20D4074068C636D58B53F46FD60FBEDC90B8DA1
gpg --verify offen-linux-amd64.asc offen-linux-amd64
```

### Install the binary

Next, let's move the downloaded version to `/opt` and create a symlink in `/usr/bin` so the command is available in the system's `PATH`:

```bash
sudo mkdir -p /opt/offen/v0.1.0-alpha.5
sudo cp offen-linux-amd64 /opt/offen/v0.1.0-alpha.5
sudo ln -s /opt/offen/v0.1.0-alpha.5/offen-linux-amd64 /usr/bin/offen
```

You can verify that this worked as intended like this:

```bash
$ which offen
/usr/bin/offen
$ offen version
INFO[0000] Current build created using                   revision=v0.1.0-alpha.5
```

### Scaffold the required directories

Offen follows the Linux Filesystem Hierarchy Standard, so next, we need to create the directories for storing data, configuration and certificates:

```bash
sudo mkdir -p /etc/offen && sudo touch /etc/offen/offen.env
sudo mkdir -p /var/opt/offen
sudo mkdir -p /var/www/.cache
```

### Creating the service

The Offen server needs to be run in a supervised manner so we can be sure it is always responding. `systemd` can do this for us. First we create the service definition:

```bash
sudo touch /etc/systemd/system/offen.service
```

and populate this file with the following content:

```
[Unit]
Description=Offen Service

[Service]
ExecStart=/usr/bin/offen
Restart=always

[Install]
WantedBy=multi-user.target
```

Now we can register the service with `systemd` itself:

```bash
sudo systemctl daemon-reload
sudo systemctl enable offen
sudo systemctl start offen
```

You can check whether this worked correctly using `status:`

```
$ sudo systemctl status offen
● offen.service - Offen Service
   Loaded: loaded (/etc/systemd/system/offen.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2020-01-27 15:57:58 CET; 1min ago
 Main PID: 6701 (offen)
    Tasks: 11 (limit: 4915)
   CGroup: /system.slice/offen.service
           └─6701 /usr/bin/offen
```

### Running the in-browser setup

To create the initial account for your Offen install, head to `[localhost:3000/setup](http://localhost:3000/setup)` and fill out the form. After doing so, your Offen instance is ready for local use! If you want to expose this instance to the public internet, [refer to our docs site](https://docs.offen.dev/running-offen/tutorials/configuring-deploying-offen-ubuntu/) for instructions on how to get free automated SSL up and running.

---

## Feedback? Found a bug?

If you have any feedback, comment or bug report on this milestone release, we'd love to hear from you. [Open an issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de.](mailto:hioffen@posteo.de)
