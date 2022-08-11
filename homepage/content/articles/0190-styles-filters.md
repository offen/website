title: Styles and Filters
description: Making the consent banner customisable and the ability to filter collected data are our main achievements over the last ten weeks.
date: 2021-07-28
slug: styles-filters
url: /blog/sytles-filters/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0190-styles-filters.jpg
author: Hendrik Niefeld
bottom_cta: disclose

# Episode Ten — Styles and Filters

Once again, we would like to share some of the highlights of our recent work. Over the last 10 weeks we have worked on improving the customisability of the consent banner and added a option to filter the collected data by cohort. As usual, we also provided some minor bug fixes and dependency updates.

Since our last update we have published two new versions:

- [v0.4.2](https://github.com/offen/offen/releases/tag/v0.4.2)
- [v0.4.3](https://github.com/offen/offen/releases/tag/v0.4.3)

You can download the latest release from [https://get.offen.dev](https://get.offen.dev/) or pull it from Docker Hub.

---

### Achievements

#### Customise your banner

An essential point in feedback was the wish for better customisability of the Offen Fair Web Analytics consent elements. Since the topic of conscious user decision is particularly important to us, we do not offer the option of integrating external consent banners. This is to avoid getting approval through dark patterns of any kind.

To make it easier for operators to integrate Offen Fair Web Analytics into their web offer, the banners can now be freely adapted via CSS. This is limited by some specifications to ensure the readability and functionality of the banner.

So unleash your inner artist and start customising your consent banner to match your website's design. Docs are found here: [https://docs.offen.dev/running-offen/customizing-consent-banner/](https://docs.offen.dev/running-offen/customizing-consent-banner/)

#### Filter collected data

One of the most important building blocks on the way to a v1.0 version has finally been implemented. Offen Fair Web Analytics v0.4.3 allows you to filter the collected usage data based on URL, Referrer, UTM parameters and Landings as well as Exits.

Furthermore, we have added the label "None" as a fallback for referrer values that are not provided. In this way, it is now also possible to filter for this cohort. Filters can be set and removed by clicking on the corresponding element.

Please test this feature extensively and let us know if there is anything we can improve.

#### Cleaning up

We have removed the database settings field as it has proved to be redundant and updated error messages when sharing accounts. There also have been a few fixes for Safari users concerning privacy and storage methods. Read more about this in the [respective releases.](https://github.com/offen/offen/releases)

---

### Next up

#### User awareness

To further contribute to user awareness, in a next step we want to give operators a choice of options to insert ready-made elements on their website that draw attention to the access to the collected data. We will also make these elements customisable in their design to make insertion more convenient for operators.

#### Dialogue

We are always open to opportunities to present Offen Fair Web Analytics and the idea of fair data transfer to an interested audience. In order to engage in dialogue with operators, users and activists, we are actively looking for suitable events around the world. Got something in mind that we should apply for? [Get in touch.](mailto:hioffen@posteo.de)

---

### Please let us know

If you have any feedback, comments or bug reports about our releases, we would love to hear from you. Open an [issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de](mailto:hioffen@posteo.de).
