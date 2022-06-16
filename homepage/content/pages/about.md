title: About | Offen
description: Who we are, what we do, who supports us and how you can can get in touch.
slug: about
bottom_cta: fair
sitemap_priority: 0.3

# About

Hi, we are [Frederik Ring](https://www.frederikring.com/) and [Hendrik Niefeld.](http://niefeld.com/) These are our tools to make the web a better place.

#### *[Offen Web Analytics](/#bg-explainer)*

The fair web analytics tool. Let your users access their data and gain valuable insights at the same time. Open source, lightweight, self hosted and free. [Learn more.](/#bg-explainer)

#### *[analytics.txts](https://www.analyticstxt.org/)*

A proposed standard which allows websites and services to disclose information about their usage of analytics software and user tracking. [Learn more.](https://www.analyticstxt.org/)

#### *[Offen Protocol](/blog/offen-protocol/)*

A specification for the discoverable exchange of data over a single HTTP endpoint. [Learn more.](/blog/offen-protocol/)

#### *[Offen Consent Tool](/blog/consent-tool/)*

A lightweight solution for managing user consent on websites. [Learn more.](/blog/consent-tool/)


---

### What is this thing called "my data" and why does seemingly everyone want to get hold of it?

It has a ring, gives a slight spine-chilling sensation and generates a whole lot of clicks: consumer magazines like German "Computer Bild" caution about ["Google espionage"](https://www.computerbild.de/artikel/cb-Ratgeber-Kurse-Wissen-Was-weiss-Google-ueber-Sie-2799009.html) just like the internet has countless tutorials on turning off numerous ["data leeches"](https://praxistipps.chip.de/datenkrake-windows-10-so-schalten-sie-auffaellige-funktionen-ab_99652). Interestingly, diving into these realms will have you accidentally catching the next toolbar, malware infection or [even worse](https://blog.malwarebytes.com/cybercrime/2012/10/pick-a-download-any-download/).

Yet, many internet users still do not know what really is happening to their data. Public relation activities trying to calm the public - as recently undertaken by Facebook [for example](https://www.zeit.de/digital/datenschutz/2019-01/social-media-facebook-mark-zuckerberg-ads-privacy-business-model-transparency) - end up being rather disturbing instead of creating transparency or adding any value to the public debate. Denelle Dixon, COO of Mozilla, just publicly [warned the European Commission](https://blog.mozilla.org/blog/2019/01/31/mozilla-raises-concerns-over-facebooks-lack-of-transparency/) about the dangerous effects an opaque apparatus such as Facebook can have on society. Updated Terms and Conditions only parenthetically mention that newly created Google accounts will now hand over real names to third parties for [advertising purposes](https://www.propublica.org/article/google-has-quietly-dropped-ban-on-personally-identifiable-web-tracking).

<div class="flex justify-end pb5">
<img class="smaller-image" alt="Detour" src="/theme/images/gfx-deepdive-A.png"/>
</div>

As a regular user of the internet, are you really being spied upon? *What exactly is "my data"?* Can a website operator see my name when I'm using it? Does it know about my Email address or my phone number? Does it know which other websites I have been visiting, which search query led me to the site in the first place, what I have recently purchased online, or who I am acquainted with?

> "If you have something that you don't want anyone to know, maybe you shouldn't be doing it in the first place."
>
> [Eric Schmidt](https://www.eff.org/de/deeplinks/2009/12/google-ceo-eric-schmidt-dismisses-privacy) (at this time CEO of Google), 2009

We would like to turn the tables on this much quoted statement and apply it to the operators of services and websites instead of their users. The analytics software Offen *transparently and uncompromisingly discloses what data is being collected and what it is being used for* to the users.

### For users

Visiting a website or using a web application that utilizes Offen, the user gains access to and ownership of the usage data collected. As a guiding principle, data collection is Opt-In only. Consent can be revoked at any time, just like users can choose delete their data retroactively. The cookie used by Offen allows viewing all of the associated metrics so that users can *assert themselves what is being collected and what isn't*. Data is being displayed in an accessible and articulate manner and each metric comes with explanations about its usage, relevance and possible privacy implications.

<img class="smaller-image-2 mt3" alt="Lots of ways to break your software" src="/theme/images/gfx-deepdive-B.png"/>

### For operators

Operators of small and mid-sized websites and web applications are faced with growing challenges not only since the introduction of GDPR: how do they gain insights into what users are interested in and which of the features offered are being used? Is it possible to showcase *transparent and considerate handling of user data* - i.e. neither being spy or data leech - without surrendering and abandoning usage metrics altogether?

Choosing Offen, websites and web applications obtain a free, open and robust tool for collecting and analyzing relevant usage data. The insights gained enable continuous improvement of these services while still respecting their user's privacy. *Opening up the data to the users does not constitute a disadvantage, but strengthens the relationship with them* by being entirely transparent.

### Part of the public debate

Transparently handling usage data in the open creates mutual trust while still enabling operators to collect needed usage statistics. Offen is designed to be a mediating agent only, and does not side with either users or operators. Sharing knowledge between the two parties creates opportunities for an *open and fact based discussion* about user data and privacy. Users gain insights into what data is being collected and what these data points are used for, just like they learn about which kind of data is not part of the collection. They are enabled to reach self-determined decisions about what they consent with and what they disagree with when it comes to privacy on the web, also in other contexts than analytics.

We want to exemplify that it is time to depart the age of ["data capitalism"](https://www.zeit.de/digital/datenschutz/2019-01/datenschutz-nick-couldry-datenkolonialismus-datenhandel/komplettansicht) and to create *technologies and infrastructure that are transparent, open and oriented towards the common good*

<div class="flex justify-end">
<img class="smaller-image mt2" alt="Detour" src="/theme/images/gfx-deepdive-C.png"/>
</div>

###  Technology

At runtime, Offen Web Analytics is just mediating exchange between users and operators. Usage data is collected in conformance to GDPR and with the concept of ["Datensparsamkeit"](https://martinfowler.com/bliki/Datensparsamkeit.html) in mind. All user data is encrypted in the browser so that it can only ever be accessed by the users themselves or the matching operator. While being collected in the context of a website or application, neither operators nor third party scripts have any possibility to access the usage data. Offen itself doesn't have any way of decrypting, processing or even selling the gathered data at any point.

The software itself, as well as *all the used tools are open source*, [project planning and technical specification](https://github.com/offen/offen) take place in the open and actively solicit feedback from the general public.

Users and operators are given intuitive and accessibility-focused tools for analyzing and managing their data in the form of a web application and a browser extension. Operators deploy the service using a simple script tag.

---

### Modus Operandi

Developing and running Offen can only work out when it is entirely *free of any kind of economic constraints or goals* and its only objective is *contributing to the common good*. Development of a prototype is reliant on public grants or similar funding sources. Long term development and maintenance of the software is tied to resources granted by foundations or being donated by the public.

[![NLnet Foundation](/theme/images/nlnet-logo.svg){:width="160px" height="60px" class="mt4"}](https://nlnet.nl/)

We are happy to work with [NLnet Foundation,](https://nlnet.nl/) which actively supports our efforts as part of its [Next Generation Internet](https://nlnet.nl/NGI/) initiative.

### Contact

*Feel free to contact us with any kind of feedback.* From criticism and praise to contributions or support, everything is welcome. Get in touch.

[hioffen@posteo.de](mailto:hioffen@posteo.de)  
[PGP Key](/theme/74B041E23DB29D552644CEB1B18C633D6967FE3F.asc)
