title: Collecting data securely
description: Our key milestone 2 features are user consent, improved crypto implementation and an extended set of stats.
date: 2020-01-31
slug: collecting-data-securely
url: /blog/collecting-data-securely/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0030-milestone-2.jpg
author: Hendrik Niefeld
bottom_cta: blog

# Episode Two — Collecting data securely

We finished milestone 2. Here is what we' ve been doing for the last 8 weeks.

---

#### Collecting data only with consent
A first approach to one of our major features is implemented. Websites that embed the Offen script now display a user consent banner. In case of user's deny, no other requests than loading the script are made from then on.  
[Learn more](https://offen.offen.dev/){: data-button="outline"}

#### Accidental leaks don't expose data
We encrypt all event data before it leaves the browser. [Two types](https://github.com/offen/offen/pull/270) of crypto implementations are used for this. This allows us to handle user data from both https and http-only sites securely.

#### What exactly happens on your website?
The insight into user behavior has been improved. Still, no sensitive user information is collected. We have added seven additional statistics like Average Page Depth as well as Landing and Exit Pages. Here you find an [overview of all added stats.](https://github.com/offen/offen/pull/270)

#### We are live
The current state of *Offen runs on this domain.* You should have noticed our conset banner by now. Opted in? Head to the [Auditorium](https://offen.offen.dev/auditorium/) to manage your data. If not, please have a look at our [Explainer.](https://offen.offen.dev/)

*We welcome any feedback* on this key subject. Did our banner text inform you sufficiently? Which issues have been left open? How can we do better? Thanks in advance.  
[Send feedback](mailto:hioffen@posteo.de){: data-button="outline"}

#### Testdrive on your system
Whether you are a developer that want to contribute or a website operator that wants to test Offen. Have a demo up and running in no time on your local machine. Download and install a single binary file on Linux, Windows or MacOS.  
[Download demo](https://github.com/offen/offen/releases/download/v0.1.0-alpha.2/offen-v0.1.0-alpha.2.tar.gz){: data-button="outline"}

#### Feeling adventurous?
Offen is under active development but with the introduction of the user consent banner has become usable for the general public. If you are brave enough you can use our [latest alpha release](https://github.com/offen/offen/releases/latest/) in a production environment.

#### We need to talk about Safari
Currently, the way we store encryption keys securely on the client side does not work in Apple's Safari browser. Fortunately, our improved opt-in flow will allow us to resume Safari support in milestone 3. Please bear with us until then.

### Up next
*Episode Three — Compelling data display* will feature informed consent, annotated statistics and a faster display of usage data. Stay tuned.

---

### Deep dive
Interested in the details? Want to get your hands dirty? Head over to our GitHub repo.  
[Open milestone 2 Pull Request](https://github.com/offen/offen/pull/270){: data-button="full"}
