title: Privacy focus? Consider the cookie.
description: Using cookies does not necessarily equal tracking your users. Learn how you can use cookies to respect the privacy of your users.
date: 2020-12-28
slug: privacy-cookies
sitemap_priority: 0.7
image_url: /theme/images/offen-blog-0140-privacy-cookies.jpg
author: Frederik Ring
bottom_cta: quality

## Privacy focus? Consider the cookie

Whoever [drafted the idea for HTTP cookies](https://tools.ietf.org/html/rfc2109){: target="_blank"} back in 1997 likely did not anticipate having created a technology that is as disputed, discussed and also disliked as it is today. A non-technical user of the internet might be under the impression that cookies are an utterly useless privacy disaster that bring you nothing but consent banners filled with dark patterns, and enable advertisers to track you on literally every website ever.

And while there are definitely problems with the modern day usage of cookies, with very good reasons to regulate their usage, they can also be used to enhance privacy on the web. Using cookies does not necessarily equal tracking your users or invading their privacy. In this article we would like to show you how you can use cookies to respect and enhance the privacy of your users.

> *Using cookies does not necessarily equal tracking your users or invading their privacy.*

---

### Collecting data should require consent, no matter your implementation details

Inside the European union the so called "[Cookie Directive](https://en.wikipedia.org/wiki/Privacy_and_Electronic_Communications_Directive_2002){: target="_blank"}" mandates acquiring consent from users for setting non-essential cookies. Similar laws exist for example in California. The internet being a global phenomenon, you are very likely to be subject to these regulations in one way or the other the moment you serve any non-trivial website. Many developers like to complain vocally about so called "cookie banners", and the number of sleazy patterns that try to trick users into consenting makes these complaints relatable. A solution that does not require user consent must surely be the better option for privacy, right?

It's not that easy though. If you think user privacy from the ground up, how do the technical details of your implementation matter? We'd argue they do not matter much. If you want to collect non-essential data from your visitors (analytics data in the case of Offen) in a privacy friendly way, you should be asking for user consent. No matter how your technical solution for doing so looks like, and no matter what regulations currently say. If you're not doing this and instead come up with something that allows you to avoid "the cookie banner" for collecting non-essential data, you are not building a privacy friendly solution, you are building a regulations friendly solution.

Think about it in this way maybe: if you feel like you really do not want ask users for consent, then maybe this is a good hint to reevaluate if you really need to collect that data you would need user consent for. Privacy values choices, and simply not making use of non-essential features should be an option for users always. Not convinced? Think about why ad blockers are so popular.

In case your conclusion is that you do need to collect the data, don't be afraid about that consent banner too much. There is absolutely nothing that requires you to use the overly complex solutions you can find on the internet way too often. Consent banners can be unobtrusive, concise and clear starting the moment when you accept a "No" just as much as you accept a "Yes".

> *Consent banners can be unobtrusive, concise and clear starting the moment when you accept a "No" just as much as you accept a "Yes".*

---

### Essential, non-essential, and what's the difference?

Regulations around data protection and collection often distinguish essential and non-essential features, and this makes a lot of sense. If a user can log in to your service and you have to store a session identifier in a cookie to enable this, it is perfectly fine to do so without consent. Having to provide credentials over and over again for every request made against your server would render your service unusable, hence it is an essential feature.

Non-essential features are usually revolving around performance and analytics. Collecting analytics data for a website definitely is not required for the user to use your service. This means it is non-essential usage and you should be asking for consent before doing so. Regulations around this topic only cover cookies, but taking privacy seriously, you would apply this principle to all techniques. On a side note, [quantity does not necessarily mean quality in web analytics](https://www.offen.dev/blog/opt-in-quality/).

Most importantly, both essential and non-essential segments require making sure their technical implementation is secure and respects user privacy as much as possible.

---

### Technical considerations for using cookies in a privacy friendly manner

Offen is a fair web analytics software. This is a promise we can only deliver with an opt-in only solution. Not having to work around a "cookie banner" (for us, that's a feature) we are free to solve any task at hand in the most privacy friendly way we can come up with. And in many cases, this means using cookies. The following collects a few guidelines we've been following when building Offen.

#### Choosing privacy friendly identifiers and values

Cookies are essentially a key-value store. It might seem tempting to store detailed and highly specific information in the values here, but let's have a look at what that would mean from a privacy perspective.

For example let's say you wanted to write a feature test, checking for whether you can set cookies in the first place, you might come up with a mechanism that writes a random value to a certain key and tries to read it again. If the value can be read and is not altered the check succeeds. However, this means the feature test does also make the user identifiable by that random token, which is a privacy implication that is not tolerable for such a basic task. Instead, you can use a static value and also a static key for all users that ever run the feature test, thus making them indistinguishable. The guideline therefore is to always use static values that are the same for each and every user, unless you really need to identify users.

If you find yourself in the situation where you do need to create an identifier that is unique to a user, cookies will give you the privacy advantage of being able to create a truly random and anonymous value (e.g. a UUID) that is not tied to any user or device specific information (as compared with for example tracking sessions by hashing a combination of IP address and User Agent string on the server, [which leaks a lot of private information, even when stored in its hashed form only](https://edps.europa.eu/data-protection/our-work/publications/papers/introduction-hash-function-personal-data_en){: target="_blank"}). Ensure you use a well-tested library for creating such identifiers. Also, consider the option of periodically rotating such tokens so that others that inadvertently get hold of such a token can only make use of it for a limited period of time.

> *Cookies will give you the privacy advantage of being able to create a truly random and anonymous value that is not tied to any user or device specific information.*

#### Allow users to delete their cookies

One of the best privacy features of cookies is: users can delete them at any time, disassociating themselves with the data tied to the previous identifiers instantly. This will never work if you use server side solutions relying in UA strings and/or IP addresses. Many users might know how to do this, but if you take privacy seriously and you are using cookies for your service, why not implement such a feature within?

#### Do not use Third Party cookies

A cookie is always bound to the domain it has been issued from. In a scenario where a page loads resources from different domains, this means that some of these resources may set or use cookies bound to a different domain than the host document is served from.

These cookies are called third-party cookies and are pretty bad for privacy, considering they can be used to follow users around the web when such third party resources are being loaded on a multitude of websites.

Luckily, usage of third party cookies is already being heavily restricted by browser vendors, and there are concrete plans to disallow their usage entirely until 2022.

However, when designing an application you might find yourself in situations where using third party cookies might become a requirement. In case such a requirement pops up, it's probably best to take a step back and reconsider the overall architecture of your application's HTTP schema. Using a third party cookie shows your application would be leaking information (both essential and non-essential) across domain boundaries. Consider consolidating all logic that requires to share such data under a single domain so that data can be neatly protected by other mechanisms such as `SameSite`.

#### Same site cookies

To preserve privacy for the values stored in the cookies you set yourself, you will want to restrict their usage to to a first-party or same-site context. In order to allow for fine grained control of this behavior, [the `SameSite` attribute](https://web.dev/samesite-cookies-explained/){: target="_blank"} got introduced in [RFC6265bis](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-03#section-4.1){: target="_blank"}.

This allows you to now set a value of either `Strict`, `Lax` or `None` for the `SameSite` attribute, limiting the scenarios in which your browser will send cookie information with requests to your domain.

Considering this article is about building secure and privacy focused applications, using `None` should not be an option here. The major difference between `Lax` and `Strict` is that `Lax` allows for cookies to be sent along with so called "top level" requests, i.e. if your site is using cookies to store a session identifier for login and a 3rd party site links to your site, using `Lax` will allow users to click that link and be logged in instantly, whereas using `Strict` would not send those cookies on the first request, but only on those initiated by the document loaded from your domain itself.

Depending on your use case, both options are valid choices and make sure you respect your users' privacy.

> *One of the best privacy features of cookies is: users can delete them at any time, disassociating themselves with the data tied to the previous identifiers instantly.*

#### Secure by default

Cookies are designed to be sent in the headers of HTTP requests. This means that when not using an encrypted connection over TLS, the values sent in plaintext and are subject to possible eavesdropping by third parties in between your user and your server.

Even while using HTTPS is becoming the default nowadays, HTTP still does exist and it's totally possible in certain setups to accidentally make HTTP requests, even when HTTPS would be available.

To protect cookie values to be sent over insecure, plain-text connections, set the `Secure` attribute on your cookies. This way, the browser will make sure to send cookies only when a request is using the `https` protocol.

#### HTTP cookies and JavaScript cookies

Cookies can be set and read in two different manners, either by using client side JavaScript, using the `document.cookie` interface or by using the `Cookie` and `Set-Cookie` HTTP Headers.

By default, cookies set by one method can be read by the other and vice-versa. This does create privacy implications though: as modern websites can load a large amount of third party code in the client, this exposes information stored in cookies to everyone who can run code on your website, e.g. third party widgets or similar.

To avoid a situation like this, the `HttpOnly` attribute can be used. When set on a cookie, it means reading from and writing to it is not possible using client side JavaScript, it can only be accessed by the server, which gives you much tighter control over the data contained.

`HttpOnly` should be the default setting when issuing cookies. Only disable when there is no other way to achieve what you need to achieve. When you have to do so, consider the information stored in that cookie public, so do never store any user identifiers, session data or similar information in a cookie that is not `HttpOnly`.

#### Scope access using domains and paths

Access rules for a cookie can be defined by using the `Domain` and `Path` parameters. The `Domain` defines the domain a cookie is sent to and `Path` limits its submission to certain sub-paths of that domain. So for example a cookie with a domain of `www.offen.dev` and a path of `/blog`  would be sent along with requests of a URL beginning with `https://www.offen.dev/blog` only.

There are some interesting details about the `Domain` parameter: it is optional and when not specified at all, the cookie will be bound to the very domain that is setting the cookie. No sibling or subdomains will be allowed to access its value. When you specify a domain, this domain and all of its subdomains will be allowed to access that cookie.

Sometimes, you will also see domain values starting with a dot like `.offen.dev`, which used to indicate that the cookie should be sent to all subdomains, yet modern browsers will treat the domain [with or without the leading dot in the same way](https://tools.ietf.org/html/rfc6265#section-4.1.2.3){: target="_blank"}. It is not needed anymore.

These two mechanisms should be leveraged from the start when you are using cookies. Start by not specifying a domain and the most restrictive `Path` value you can use and only relax these rules if it is strictly necessary for your application to function. Be extra stringent about this when handling cookies that contain identifiers.

#### Expire cookies you do not need

Cookies come in two flavors: Session cookies and persistent cookies. Session cookies will be purged by your browser once your [browsing session](https://html.spec.whatwg.org/dev/history.html#browsing-session){: target="_blank"} ends, persistent cookies define a point of time where they expire themselves. Technically, it's not possible to issue a cookie that is never expiring, although you can create one that expires in a 100 years, resulting in the same effect for the end user.

Once again using the principle of [Datensparsamkeit](https://martinfowler.com/bliki/Datensparsamkeit.html){: target="_blank"} as a guideline, it's a good habit to start with all cookies being session cookies. Only make those persistent where the benefits justify the consequences of storing possibly sensitive data like user identifiers on a user's device for a prolonged period of time. Consider the trade-offs for your users when defining the expiry and err on the side of security and privacy. If you really need a very long lived cookie, look into if you could periodically refresh its value so that it does not create a potentially unwanted tracking identifier for others.

> *Start with all cookies being session cookies. Only make those persistent where the benefits justify the consequences of storing possibly sensitive data.*

---

### Wrapping up

If you find yourself building a product where privacy is important - just like we do when building Offen - feel encouraged to consider cookies as an option for your tasks. Very often, it's a robust and simple choice that is beneficial for your user's privacy when done right, and the implicit requirement for acquiring user consent is a major privacy feature.

Do you have comments or feedback about this article or about Offen in general? Tweet at us [@hioffen](https://twitter.com/hioffen){: target="_blank"} or email us at [hioffen@posteo.de](mailto:hioffen@posteo.de).
