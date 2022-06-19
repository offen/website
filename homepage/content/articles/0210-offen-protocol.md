title: Introducing the Offen Protocol
description: A new vocabulary for software that aims to handle usage data in a transparent manner.
date: 2022-01-17
slug: offen-protocol
url: /blog/offen-protocol/
sitemap_priority: 0.7
image_url: /theme/images/offen-blog-0210-offen-protocol.jpg
author: Frederik Ring
must_read: True
bottom_cta: cookie

# Introducing the Offen Protocol

The most unique feature Offen has to offer is the ability of users to discover their data and manage it in a "self-service" fashion. This might seem like a highly unique feature at first glance, it's also a requirement mandated by GDPR for everyone that collects data. The “rights of the data subject” are defined as:

1. The right to be informed
2. The right of access
3. The right to rectification
4. The right to erasure

Implementing these ideas in Offen we discovered a lot of subtleties and details to be considered. Now that we have built a thorough understanding of how this can work we would like to share what we learned along the way with the public so our ideas and approaches can be adopted and extended by others.

---

### Design goals

#### Conceptual goals

The very foundation of the Offen Protocol is the definition of five actions that clients can take when interacting with a server that is handling their data. On a conceptual level, these actions map closely to the rights of the data subject as defined by GDPR.

Software that aims to handle usage data in a transparent manner can now use this vocabulary to define what is happening at which stage.

> *The ability of users to discover their data and manage it might seem like a highly unique feature at first glance but it's also a requirement mandated by GDPR for collecting data.*

#### Five actions describing the exchange of data:

###### Probe
is used to request additional information about the service. The response might for example contain information about data handling policies or keys used for exchanging data. In GDPR terms, this is the right to be informed.
###### Register
is used in case a client wants to make itself known to the server. In response the client will set a cookie that is used to identify the client on subsequent requests. While this action is not explicitly mentioned in the rights of the data subject, it’s foundational for exercising any of them.
###### Submit
is the action taken when a client transfers data to the client. This action is also supposed to cover the right of rectification.
###### Query
will be used in case clients want to query the server for data. By default, the data returned will always be scoped to the client identifier that is sent along the request. In GDPR terms this is the right of access.
###### Purge
can be used by clients that want to initiate removal of data. In GDPR terms, this is the right to erasure.

#### Technical goals

The Offen Protocol is designed to be used in a server/client setup where both the client and the server speak HTTP, all actions are driven by the client. The server exposes a single endpoint that is used for performing all actions necessary. HTTP already has all of the building blocks needed for the protocol to work, so using it is mostly about adopting the operations vocabulary defined by the protocol and model your transfer of data around it.

> *HTTP already has all of the building blocks needed for the Offen Protocol to work, so using it is mostly about adopting the operations vocabulary.*

#### Non-goals

The Offen Protocol explicitly does not prescribe anything about what kind of data is being shared between clients and the server and how the server models and stores the data itself. The only hard requirement is the use of a user identifier that is handled using HTTP cookies. This also means the protocol is not a good fit when the client is not a browser.

Using cookies might sound invasive at first sight, yet if you evaluate the options on the table without any bias, it is [the most privacy friendly, secure and robust option](/blog/privacy-cookies/) there is. Collection of usage data requires the user to consent in any case, so to us, there is no reason not to use this approach.

### The specification

The full specification document can be [found on the website](https://offen.github.io/protocol/). We won’t dive too deep in this article as changes might still happen, but as we already explained how the defined actions map to behavior, it’s probably interesting to quickly demonstrate how they also map to HTTP:

#### Actions on a technical level

Just like mapping actions to the rights of the data subject, you can map them closely to the HTTP Protocol:

###### Probe
sends a GET request to the given endpoint, omitting the user cookie in case it already exists.
###### Register
sends a POST request to the given endpoint. The server will now set a new user identifier in the response.
###### Submit
sends a PUT request to the server, transmitting arbitrary data.
###### Query
sends a GET request to the server, including the user cookie and also sending optional query parameters to define the scope of the query.
###### Purge
is a DELETE request against the endpoint, requesting deletion of data. It can be scoped down by passing query parameters.

> *Using cookies might sound invasive at first sight, yet if you evaluate the options on the table without any bias, it is the most privacy friendly, secure and robust option there is.*

### Reference implementations

The protocol is not too complicated and maybe even more of a convention than a specification. Nonetheless, we factored out the code we use in Offen and added these implementations to the [GitHub repository](https://github.com/offen/protocol) that also contains the specification itself. The client is supposed to be used in the browser, the server part is written in Golang.

Both can be used as a library or as a guideline for writing your own implementation.

---

### Thoughts? Please share them with us

Do you build an application where the Offen Protocol could be of use? Do you have an idea about how to extend or improve the specification? We’re happy to open the discussion: [tweet at us](https://twitter.com/hioffen), send us [an email](mailto:hioffen@posteo.de), or [open an issue on the GitHub repository](https://github.com/offen/protocol) and let us know what you think.
