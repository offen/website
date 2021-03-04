title: Resilience and documentation
description: With milestone 5 we finally got rid of the alpha label, improved testing as well as licensing and upgraded our documentation.
date: 2020-07-22
slug: resilience-documentation
url: /blog/resilience-documentation/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0090-milestone-5.jpg
author: Frederik Ring
bottom_cta: blog

# Episode Five — Resilience and documentation

Maybe the most exciting milestone in our current journey, Milestone 5 ends with Offen finally stripping off that `alpha` label we have been carrying around for quite a while now, and which admittedly might have scared away some potential users. The good thing about keeping it this long though is that we can feel pretty confident to release working software. We'll still defer the 1.0 for a while and start with `v0.1.0`, but from now on we really mean it: Install Offen in production, we are confident it'll be a good choice.

This means that during Milestone 5 we have released the following versions:

- [v0.1.0-alpha.9](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.9)
- [v0.1.0-alpha.10](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.10)
- [v0.1.0](https://github.com/offen/offen/releases/tag/v0.1.0)
- [v0.1.1](https://github.com/offen/offen/releases/tag/v0.1.1)

As always, you can download the latest release from [get.offen.dev](https://get.offen.dev) or pull it from Docker Hub.

---

## Achievements

### Accessibility Audit

As an NGI Zero project we are lucky enough to have great people in our network by default. This time Stichting Accessibility helped us with an A11y audit of Offen. This audit resulted in helpful feedback and action points for us to improve upon the A11y aspects of the Offen Auditorium and make Offen an analytics tool for everyone.

Relevant PRs are: [386](https://github.com/offen/offen/pull/386), [387](https://github.com/offen/offen/pull/387), [389](https://github.com/offen/offen/pull/389), [393](https://github.com/offen/offen/pull/393)

### Security Audit

Another really helpful experience was having Offen audited from a security perspective by the wonderful people from Radically Open Security. We had a great time looking at Offen together, checking for exploits, leaky crypto, security issues and discussing general design questions that came up while working on Offen. We did not find major flaws, but instead came up with a couple of very good ideas about how to make Offen more secure and harden the server even further. These have been implemented by now and are included in the latest release, so make sure to update.

Relevant PRs are: [399](https://github.com/offen/offen/pull/399), [400](https://github.com/offen/offen/pull/400), [401](https://github.com/offen/offen/pull/401), [405](https://github.com/offen/offen/pull/405), [406](https://github.com/offen/offen/pull/406)

### Community approved handling of licensing

With help from the FSFE, we adopted [REUSE](https://reuse.software/){: target="_blank"}, a standard and tooling around the handling of licensing in non-small repositories. Having integrated a dedicated check for REUSE compliance into our CI pipeline allows us to stop worrying we have forgotten something, and will give everyone access to all licensing information needed to use or reuse Offen in all scenarios.

In addition to that we now also automatically generate a NOTICE file from our dependency tree that we can include in our binary distributions, making sure every dependency is properly attributed when others download and use Offen. You can see it in action being served from our own Offen instance here: [offen.offen.dev/NOTICE.txt](https://offen.offen.dev/NOTICE.txt)

Relevant PRs are: [383](https://github.com/offen/offen/pull/388), [414](https://github.com/offen/offen/pull/414), [415](https://github.com/offen/offen/pull/415)

### Integration tests

Putting more effort into an ongoing effort, we added more integration tests using the setup from Milestone 4. We now cover users and operators, so we'll hopefully ship fewer and fewer regressions with each test added. Also, we now run integration tests against all supported database backends (SQLite, MySQL, Postgres) so we can be sure all installation methods are always considered.

Relevant PRs are: [395](https://github.com/offen/offen/pull/395), [413](https://github.com/offen/offen/pull/413), [394](https://github.com/offen/offen/pull/394)

### Improved documentation

Improving our documentation has been an important part of this milestone as it means our move to a non-alpha version is supported by making Offen even more accessible to developers and operator that want to install Offen or hack on it.

To keep the docs in sync with our ongoing development efforts, we merged our existing `offen/docs` repository into `offen/offen`. This allows us to document new features and changes while they are being developed and also makes versioned documentation available on [docs.offen.dev](https://docs.offen.dev). It also moves the docs closer to the code so that developers do not need to do any more context switching during development.

Relevant PRs are: [392](https://github.com/offen/offen/pull/392), [396](https://github.com/offen/offen/pull/396), [402](402), [407](https://github.com/offen/offen/pull/407), [411](https://github.com/offen/offen/pull/411)

---

## Next up

### More deployment targets and tests

Offen's deployment story as a single binary file and no external database required is relatively easy, yet there is always room to improve, especially for a non-technical audience. While we already have tested installing Offen successfully on a multitude of providers, ranging from industry leaders like AWS to offbeat offerings like Uberspace, we want to look into more options. While doing so we will share our findings with the public so they can use our experience when installing Offen themselves. We will also look into how we can make running Offen even easier. Maybe this one configuration value isn't even needed. Maybe creating your first account can be even easier. Let's find out.

### Reaching out to the community

When the last months it has been the two of us working on Offen exclusively, moving into Beta is a good time to get the community involved. We want to know where our users would like to see us heading, and when want to know how we can make Offen more accessible for external contributors. Now that we have defined the foundation, Offen can serve the community better the more that it's a community effort.

### Defining where we want to head next

Upcoming Milestone 6 will be the last one in our current funding round by NGI Zero PET. It's been an incredibly supportive and inspiring journey which taught us a lot, one thing being that we are onto something with Offen.

To allow us to sustain development further, we are going to flesh out ideas on where we want to take Offen (come have a look at our [roadmap](https://github.com/offen/offen/projects/1)), but also on how we can make the ideas behind Offen accessible to the public in a way that people can build software and tools that follow the same set of guiding principles.

Once this is defined, we will apply for new funds. Let us know if you know of any good opportunities for a project like Offen.

---

## Getting your hands dirty

### Load testing the hardened Offen server

An important part of Milestone 5 was hardening the HTTP interface of Offen, which in most cases will be exposed to the internet directly, without any reverse proxy or similar in front. So why not do a load test and see how far we can take it?

The tools we'll be using to perform the load test is called [vegeta](https://github.com/tsenart/vegeta){: target="_blank"}, which you can install using `go get` (or you download the binaries from GitHub):

```
go get -u github.com/tsenart/vegeta
```

Then, fire up a demo instance of Offen on your machine. This is really easy using our script:

```
curl -sSL https://demo.offen.dev | bash
```

When done, this will tell you about a port that has been opened on your `localhost`, which we will now use for the load test.

Let's start with something really simple, load testing the (static) index page:

```
$ echo "GET http://localhost:40125" | vegeta attack -duration=5s | vegeta report

Requests      [total, rate, throughput]         250, 50.20, 50.17
Duration      [total, attack, wait]             4.983s, 4.98s, 2.661ms
Latencies     [min, mean, 50, 90, 95, 99, max]  974.69µs, 2.664ms, 2.579ms, 3.389ms, 3.61ms, 4.433ms, 6.595ms
Bytes In      [total, mean]                     796500, 3186.00
Bytes Out     [total, mean]                     0, 0.00
Success       [ratio]                           100.00%
Status Codes  [code:count]                      200:250  
Error Set:
```

This looks pretty good, latencies are minimal and all requests succeeded. Next, let's use some URL that actually uses the database connection. The easiest way is using `/healthz` which checks if the connection is alive before responding 200:

```
$ echo "GET http://localhost:40125/healthz" | vegeta attack -duration=5s | vegeta report

Requests      [total, rate, throughput]         250, 50.20, 50.18
Duration      [total, attack, wait]             4.982s, 4.98s, 1.731ms
Latencies     [min, mean, 50, 90, 95, 99, max]  296.96µs, 1.094ms, 1.079ms, 1.363ms, 1.462ms, 1.716ms, 1.758ms
Bytes In      [total, mean]                     2750, 11.00
Bytes Out     [total, mean]                     0, 0.00
Success       [ratio]                           100.00%
Status Codes  [code:count]                      200:250
```

Looks like this also passes the test without any problems.

Now, let's try doing something more interesting: trying to flood the login endpoint with requests using the known `demo@offen.dev` login and a random password and see if we can break something here. To do so create a `login.json` file that looks like this:

```json
{"username":"demo@offen.dev","password":"xy18293kxmak"}
```

Now, we can run the actual test:

```
$ echo "POST http://localhost:40125/api/login" | vegeta attack -body=login.json -duration=5s | vegeta report 

Requests      [total, rate, throughput]         250, 50.20, 0.00
Duration      [total, attack, wait]             29.095s, 4.98s, 24.115s
Latencies     [min, mean, 50, 90, 95, 99, max]  312.109µs, 369.558ms, 1.033ms, 1.521ms, 9.637ms, 16s, 28.935s
Bytes In      [total, mean]                     30259, 121.04
Bytes Out     [total, mean]                     14000, 56.00
Success       [ratio]                           0.00%
Status Codes  [code:count]                      401:9  429:241  
Error Set:
401 Unauthorized
429 Too Many Requests
```

which shows us a few things:

- relatively early, rate limiting kicks in, which means most requests will see a 429 status code
- The few requests that do not see a 429 will be throttled so that response times increase exponentially. This means someone that mistypes their password once or twice will notice no difference when logging in, where someone who is trying to brute force their way into a successful login will take months to do so.

Load testing gets even more interesting when you look at sending events. If you feel like it, craft a few payloads and see what happens.

---

## Feedback? Found a bug?

If you have any feedback, comment or bug report on this milestone release, we'd love to hear from you. [Open an issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de.](mailto:hioffen@posteo.de)
