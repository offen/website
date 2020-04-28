title: Displaying data | Offen
description: Our milestone 3 achievements include an improved UX, a Heroku deploy option and full Safari support.
date: 2020-04-13
slug: displaying-data
sitemap_priority: 0.7
sm_image_url: /theme/images/offen-blog-0050-milestone-3.jpg

<figure class="larger-image mb5">
<img alt="Milestone 3 - Displaying data" src="/theme/images/offen-blog-0050-milestone-3.jpg"/>
</figure>

###### 14 Apr 2020, Hendrik Niefeld
# [Episode Three  — Displaying data](/blog/displaying-data/)
Milestone 3 has been completed. This is what we have achieved in the last ten weeks.

---

### Improved UX
The Auditorium for users is now annotated with explanations of all metrics as well as analytics-specific terms. It also contains an FAQ section. In general, new metrics were added and the UX was refined for users and operators.
<img class="screencast mt3 mb2" alt="browser setup" src="/theme/images/offen-blog-0050-explainer.gif"/> 
These updates are already *up and running in our own instance* for users. Opt in and open the Auditorium.  
[Check it out](https://analytics.offen.dev/){: target="_blank" data-button="outline"} 

### Working in teams
If you want to improve your services with transparent and fair web analytics, it is very likely that you collaborate in groups. Therefore, in a first draft we have added basic utilities for managing user logins and accounts. These tools will be further refined during milestone 4.

### Convenient setup
Using the command line can be a bit intimidating. This is why we have added an in-browser setup screen for a more intuitive setup. You can now use your browser to perform the initial setup.
<img class="screencast mt3 mb2" alt="browser setup" src="/theme/images/offen-blog-0050-browserSetup.gif"/> 

### Goodbye Choo, hello Preact
[Choo](https://choo.io/){: target="_blank"} was a great choice to build dynamic UIs very quickly. But as the Auditorium grew, we noticed a lack of mechanisms to break interfaces into components. So we migrated the application to [Preact.](https://preactjs.com/){: target="_blank"} A better way to use modern paradigms for programming interfaces.

### Verifying download integrity
Our binaries are now signed with a GPG key. After downloading Offen, you can now check if the binary you want to use is the one we intend to distribute.
[Learn more](https://docs.offen.dev/running-offen/downloads-distributions/#verifying-the-binaries-signatures){: target="_blank" data-button="outline"} 

### Safari now fully supported
At the end of milestone 2 we noticed problems with the way the Safari browser stores keys. We fixed this by adding a dedicated fallback mechanism. [Give it a try.](https://analytics.offen.dev/){: target="_blank"}

### Ready in one minute
Self-hosting is ideal for privacy focused software. Based on free resources, you can now deploy a production ready Offen instance to Heroku in a jiffy. 
<img class="screencast mt3 mb2" alt="browser setup" src="/theme/images/offen-blog-0050_oneClickDeploy.gif"/> 
We are currently working on further 1-click options for platforms such as [DigitalOcean](https://github.com/offen/digitalocean){: target="_blank"} and YunoHost.  
[Deploy to Heroku](https://heroku.com/deploy?template=https://github.com/offen/heroku/tree/maste){: target="_blank" data-button="outline"}

### Happy Birthday to us
Offen is now [one year old.](https://github.com/offen/offen/commit/3a50763bbd93c9c655fad002e94c340a623ee613){: target="_blank"} We made some progress on our way to develop a self hosted and transparent alternative to established web analytics tools. 

But it is not yet the time for standing ovations. There is still a lot to be done. If you like, you can help us. *Stay tuned and provide us with your feedback.* Thanks in advance!

### Up next
*Episode Four — Managing data* will feature a more fine grained account management and the collecting and implementing of first user feedback. We'll be right back.

---

### Deep dive
Interested in the details? Want to get your hands dirty? Take a look at our code.
[Open GitHub repo](https://github.com/offen/offen){: target="_blank" data-button="full"}
