title: Hosting Offen on a budget | Offen
description: These are some real world options for hosting Offen on a budget. Let's compare how they relate in terms of ease of deployment, performance and pricing.
date: 2020-06-28
slug: hosting-offen-on-budget
sitemap_priority: 0.7
sm_image_url: /theme/images/offen-blog-0070-budget.jpg

<figure class="larger-image mb5">
<img alt="Hosting on a budget" src="/theme/images/offen-blog-0070-budget.jpg"/>
</figure>

###### 28 Jun 2020, Frederik Ring
# [Hosting Offen on a budget](/blog/hosting-offen-on-budget/)

Using self-hosted software like Offen when you're on a budget can seem daunting as you usually don't know too much about the performance requirements of the software you are planning to use beforehand. Once you do know, you might have locked in yourself already.

In this article we collect a few real world options and scenarios for hosting Offen on a budget and compare how they relate in terms of ease of deployment, performance and pricing.

---

*Prerequisite:* All of the below assumes you have registered one or multiple domains on which you run your applications and websites, and can set [A](https://en.wikipedia.org/wiki/List_of_DNS_record_types#A){: target="_blank"} or [CNAME records](https://en.wikipedia.org/wiki/CNAME_record){: target="_blank"} for these. If you do not know what this means exactly: it is a default feature in almost all packages that let you register a domain. Your provider or registrar surely can help you with further support if you need any. Read more about it in our [dedicated subdomain tutorial.](https://docs.offen.dev/running-offen/setting-up-using-subdomains/){: target="_blank"}

## Scenarios where Offen is a good fit

Offen is designed to be lightweight and easy to install. It's probably not a good fit if you need advanced features like interaction heatmaps or tracking the funneling of users across multiple sites, but if you want a lean way of knowing how people use your website without invading your user's privacy, Offen is a solid choice.

### *Handling multiple low-ish traffic sites on a single instance*

One scenario we are targeting is deploying an Offen instance and using it for analyzing multiple low traffic sites (like for example blogs or side projects). Offen allows you to create as many accounts as you like, so you can have one bucket per each of these projects that you want to run analytics on.

It is also important to understand that even if these projects are run on different domains, you can still setup distinct CNAME records for each of these sites so that Offen can run on the same domain as your target. When you log in, you can always view and analyze usage data across all of the accounts, even if they are served from different hostnames. Offen is also able to automatically acquire free and auto-renewing SSL certificates from Let's Encrypt for each of these domains.

As for data storage, you will likely want to use the default SQLite option in this scenario which stores data in a file on the host system.

### *Handling a single high traffic site*

If you are working on a bigger project with a lot of traffic, you might consider deploying a single instance for that project only. Also, this is a scenario where we would recommend using a dedicated database server instead of using a local SQLite file, as it would allow you to scale Offen further while your traffic grows.

---

## Some available hosting providers

This list is a non-exhaustive collection of hosting providers that we happen to know and have used ourselves. We are in no way affiliated with any of these, don't earn any money when you install Offen there, and definitely don't want to push you anywhere. We do want you to use Offen though, of course, but it's always your choice where to run it. If you know of any other good option, tweet them our way [@hioffen](https://twitter.com/hioffen){: target="_blank"}.

### [AWS](https://aws.amazon.com/){: target="_blank"}

The obvious choice for hosting your Offen instance in the AWS ecosystem is probably using EC2 (which is a virtual server). For handling Offen in any of the above scenarios a `t3.nano` instance is sufficient, which - at the time of writing - bills at *USD 3.90 per month*. In case you have just recently signed up for AWS, you could also run Offen using the *free tier usage plan* that gives you one free `t2.micro` (this, by the way, is also how we are currently running our own instance).

If you decide to use a dedicated database server, AWS offers managed databases as a service called RDS, but this service is relatively expensive (pricing maps to the cost of the underlying EC2 instance and instances are big). A cheaper option would be using a Lightsail VM (which currently costs USD 5.00) and configuring it to use the PostgreSQL or MySQL presets that give you a running database server out of the box.

As Offen will provide free SSL certificates for you, so this will not incur any additional costs.

The lowdown on AWS:

- USD 3.90 per month (plus USD 5.00 if you need a database) or maybe even free for 12 months if you just signed up
- Offen needs to be installed manually from the command line

---

### [Heroku](https://www.heroku.com/){: target="_blank"}

Heroku is famous for making deployment of web based software as easy as possible, and it indeed lets you deploy Offen from within your browser using our Heroku preset.

[Open Heroku preset](https://github.com/offen/heroku){: target="_blank" data-button-mb3="outline"}

Heroku has a free tier that theoretically lets you deploy Offen and a database for free. The only caveat with this is that you will need to provide your own SSL certificate in this scenario, which makes it relatively complicated to get going. In addition to that Dynos (this is Heroku's name for a virtual server) on the free plan fall asleep when they are not used, so applications tend to be relatively sluggish when going down that route.

If you would upgrade your plan to a "Hobby" plan which clocks in at *USD 7.00 per month* you get an always-awake Dyno, a Postgres Database under the free plan and free SSL provided by Heroku (Offen cannot acquire certificates itself when it is deployed behind the Heroku Routing Mesh).

This option is probably on the more expensive side of things, but it's definitely easy to manage, especially for a non-technical audience.

The lowdown on Heroku:

- Free if you can live with servers falling asleep and can provide your own SSL certificate. This setup can only serve a single domain.
- USD 7.00 per month if you need proper performance and managed SSL
- Can be set up from inside your browser

---

### [DigitalOcean](https://www.digitalocean.com/){: target="_blank"}

DigitalOcean provides virtual servers in a product they call Droplets. The cheapest variant - which is enough to host Offen for one of the above scenarios - costs *USD 5.00 per month*. On this droplet you can install Offen yourself in whatever fashion you prefer (Docker, systemd, something else) or use our prebuilt image.

[Open prebuilt DigitalOcean image](https://github.com/offen/digitalocean){: target="_blank" data-button-mb3="outline"}

If you need a dedicated database server, you can either use the managed Postgres offering (which is relatively expensive) or add another Droplet, installing a prebuilt PostgreSQL or MySQL image.

SSL certificates can be acquired by Offen in this scenario without any additional cost.

The lowdown on DigitalOcean:

- USD 5.00 per month (plus another USD 5.00 if you need a dedicated database)
- Setup can be done using a prebuilt image but still requires command line interaction

---

### [Linode](https://www.linode.com/){: target="_blank"}

Feeling "close to the metal" in a good way, Linode offers virtual servers on shared instances. At *USD 5.00 per month* you get a Linux server that you can use to install and serve your Offen instance. There is no dedicated database offering, so if you wanted to use a dedicated database you would need to install MySQL or PostgreSQL on another shared instance. Presets are available for these.

Offen can handle SSL certificates for you in this scenario as well, so this does not incur additional costs.

The lowdown on Linode:

- USD 5.00 per month (plus another USD 5.00 if you need a dedicated database)
- Offen needs to be installed manually from the command line

---

## Where to head next

If you made a choice and want to deploy your own Offen instance, head over to our [Installation tutorials](https://docs.offen.dev/running-offen/tutorials/){: target="_blank"} where you will get further guidance on what to do next and how to get your instance up and running. And in case you get stuck or need help, file an [issue](https://github.com/offen/offen/issues){: target="_blank"}, [tweet](https://twitter.com/hioffen){: target="_blank"} or [email](mailto:hioffen@posteo.de){: target="_blank"}.
