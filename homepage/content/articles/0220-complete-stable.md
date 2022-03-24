title: Complete and stable
description: Yay! Offen and its configuration APIs are now available in version v1.0.0.
date: 2022-03-24
slug: complete-stable
url: /blog/complete-stable/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0220-complete-stable.jpg
author: Hendrik Niefeld
bottom_cta: protocol

# Episode Twelve — Complete and stable

It is a particular delight to share some of the highlights of our recent work with you this time. Over the last 4 months we made it possible to to run Offen on ARM based hardware and added a Spanish and Portuguese locale. As always, we have also made some minor bug fixes and dependency updates.

Since our last update we have published a few new versions:

- [v0.6.0](https://github.com/offen/offen/releases/tag/v0.6.0)
- [v0.7.0](https://github.com/offen/offen/releases/tag/v0.7.0)
- [v1.0.0](https://github.com/offen/offen/releases/tag/v1.0.0)
- [v1.0.1](https://github.com/offen/offen/releases/tag/v1.0.1)

Yes, you have read correctly. Finally, the time has come: After intensive work, Offen is now available in the first, from our perspective, complete and fully functional version. Download it at [https://get.offen.dev](https://get.offen.dev/) or pull it from Docker Hub.

---

### Achievements

#### v1.0.0

More than two years ago, we had reflected [on this matter.](/blog/untold-roads-versioning-early-stage-software/) Now this stage has finally come for this project as well. [Offen v1.0.0 is here.](https://github.com/offen/offen/releases/tag/v1.0.0)

Altough this does not bring major changes, we have decided to keep Offen and its configuration APIs stable for now. That means you will always be able to upgrade a v1 instance to a later v1 version without any further steps required.

On this occasion thanks again to all who have contributed to the code base:
[@strootje](https://github.com/strootje) [@rocketnova](https://github.com/rocketnova) [@jtraulle](https://github.com/jtraulle) [@0xflotus](https://github.com/0xflotus) [@raLaaaa](https://github.com/raLaaaa) [@kocvrek](https://github.com/kocvrek) [@MarcoPNS](https://github.com/MarcoPNS)

#### Hola mundo, Olá Mundo

Our consent banner and the Auditorium for operators as well as users can be displayed in two more locales. Offen is now available in English, German, French and recently also in Spanish and Portuguese.

To run Offen in a non-default locale, you need to set *OFFEN_APP_LOCALE* to the desired value. In the case of Portuguese that'd be *pt* for example. [Check the docs](https://docs.offen.dev/running-offen/configuring-the-application/#application) about configuring the application.

If you want to support fair web analytics by contributing other language versions, don't hesitate to [request an invite.](mailto:hioffen@posteo.de)

#### Raspberry Pi

We added the option to run Offen on ARM based hardware such as Raspberry Pis using the official binary distributions and Docker images. Many thanks for the contribution[@strootje.](https://github.com/strootje)

---

### What now?

Maybe now would be a good time to look back on the past 2 years. However, since we are already working on projects that take the idea behind Offen even further, writing a project summary is postponed for the time being. In the meantime, we suggest taking a look at this [interim retrospective](/blog/our-story-so-far/) and our [analytics.txt](https://www.analyticstxt.org/) project.

Obviously, the development of Offen is not finished with ther current v1.0.0 version. We will continue to maintain the project and adapt it to new requirements. *For this we definitely need your continued support.* Keep testing and installing Offen latest releases and share your experience with us.

General feedback, comments or bug reports are always welcome. [Open an issue](https://github.com/offen/offen/issues), drop us a [tweet](https://twitter.com/hioffen), or send an [email](mailto:hioffen@posteo.de). Feel invited to work together to drive the idea of fair data transfer forward.
