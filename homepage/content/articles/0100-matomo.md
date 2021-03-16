title: Why Offen is a valid Matomo alternative
description: This brief comparison of both tools gives you a first insight into the field of fair and lightweight web analytics.
date: 2020-08-28
slug: matomo-alternative
url: /blog/matomo-alternative/
sitemap_priority: 0.7
image_url: /theme/images/offen-blog-0100-Matomo.jpg
author: Hendrik Niefeld
bottom_cta: fair

## Why Offen is a valid Matomo alternative

#### Matomo at a glance

Matomo was started around 2007 as a successor to phpMyVisites and *open-source alternative to Google Analytics.* The project founded by Matthieu Aubry used to be called Piwik until it was rebranded to its current name in 2018. According to Wikipedia it is installed on about 1.5 million websites, making it one of the best known open source web analytics applications on the market.

Operators interested in open and privacy friendly web analytics particularly appreciate Matomo's ability to be self hosted. The respective app variant called "Matomo On-Premise" has no license costs, but paid plugins are necessary for extensive use.

### Room for improvement

Despite the general popularity, there are some problems with Matomo's decisions regarding privacy. By default, the software only offers an opt-out feature for website users. This way, *consent is practically a preset.* In addition, access to usage data is not automated and therefore can be very complex and laborious for users. A common problem which the GDPR mandates explicitly under the heading ["Rights of the data subject"](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation#III_Rights_of_the_data_subject){: target="_blank"}.

On the technical side, the following issues are particularly apparent. Installing Matomo can be a bit of a pain as there are many dependencies that must be pre-installed on the system. This also applies to the requirement to use a dedicated MySQL database, which makes installation even more complex. Last but not least, the tracking script that Matomo uses is extensive and therefore delays the loading of the pages considerably.

---

### Operators and users as equal parties

To address the above mentioned issues we develop a fair and lightweigt web analytics tool that treats operators and users as equal parties. It is called Offen and is [available as a beta version.](https://www.offen.dev/get-started/)

*Offen's default is to NOT collect any data.* Usage data is collected after opt-in only. If users choose to opt in, they have full access to their data. They can delete it any time or opt out completly.

The collected data is presented to users with explanations that describe why a particular metric is relevant and what the privacy implications are. This helps to strengthen trust in operators.

At the same time essential metrics give operators the chance to gain valuable insights in an ethical way. Thereby allowing them to improve their websites and develop ideas for new services. All without violating the privacy of their users.

Offen is open source and will always be available for free with no hidden costs lurking. Operators self host the app and can be sure not to pass on any data to third parties.

The installation is relatively simple and supports the use of SQLite files as well. The tracking script is reduced to a bare minimum and allows pages to load much faster.

To complete the package, the app allows to manage several websites with one login. All website accounts can be shared within teams. A [detailed documentation](https://docs.offen.dev/){: target="_blank"} assists with the installation and daily operation.

### Confidential by design

Our strict focus on data protection also means that there are some Matomo features we will never offer. This includes the export of data and public access to reports without prior login. Furthermore due to the integrated end-to-end encryption Offen does not provide access to the raw data.

### Switch to fair web analytics

We hope this overview helps you to get a better insight into the topic of fair web analytics. If you are passionate about ethical software and want *a truly lightweight and privacy focused alternative to Matomo* you should give Offen a try. Why not let both run parallel for a while and then see how it feels? We are looking forward to your [feedback.](mailto:hioffen@posteo.de)


Find further information in our [explainer](https://www.offen.dev/#bg-explainer) or head to our [get started](https://www.offen.dev/get-started/) section.
