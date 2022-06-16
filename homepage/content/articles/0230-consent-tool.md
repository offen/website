title: Say hi to the Offen Consent Tool
description: A lightweight solution for managing user consent on websites.
date: 2022-06-16
slug: consent-tool
url: /blog/consent-tool/
sitemap_priority: 0.7
image_url: /theme/images/offen-blog-230-consent-tool.jpg
author: Hendrik Niefeld
must_read: True
bottom_cta: protocol

# Say hi to the Offen Consent Tool

This article is about our new Offen Consent Tool *[Fast forward to the details here.](#consent-tool)*

---

### What’s wrong with consent?

“Cookie banners are just a pain in the ass.” or "Why are there so many buttons? I just don’t care.” - that's what you hear when a conversation revolves around today's web experience.

But if we consider solely the situation within the EU, the scenario is actually quite simple. GDPR states that data processing, any compelling reasons aside, is only legal if consent is freely given, specific, informed and unambiguous. However, the fact that this implies a real choice by the data subject is often where the problems start.

The very fact that consent requests are often described as “cookie banners” is the first major misconception here. Relevant requests to invade the privacy of users are thereby framed as useless information about the use of certain technical specifications. This is all the more disappointing as cookies can actually be [quite useful for protecting privacy.](/blog/privacy-cookies/)

it is usually not the consent request that is annoying but the fact that so many operators do not accept a possible “no” from the user. A whole arsenal of dark patterns and UX gimmicks is employed to willfully circumvent the actual intention of the GDPR, the informed decision of the user, and force a "yes". So it's not surprising that so-called "consent management tools" have become established, which suggest to be able to increase the rate of user consent.

Lucky are those who have found a way to completely avoid consent requests. But unfortunately, all too often, data collection is not abandoned here, but only some technical loophole is exploited that lies in some grey area of jurisdiction.

### Our take

As we develop a [fair and lightweight web analytics software](/) that treats operators and users as equal parties our attitude to the issue of consent is clear: Consent is a must. Absolutely. We need the user's consent for anything that may contribute to their identification.

We are committed to privacy and the rights of users, but we also support the legitimate interest of operators to improve their services. Requesting consent is, in our opinion, the only way to mediate meaningfully between these two aspects. And as a side effect, the [quality of the collected data is significantly improved.](/blog/opt-in-quality/)

> *Nevertheless, the simplest option is all too often ignored: Do you really need all this?*

We believe that a large part of the operators collect data even though they have neither time nor sufficient experience to evaluate it for any real benefit. Similar questions arise when using other third-party services. Why, for example, not integrate fonts yourself into a website with little effort?

Not at least this is due to the fact that many developers of SaaS tools are still not willing to support the operators in properly implementing the applicable laws. They are hesitant about an important principle when it comes to consent. Accept a "no" as much as a "yes”.

<div id="consent-tool"></div>

This leads to another essential question of principle that is asked far too rarely. Does a service “make no sense” if some of the users want to remain anonymous? Then maybe there is something wrong with it in the first place…



### The Offen Consent Tool

Having outlined the reasons for a consistent implementation of consent, let’s consider the technical aspects. Many elements that are implemented on web services today provide no or at best inconvenient solutions. For operators of small and medium-sized services it is very tedious to integrate these different consent requests correctly.

Your analytics tool thinks it doesn't need a consent request? There are tweets embedded in your blog articles? What’s with that TikTok you want to share with your readers? The nice font featured on your page, is it provided by a third party? How do you collect consent for all of this?

Well, we have developed a tool for these needs. Say hello and give it a try. We used it to conditionally embed the following Tweet.

<div class="consent-container w-100 flex justify-center mt3">  
</div>
<div class="tweet-container mb4">  
</div>

<script src="https://consent.offen.dev/client.js"></script>
<script>
  const client = new window.ConsentClient({
    host: document.querySelector('.consent-container'),
    ui: {
      styles: {
        position: 'relative'
      }
    }
  })
  client.acquire('twitter')
    .then(function (result) {
      if (result && result.decisions && result.decisions.twitter) {

        const blockquote = document.createElement('div')
        blockquote.innerHTML = '<blockquote class="twitter-tweet"><a href="https://twitter.com/hioffen/status/1510854517092491270?ref_src=twsrc%5Etfw"></a></blockquote>'

        document.querySelector('.tweet-container').appendChild(blockquote)
        const script = document.createElement('script')
        script.src = 'https://platform.twitter.com/widgets.js'
        document.querySelector('.tweet-container').appendChild(script)
      }
    })
    .catch(function (err) {
      console.error(err)
    })
</script>

The *Offen Consent Tool* keeps your data footprint small by never storing data about consent decisions on your end. As a lightweight solution for managing user consent on websites, it focuses on these objectives:

- No server side persistence of consent decisions
- No need to assign user identifiers or similar, meaning no additional tracking vectors
- Consent decisions are secured from interference of 3rd party scripts
- Users can revoke their consent decisions and any traces at any time by clearing their cookies or using the provided UI
- Operators can customize the UI elements in use to match their design

Installation requires you to be able to configure deploy a simple web server to a dedicated domain. Linux binaries and a Docker image are provided, or you can build the server for any other platform. However, it is not a solution to the requirements of GDPR. Operators must comply with the applicable regulations themselves.

### Get started today

The *Offen Consent Tool* is using 1st Party Cookies to store user's consent decisions. To enable this mechanism, you need to deploy the respective server to a sibling domain, i.e. if you plan to use the tool on `www.example.com`, it should be served on a domain like `consent.example.com`. The tool can serve any number of domains at once, so it's possible to use the same deployment for multiple domains at once.

Next deploy the application to a domain like `consent.example.com`. On the host site `www.example.com` embed the client script:

```jsx
<script src="[https://consent.example.com/client.js](https://consent.example.com/client.js)">
```

which exposed `window.ConsentClient`. In your client side code, construct a new client instance pointing at your deployment and request user consent for the desired scope(s):

```jsx
const client = new window.ConsentClient({ url: '[https://consent.example.com](https://consent.example.com/)' })
client
.acquire('analytics', 'marketing')
.then((decisions) => {
if (decisions.analytics) {
// load analytics data
}
if (decisions.marketing) {
// trigger marketing tools
}
})
```

##### The *Offen Consent Tool* further allows you to create the binary yourself and provides a development setup. It can also be used as a library and be integrated into any web server written in Golang.
[Learn more](https://github.com/offen/consent){: data-button="full"}


##### Read the Docs for further assistance with installation and use.
[Open Docs](https://github.com/offen/consent/blob/main/MANUAL.md){: data-button="outline"}

### Please let us know
This is our latest development in [a series of privacy-friendly tools](/about/) designed to make the web a better place.

If you have any feedback, comments or bug reports about this or other project, we would love to hear from you. Open an [issue](https://github.com/offen/consent/issues) or send us an email at [hioffen@posteo.de](mailto:hioffen@posteo.de).
