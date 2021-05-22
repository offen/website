title: Disclose what you collect
description: Why we drafted a standard that allows you to disclose information about your use of analytics software and user tracking.
date: 2021-05-24
slug: analytics-txt
url: /blog/analytics-txt/
sitemap_priority: 0.7
image_url: /theme/images/offen-blog-0180-analyticstxt.jpg
author: Hendrik Niefeld
bottom_cta: cookie

# Disclose what you collect

The variety of data protection regulations and the range of methods used to collect usage data make web analytics a confusing field. A well-defined way for websites to indicate their use of analytics and tracking software is still missing. Earlier this year we started working on such a standard and gave it the name `analytics.txt` .

### Learning from building Offen

We recently drafted a standards proposal that allows websites and services to disclose information about their use of analytics software and user tracking. As this is related to our work on [Offen](https://www.offen.dev/), we wanted to provide some insight here into our motives, implementation and state of affairs on this matter.

Offen is a fair web analytics software that treats operators and users as equal parties. Operators can self-host Offen and gain insights about how users interact with their services while ensuring that users remain in full control over their data.

In the course of the development of our software, we came across a fundamental problem concerning the handling of user data on the internet today. The range of data protection regulations across the globe and the resulting variety of techniques for collecting usage data make web analytics a confusing field to navigate.

> *The range of data protection regulations across the globe and the resulting variety of techniques for collecting usage data make web analytics a confusing field to navigate.*

---

### What today's web lacks

Sure, terms like "data protection", "privacy-focused" or "privacy-friendly" are widespread and appear reliably in consent banners and privacy statements of of websites and services. But what do they actually [stand for?](https://www.offen.dev/blog/privacy-friendly-and-fair-web/)

In many cases, users still don't know what data is being collected and how it is being used. This leaves them confused about their situation and does not help to reduce the underlying mistrust towards operators and the web in general.

We believe that privacy has become an important aspect for users and its importance will continue to grow in the coming years. However, a clearly defined way for websites and services to signal their use of analytics and tracking software to users and make it discoverable for their tooling is still lacking.

A new specification is needed that can fill this gap for both operators and users. This standard should be nothing less than a comprehensive description of the usage of analytics and tracking in an unbiased way that is both understandable for a non-technical audience, but also useful for consumption by tools and software.

In January 2021 we started working on such a standard and gave it the name `analytics.txt` .

> *A clearly defined way for websites and services to signal their use of analytics and tracking software to users and make it discoverable for their tooling is still lacking.*


### Why a web standard?

Regulations regarding the handling of user data on websites will continue to evolve swiftly. The resulting ongoing adaptation of practices is a challenge for developers that should not be underestimated. Here, standardised information can give auditors immediate insight into the approaches followed and their compliance with applicable regulations.

However, more important than all legal aspects is the situation of the user. Those who value services that are transparent about the privacy implications will be able to easily inform themselves without having to go through huge amounts of legal text that have become common in the industry.

Not least, tools such as crawlers or browser extensions can use the information provided to signal all relevant privacy metrics to users and other third parties. A feature from which especially operators with ethical business models will benefit in the future.

> *Those who value services that are transparent about the privacy implications will be able to easily inform themselves without having to go through huge amounts of legal text.*

---

### First version submitted

For a standard to be effective, it needs a forum in which it can be discussed. We have chosen the format of the [IETF](https://www.ietf.org/standards/ids/) Internet Draft for this purpose and submitted a first version there. Thereby we want to provide a draft version for the interested public. It can be used for informal review and comment on our approaches and does not yet constitute an adopted standard.

[View Internet-Draft](https://datatracker.ietf.org/doc/draft-ring-analyticstxt/){: data-button="outline"}

### How it works

On your website, all that is needed is a simple text file stored in an defined location on the server. This text file contains formatted information on the type of data collected, techniques used, consent settings and duration of storage. Furthermore, information can be provided on compliance with legal requirements, use of software packages and additional features. All this information is ideally supported by comments that also enable the non-expert to gain better understanding.

> *On your website, all that is needed is a simple text file stored in an defined location on the server.*

This actual website is already provided with such a text file. As we obviously use Offen, our own fair web analytics tool, information on it is included in the data. This is what it looks like:

```
# analytics.txt file for www.offen.dev
Author: Frederik Ring <hioffen@posteo.de>

Collects: url, referrer, device-type
Stores: first-party-cookies, local-storage
# Usage data is encrypted end-to-end
Uses: javascript
# Users can also delete their usage data only without opting out
Allows: opt-in, opt-out
# Data is retained for 6 months
Retains: P6M

# Optional fields
Honors: none
Tracks: sessions, users
Varies: none
Shares: per-user
Implements: gdpr
Deploys: offen
```

The original file can be found [here](https://www.offen.dev/.well-known/analytics.txt) and will most likely undergo some changes in the coming months.

---

### Looking forward to hear from you

As already mentioned, `analytics.txt` is available as a draft for now and is awaiting to be discussed. Therefore, we are actively looking for reviewers and welcome any feedback.

Are there comments on the type and range of fields? Do you have an idea for an application that could consume the provided data? Are you as enthusiastic about fair data transfer as we are?

Don't hesitate to [reach out to us](mailto:hioffen@posteo.de) and feel invited to take this idea forward together. More information about the standard and its implementation can be found on the dedicated website.

[View analyticstxt.org](https://www.analyticstxt.org/){: data-button-mb5="full"}
