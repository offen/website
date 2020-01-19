title: Laying the foundation for fair web analytics | Offen
description: Our milestone 1 achievements include extensible architecture, a localization option and an improved server structure.
date: 2019-12-12
slug: laying-foundation-for-fair-web-analytics
sitemap_priority: 0.7
sm_image_url: /theme/images/offen-blog-0010-milestone1.jpg

<figure class="larger-image mb5">
<img alt="Milestone 1 - Laying the foundation for fair web analytics" src="/theme/images/offen-blog-0010-milestone1.jpg"/>
</figure>


###### 12 Dec 2019, Hendrik Niefeld
# [Episode One — Laying the foundation for fair web analytics](/blog/laying-foundation-for-fair-web-analytics/)
Milestone 1 is completed. This is what we've achieved in the last six weeks.

---

### Extension through middleware
We have further refined the existing application architecture to make it more robust and accessible to both contributors and people who want to build upon Offen. As a developer, you can transparently control additional behavior by adding or removing middleware.

### Easy to test drive
Download a single binary file and run it on your local computer to get an Offen instance up and running immediately. At the moment this setup only supports Linux. Windows and MacOS will follow soon.  
[Download binary](https://8342-180605180-gh.circle-artifacts.com/0/tmp/artifacts/offen-stable.tar.gz){: target="_blank" data-button="yellow"} 

### Develop without complex setup
Docker and Docker-Compose are the only hard requirement for you to develop Offen. We have successfully tested this setup under Linux, Windows and MacOS. Head over to our wiki for instructions how to get the setup up and running.  
[Open wiki](https://github.com/offen/offen/wiki/Developing-offen#setup){: target="_blank" data-button="yellow"}

### Lightweight and accessible interfaces
The *Auditorium* is ready for a dry run. It's a functional prototype for accessing and managing user data. We opted for [Choo](https://choo.io/){: target="_blank"} as the application framework and [Tachyons](https://tachyons.io/){: target="_blank"} as the CSS framework.

### Ready to localize
You can now localize all user-related content in server- and client-side applications. At the moment English is the only supported locale, but we would be happy to add more locales soon. Contributors wanted after milestone 3 is completed.  
[Get in touch](mailto:hioffen@posteo.de){: data-button="yellow"}

### Read the docs
The work on our wiki has started. Including documentation for [developers](https://github.com/offen/offen/wiki/Developing-offen){: target="_blank"} as well as for [website operators](https://github.com/offen/offen/wiki/Running-offen){: target="_blank"} who want to deploy and run Offen.

### No reverse proxy required
We have further hardened and improved the HTTP server that Offen exposes. If you want to, you can already expose this server to the Internet without having to run a reverse proxy in front of it.

### Up next
*Episode Two — Collecting data securely* will feature user opt-in, userland cryptography, meaningful statistics and much more. We'll be right back.

---

### Deep dive
Interested in the details? Want to get your hands dirty? Head over to our GitHub repo.  
[Open milestone 1 Pull Request](https://github.com/offen/offen/pull/192){: target="_blank" data-button="black"}
