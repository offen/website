title: Extend the view
description: Over the last eight weeks, we have further optimized our display options, added a French locale, and made our Docker image more safe.
date: 2021-04-20
slug: extend-view
url: /blog/extend-view/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0170-extend-view.jpg
author: Hendrik Niefeld
bottom_cta: cookie

# Episode Nine — Extend the view

As spring arrives in Berlin, we would like to share with you some highlights of our work over the past eight weeks.

With version v0.4.1 now officially out, the UI for Offen Fair Web Analytics is now also available in French. We've added a widescreen option for the Auditorium and made our Docker image more safe. Plus, we've done a lot of maintenance under the hood to make sure everything is up to date

Since our last update we have published three versions:

- [v0.3.1](https://github.com/offen/offen/releases/tag/v0.3.1)
- [v0.4.0](https://github.com/offen/offen/releases/tag/v0.4.0)
- [v0.4.1](https://github.com/offen/offen/releases/tag/v0.4.1)

As usual, you can download the latest release from [https://get.offen.dev](https://get.offen.dev/) or pull it from Docker Hub.

---

### Achievements

#### Go widescreen

We have further optimised our display options and brought them closer to real workflows. The Auditorium for operators now makes better use of the screen space on desktop devices. Furthermore, we have optimised the display of the bar chart in mobile view.

#### Nous parlons français

Our consent banner and the Auditorium for operators as well as users can be displayed in one more locale. Thanks to the great contribution of [@jtraulle](https://github.com/jtraulle), *Offen Fair Web Analytics is now also available in French.*

To run Offen Fair Web Analytics in a non-default locale, you need to set `OFFEN_APP_LOCALE` to the desired value. In the case of French that'd be `fr` for example. [Check the docs](https://docs.offen.dev/running-offen/configuring-the-application/#application) about configuring the application.

If you want to support fair web analytics by contributing Spanish, Portuguese or other language versions, don't hesitate to [request an invite.](mailto:hioffen@posteo.de)

#### More safe

There is a breaking change for users of our Docker image using a SQLite database.

Until now, our Docker image has run the application as `root`. This could theoretically have allowed malicious third-party code to be injected into Offen Fair Web Analytics.

*It has not happened in any Offen Fair Web Analytics version* but to prevent this from potentially happening in the future, all images published from now on run the application as a dedicated, non-priviledged `offen` user. Please [refer to our documentation](https://docs.offen.dev/running-offen/known-issues/#docker-based-deployment-stops-working-after-upgrading-to-v040-or-later) on how to update. Feel free to contact us if you need further assistance.

---

### Next up

#### Awareness once more

We want to further support operators in making users aware of how their data is handled. As a further step, we plan to make all existing consent elements customizable in their design to make insertion less painful for operators.

Following on from this, we then aim to give operators a range of options for adding pre-built elements to their website that will help attract user awareness.

#### Talks and conferences

As far as the visibility of our project in the relevant public is considered, there is still much to be done. That' s why we want to present Offen Fair Web Analytics and the idea of fair data transfer behind it to a professional audience as well.

We already have a few events in mind but welcome more recommendations for relevant talks and conferences worldwide. Do you have something in mind that we should apply for? [Let us know.](mailto:hioffen@posteo.de)

---

### Happy to hear from you

Are you using Offen Fair Web Analytics? We're happy to feature you in this [README.](https://github.com/offen/offen/blob/development/README.md) Send a PR adding your site or app to [this](https://github.com/offen/offen/blob/development/README.md#whos-using-offen) section.

If you have any feedback, comment or bug report on the latest release, let us know. Open an [issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de](mailto:hioffen@posteo.de).
