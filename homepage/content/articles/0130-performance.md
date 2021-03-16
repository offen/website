title: Performance and Awareness
description: In the last three months, we have significantly improved query performance, added onboarding to our Auditorium, and updated our Docs.
date: 2020-12-17
slug: performance-awareness
url: /blog/performance-awareness/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0130-performance-awareness.jpg
author: Hendrik Niefeld
bottom_cta: blog

# Episode Seven — Performance and Awareness

Some time has passed after [NGI Zero PET Initiative](https://nlnet.nl/thema/NGIZeroPET.html){: target="_blank"} funding ended, we want to recap the results of our work with this blog post.

Wrapping up what has been a challenging year for everyone, we have been working steadily over the past three months to further enhance our product. The most important aspect of this was a significant improvement in query performance. An update that is particularly beneficial for operators of high-traffic websites who want to analyse user behavior over long periods of time.

Furthermore, we have started to work on increasing the awareness of users for the access to their data in the Auditorium. We have identified this challenge as one of the most important for us and it will continue to engage us in the coming months, well into 2021.

During the last three months we have released the following versions:

- [v0.1.7](https://github.com/offen/offen/releases/tag/v0.1.7)
- [v0.1.8](https://github.com/offen/offen/releases/tag/v0.1.8)
- [v0.2.0](https://github.com/offen/offen/releases/tag/v0.2.0)
- [v0.2.1](https://github.com/offen/offen/releases/tag/v0.2.1)
- [v0.2.2](https://github.com/offen/offen/releases/tag/v0.2.2)

As usual, you can download the latest release from [https://get.offen.dev](https://get.offen.dev/) or pull it from Docker Hub.

---

### Achievements

#### Faster queries

By adding an aggregate cache, we were able to significantly improve query performance in the Auditorium. This is quite noticeable when analyzing many data points over extended time frames. On desktop computers with current browsers, we were able to cut query times by up to two-thirds.

#### A better Auditorium

Before we will tackle some major UX updates that will primarily benefit the operators, we first took a closer look at the user side. Users' access to their data is one of our key features. However, the feedback we have collected so far has shown us that the context and functionality presented in the Auditorium is not instantly clear to some users. To address this, there now is an onboarding feature for the first-time user when visiting the Auditorium. Here, in addition to a short insight into the data just collected, the basic functionality of Offen is pointed out once again. Moreover, as little extras, there is now an empty state illustration on the user side and a loading state animation for all to enjoy.

#### Tagging campaigns and sources

As we want to give website operators a fair and professional web analytics alternative, we integrated a UTM feature at an early stage. This feature allows you to add special tags to your URLs, which will be displayed separately in the Auditorium. Now, you can find details about the functionality and tips on how to use it [in our Docs.](https://docs.offen.dev/running-offen/campaigns-sources/)

#### Migrate an instance to different hardware

For operators who want to migrate an older running Offen instance to another hardware, there is now an important bugfix to pay attention to. If you find yourself affected by issues, check our [detailed workarround.](https://docs.offen.dev/running-offen/known-issues/)

---

### Next up

#### Localization

As already mentioned in our last milestone, localization ranks at the top of our bucket list. Thanks to the kind support of the folks at [POEditor](https://poeditor.com/){: target="_blank"}, we now have a proper workflow in place and the translation may begin. Not surprisingly, German will be the second locale we tackle. Let us know if you can you help us out with French, Spanish or any other mother tongue.

#### Easily accessible analytics data

For Offen to be a fully competitive analytics tool, some significant UX improvements are missing. To make the analytics data more accessible, we will add two elements for operators and users: A sophisticated selection of date ranges, which is easy to use even on mobile devices, and a flexible drill-down workflow, which provides a better insight into cohorts.

#### Once again, awareness

We want to give operators a range of possibilities to insert ready-made elements on their website that make users aware of how to access their data. These and all existing consent elements will be made customizable in their design to make it less painful for operators to insert them.

#### Expanding the idea underlying Offen

Over the last year we have developed a fair, open and lightweigt web analytics tool that treats operators and users as equal parties. We like to describe the basic idea behind Offen with the concept of fair data transfer.

Taking this concept seriously, it cannot be limited to a single software project. That's why we decided to create the prerequisites to make it easier for others to get involved and use similar fair approaches. More on this in one of our following blog posts. Stay tuned.

---

### Happy to hear from you

Are you using Offen? We're happy to feature you in this [README.](https://github.com/offen/offen/blob/development/README.md) Send a PR adding your site or app to [this](https://github.com/offen/offen/blob/development/README.md#whos-using-offen) section.

If you have any feedback, comment or bug report on the latest release, let us know. Open an [issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de](mailto:hioffen@posteo.de).
