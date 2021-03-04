title: Improving interfaces
description: Our key achievements in the last six weeks are a German locale and customizable time intervals for the Auditorium.
date: 2021-02-07
slug: interfaces
url: /blog/interfaces/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0150-interfaces.jpg
author: Hendrik Niefeld
bottom_cta: blog

# Episode Eight — Improving interfaces

Like last year, we want to keep you updated on the current status of our project at regular intervals. So these are the highlights of our work over the last six weeks. With version v0.3.0 now officially out, we've added some great additions to our interfaces.

First of all the UI for Offen is now also available in German. This gives all users in the DACH region the chance to use our fair web analytics tool also for their localised web projects.

We also overhauled the date range selection interface adding custom time ranges. Furthermore, we added an experimental JS API and cleaned up the codebase, making things faster and more lightweight for you to use.

Since our last update we have published two versions:

- [v0.2.3](https://github.com/offen/offen/releases/tag/v0.2.3)
- [v0.3.0](https://github.com/offen/offen/releases/tag/v0.3.0)

As usual, you can download the latest release from [https://get.offen.dev](https://get.offen.dev/) or pull it from Docker Hub.

---

## Achievements

### Localize it

Offen is now also available in English and German. Our consent banner and the Auditorium for operators as well as users can be displayed in the respective locale.

To run Offen in a non-default locale, you need to set `OFFEN_APP_LOCALE` to the desired value. In the case of German that'd be `de` for example. [Check the docs about configuring the application](https://docs.offen.dev/running-offen/configuring-the-application/#application).

Our translation workflow featuring [POEditor](https://poeditor.com){: target="_blank"} is up and running and ready to be applied to other languages. A further locale, Indonesian, is currently in the works. If you want to support fair web analytics by contributing French, Spanish or other language versions, don't hesitate to [request an invite.](mailto:hioffen@posteo.de)

### About time

In order to evolve Offen into a fully competitive analytics tool, we still have some significant UX improvements in mind. Over the last few weeks, we have implemented one of them.

Now you can easily display custom intervals of the existing data. Furthermore, we have revised the selection of standard time periods. As always, we are happy to hear feedback on its usability from you.

### Experimental JS API

For all of you who would like to have a little more precision in the way user consent is exercised, we have good news.

Offen automatically acquires a user consent decision and collect pageviews in case consent is given. For more fine-grained contro you can now use the JavaScript API exposed by the Offen `script` instead and trigger a pageview event yourself. [Learn more about this in our docs.](https://docs.offen.dev/running-offen/embedding-the-script/#triggering-pageviews-using-the-javascript-api)

---

## Next up

### Cohorts

In the UX realm, we will next be dealing with cohorts. We plan to add a flexible drill-down workflow to the Auditorium that will provide better insight into the performance of data subsets. This will allow operators to compare user subgroups with each other, e.g. how page depth behaves depending on the refferer.

### Views

We will also further optimize the general display options and bring them closer to real-world workflows. We aim to display more functions above the fold on desktop devices and to optimise for clarity on mobile devices.

### Reach out

We have already made progress in terms of the visibility of our project in the relevant public sphere. Nevertheless, there is still a lot to be done. As we did at the beginning of last year, we will again directly address stakeholders in the privacy field and try to draw their attention to our fair approach to web analytics.

You got someone in mind we should urgently talk to? [Let us know.](mailto:hioffen@posteo.de)

---

## Already using Offen?

We're happy to feature your project in our GitHub [README.](https://github.com/offen/offen/blob/development/README.md) Send a PR adding your site or app to [this](https://github.com/offen/offen/blob/development/README.md#whos-using-offen) section.

If you have any feedback, comment or bug report on the latest release, we'd love to hear from you. Open an [issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de](mailto:hioffen@posteo.de).
