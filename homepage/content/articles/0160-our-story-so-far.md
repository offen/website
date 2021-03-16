title: Our story so far
description: All about why and how we develop a fair and open source web analytics software.
date: 2021-03-09
slug: our-story-so-far
url: /blog/our-story-so-far/
sitemap_priority: 0.7
image_url: /theme/images/offen-blog-0160-our-story-so-far.jpg
author: Hendrik Niefeld
bottom_cta: cookie

# Our story so far

Hi there. This is our story on how we develop fair and open source web analytics software. A note first. This story is not finished yet. We are just about to take the next major step. But more about that later.

### A genuine problem

Privacy on the web has been a major point of discussion for quite some time now. Since we both have been running different websites for a long time, this has always been an issue for us as well. However, when the GDPR came into force in the EU in mid 2018, the old questions once again arose. What kind of cookies can I use? How can I get valid user consent for them? What content must be included in my privacy policy?

The choice of web analytics tool to be used was a key factor in answering all these questions. It soon became clear that we needed an alternative to Google Analytics in order to achieve real progress and make our websites fully privacy friendly. Last but not least this would also avoid all future uncertainties in relation to GDPR.

While searching for a new analytics tool, we realized that there was no offer that allowed a really fair data transfer between website operator and website user. With all the tools we found, users did not know what kind of data was collected or how it was used. They could not access or delete their data. A problem that GDPR explicitly addresses under the heading "Rights of the data subject".

> *While searching for a new analytics tool, we realized that there was no offer that allowed a really fair data transfer between website operator and website user.*

### How it all began

That made us think. Obviously, as website operators, we had an interest in seeing what happened on our pages. Of course we wanted to know how we could improve our services. But could this not be done in a fair way in which operators and users are treated as equal parties?

A few more months had to pass and in late 2018, after further in-depth research, we were convinced. Yes of course it could be done. And if it does not exist yet then we should build it ourselves!

We knew right away that our web analytics tool would have to go much further than anything we were aware of at the time regarding privacy. Only with a consequent attitude towards fundamental issues such as consent and users access to data we could claim a niche that had not been filled so far. The term 'fair data transfer' was not yet in our minds at that time. In retrospect, however, this is the best summary of all the ideas that we were dealing with.

Furthermore we were soon confident that in this consequence only an Open Source and non-commercial approach was suitable for developing such an analytics tool. Which immediately raised the question how to finance such a rather idealistic venture.

> *Our web analytics tool would have to go much further than anything we were aware of at the time regarding privacy.*

### Business as unusual

Sure, we have both heard the term 'business plan' before, but frankly it is definitely not our area of expertise and we lack the necessary drive to deal with such things.

Please dont get us wrong here. We have the greatest respect for the hard work of people who build their own idea into a sustainable business. This of course also applies to all teams out there who run privacy friendly web analytics tools with a SaaS approach. The success of these projects shows that there is a market for these products that continues to grow.

We, however, wanted to do something different right from the start. Yes, we too had initially thought of offering a kind of SaaS solution. But the development and operation should have been carried out largely by financing that does not pursue profit interests. It did not happen exactly this way and that turned out to be a good thing.

### Finding support

We had already started looking for support in late 2018. And as we delved deeper into the matter, we were surprised how many funding sources for the development of open source software exist worldwide. Nevertheless there are of course a lot of applicants. Therefore we believe that you have to carefully consider your application.

In our experience, the key to preparing is to find out as much as possible about the intention of a funding program. Who are the funding backers? Which people decide on the granting? Which projects have been funded so far? Does my project really fits into this whole constellation? Based on these factors you have to make a honest decision. Is the effort of an application really worth it?

With this approach we were able to focus on one German and a few international calls. And by summer 2019 we had submitted a handful of applications. To our great pleasure our proposal to the [NGI Zero Privacy & Trust Fund of the Dutch NLnet Foundation](https://nlnet.nl/PET/){: target="_blank"} was then successful.

> *We were surprised how many funding sources for the development of open source software exist worldwide.*

### Get to work

We realized how lucky we were immediately when we started working with the people from NLnet. This is because the support there goes far beyond the financial. In in-depth discussions we together sharpened our vision of the product and worked out a realistic roadmap for its development.

Clearly, we did not always happen to agree during these discussions. But it was precisely this friction that has made a decisive contribution to our project. It was during this process we came to the conclusion that our web analytics tool should only be offered as a self host solution. A decision which, in retrospect, helped us a lot to focus on the more essential topic of fair data transfer.

At the end of 2019 things started to take shape. We decided on the name 'Offen' and set out with the goal of creating a first working version within about 30 weeks. At the same time a documentation should be created and our project should be promoted to an interested audience.

Here it should be mentioned that we both still work part-time in our old jobs. A decision that we have made well-considered. Of course this slows you down, and you reach a lively environment late with your product. But this scenario also gives you the necessary distance to think deeper about how to create a real alternative to existing solutions.

> *This scenario also gives you the necessary distance to think deeper about how to create a real alternative to existing solutions.*

### Achieved to date

The first thing to say is that it took us a little longer. We reached the goals set out in our product plan at the beginning of September 2020. So we needed about 38 weeks to get there. This wasn't due to major issues regarding technical and editorial implementation. It was much more about personal preferences in terms of time budgeting and the impact of the Covid 19 pandemic, which of course also hovers over our personal lives.

5 months have already passed since the official completion of the funding program. During this time, we have taken Offen even a good deal further. These are all key features available with our latest [v0.3.0 release.](https://github.com/offen/offen/releases/tag/v0.3.0)

* *Fair data collection*  
Usage data collection is opt-in by default. Users have full access to their data with detailed explanations of metrics and terms. They can opt-out completely at any time or only delete existing usage data.

* *Compelling analytics*  
A clear presentation of all essential metrics regarding the use of your website, to help you improve your service. Usage data is only stored for 6 months and then automatically deleted. All event data is encrypted end-to-end.

* *Easy to deploy*  
Offen runs on-premises, or in any other deployment scenario that fits your need. You can easily analyze multiple websites within one installation. All website accounts can be shared within teams. A detailed documentation on how to run Offen is available.

### Up next

As mentioned at the beginning, the next major step is ahead. In the upcoming stage we want to develop Offen to a release v1.0 that deserves its name.

This will involve enhancing the UX to a level that can fully compete with other web analytics tools. This includes raising website users awareness of the unique Offen feature - granting full access to one' s own data.

Furthermore, by factoring out tools from our code we will create an open access for all developers interested in the topic of fair data transfer. In addition to that we want to formalize the general approach we use in Offen and define a protocol spec that others can adopt, ideally generating an ecosystem of compatible client and server implementations.

NLnet is willing to support us once again in these ambitions. This time from the [NGI Zero Search and Discovery Fund.](https://nlnet.nl/discovery/){: target="_blank"} We are of course more than happy about this and would like to take this opportunity to thank the whole NLnet team for their confidence in our work.

> *We want to formalize the general approach we use in Offen and define a protocol spec that others can adopt, ideally generating an ecosystem of compatible client and server implementations.*

### Happy to hear from you

Do you have feedback on the latest Offen release or our next steps? What is your experience in developing open source tools? Are you as enthusiastic about fair data transfer as we are?

Drop us a [tweet](https://twitter.com/hioffen){: target="_blank"} or [email](mailto:hioffen@posteo.de) and feel invited to work together to drive this idea forward.
