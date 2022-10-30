title: Instant Access
description: Keep track of all Offen Fair Web Ananlytics instances you have visited.
date: 2022-10-30
slug: instant-access
url: /blog/complete-stable/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0240-instant-access.jpg
author: Hendrik Niefeld
bottom_cta: protocol

# Episode Thirteen — Instant Access

Once again, we would like to share some of the highlights of our recent work. Over the last five months we have build a companion browser extension to keep track of all *Offen Fair Web Ananlytics* instances you have visited, added a Vietnamese locale and updated the filtering mechanism. As usual, there are some minor bug fixes and dependency updates as well.

Since our last update we have published a few new versions:

- [v1.1.0](https://github.com/offen/offen/releases/tag/v1.1.0)
- [v1.2.0](https://github.com/offen/offen/releases/tag/v1.2.0)
- [v1.2.1](https://github.com/offen/offen/releases/tag/v1.2.1)
- [v1.3.0](https://github.com/offen/offen/releases/tag/v1.3.0)
- [v1.3.1](https://github.com/offen/offen/releases/tag/v1.3.1)
- [v1.3.2](https://github.com/offen/offen/releases/tag/v1.3.2)
- [v1.3.3](https://github.com/offen/offen/releases/tag/v1.3.3)

Download it at [https://get.offen.dev](https://get.offen.dev/) or pull it from Docker Hub.

---

### Instant Access

Users of Firefox, Chrome and Edge can now install a companion browser extension that keeps track of all Offen Fair Web Ananlytics instances they have visited. The extension detects if there is an official installation running on the currently open website and displays a link to the dedicated Auditorium.

In the Auditorium (that runs on version v1.3.0 or later), all installations you have visited so far are then accessible. If usage data has been collected, it can be easily accessed and managed. [Read the docs](https://docs.offen.dev/using-offen/browser-extension/) to learn more.

##### Firefox users can install the extension directly from the Mozilla Add-Ons Store.
[Install for Firefox](https://addons.mozilla.org/en-US/firefox/addon/offen-instant-access/){: data-button="full"}

##### *Chrome and Edge* users can download the extension directly from our server (Right click and save) and then drag the file onto the browser.
[get.offen.dev/crx](https://get.offen.dev/crx){: data-button="outline"}

---

### Supporters club

We are very pleased that [@appwrite](https://twitter.com/appwrite) is supporting us as part of their initiative to promote the Open Source community. Big thanks guys for being our first [GitHub sponsor!](https://github.com/sponsors/offen)
We really appreciate the [recognition](https://dev.to/appwrite/appwrite-loves-open-source-why-i-chose-to-sponsor-offen-5efn) and generous funding.

It helps us to continue to improve Offen Fair Web Ananlytics and make the web a better place. Are you interested in joining the supporters club too? Enroll today on [GitHub](https://github.com/sponsors/offen) or [Patreon!](https://www.patreon.com/offen)

---

### What else?

#### Xin Chào

Our consent banner and the Auditorium for operators as well as users can be displayed in one more locale. Offen is now available in English, French, German, Portuguese, Spanish and, most recently, Vietnamese. Thanks to the wonderful contribution by [@hiensarahly](https://github.com/hiensarahly).

To run Offen in a non-default locale, you need to set *OFFEN_APP_LOCALE* to the desired value. In the case of Vietnamese that'd be *vi* for example. [Check the docs](https://docs.offen.dev/running-offen/configuring-the-application/#application) about configuring the application.

If you want to support fair web analytics by contributing Italian, Dutch, Polish or other language versions, don't hesitate to [request an invite.](mailto:hioffen@posteo.de)

#### All filtered

From version v1.1.0, Offen applies filters to all metrics. For example, if the filter "Visitors with a specific referrer value" is set, only these will be then displayed in the “Weekly retention” table as well as in the “Real time” view.

#### Happy to hear from you

Are you using Offen Fair Web Analytics? We're happy to feature you in this README. Send a PR adding your site or app to this section.

As always, if you have feedback, comments or bug reports on the latest version, let us know. Open an [issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de](mailto:hioffen@posteo.de).
