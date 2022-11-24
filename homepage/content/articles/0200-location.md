title: Visitor location
description: Recently we have added privacy friendly location stats and further options to improve user awareness.
date: 2021-11-02
slug: visitor-location
url: /blog/sytles-filters/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0200-visitor-location.jpg
author: Hendrik Niefeld
bottom_cta: disclose

# Episode Eleven — Visitor location

After a fairly long break, today we like to share with you some of the highlights of our recent work. In the last 3 months, we have been working hard to add visitor location statistics that meet our privacy standards. In addition, we have included widgets that can help to increase the user awareness.

As usual, we also provided some minor bug fixes and dependency updates. Since our last update we have published three new versions:

- [v0.4.4](https://github.com/offen/offen/releases/tag/v0.4.4)
- [v0.5.0](https://github.com/offen/offen/releases/tag/v0.5.0)
- [v0.5.1](https://github.com/offen/offen/releases/tag/v0.5.1)

You can download the latest release from [https://get.offen.dev](https://get.offen.dev/) or pull it from Docker Hub.

---

### Achievements

#### Locations stats from time zones

A user's geographic location is one of the most important metrics for operators. Where are they actually successful and where do the services not work as intended?

This feature has been on our to-do list for a long time, but implementing it in a way that meets our privacy standards proved to be a challenge. After intensive research and [careful consideration](https://github.com/offen/offen/issues/423), we have finally opted for a time zone-based approach in this matter.

This method does not rely on an IP database to derive the geographical location, but asks the browser for the selected time zone and tries to match it to a country. Therefore, the only resolution available is at country level. Countries that span multiple time zones are merged before the data is stored. This fully protects the privacy of users and provides sufficiently accurate results for analysis as well.

#### Spread the word

Giving users the option to manage their usage data is only meaningful if users know about it and can access it without any problems.

As the only direct link to the User Auditorium is in the consent banner, it was important for us to provide further offers to improve user awareness. Widgets now give operators the possibility to easily integrate a link to the User Auditorium into their services.

In this way, we would like to invite all operators who use Offen Fair Web Analytics to give their users uncomplicated access to their data. At best with a link to the User Auditorium on every page.

#### Under the hood

Please note that we have stopped supporting `root` Docker images. If you are upgrading from an ancient version (v0.3.1 or earlier) or you have been using the -root Docker image, you will need to perform some changes to file permissions as [described in our documentation.](https://docs.offen.dev/running-offen/known-issues/#docker-based-deployment-stops-working-after-upgrading-to-v040-or-later)

All other installations can be updated without any extra steps. Read more about minor updates in the [respective releases.](https://github.com/offen/offen/releases)

---

### Next up

#### Getting close

There are still a few more small improvements on the agenda, but with the implementation of location stats we are a decisive step closer to v1.0. So stay tuned and follow us here or on [Mastodon](https://fosstodon.org/@offen) for the next release updates.

#### More dialogue

Over the past months, we have had the opportunity to share our vision and give some insights into the work on our projects. Thanks again to the teams from [FrOSCon](https://programm.froscon.de/2021/events/2659.html) and [PrivacyWeek](https://fahrplan.privacyweek.at/pw21/talk/L7VGKD/) for supporting us.

As we are always open to present Offen Fair Web Analytics and the idea of fair data transfer to an interested audience, we are actively looking for suitable events around the world. Got something in mind that we should apply for? [Get in touch.](mailto:hioffen@posteo.de)

#### ¿Ayuda, por favor?

Open is currently available in English, French and German. Our translation workflow featuring [POEditor](https://poeditor.com) is up and running and ready to be applied to other languages. A further locale, Greek, is currently in the works. If you want to support fair web analytics by contributing Spanish, Portuguese or other language versions, don't hesitate to [request an invite.](mailto:hioffen@posteo.de)

---

### Always happy to hear from you

Are you using Offen Fair Web Analytics? We're happy to feature you in this [README.](https://github.com/offen/offen/blob/development/README.md) Send a PR adding your site or app to [this](https://github.com/offen/offen/blob/development/README.md#whos-using-offen) section.

If you have any feedback, comment or bug report on the latest release, let us know. Open an [issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de](mailto:hioffen@posteo.de).
