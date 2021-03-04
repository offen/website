title: Managing data
description: Milestone 4 comes with enhanced account management, UX improvements and an updated demo version.
date: 2020-06-09
slug: managing-data
url: /blog/managing-data/
sitemap_priority: 0.6
image_url: /theme/images/offen-blog-0060-milestone-4.jpg
image_caption: <a class="link b dim moon-gray" target="_blank" href="https://www.flickr.com/photos/wocintechchat/25926651781/in/album-72157664006621903/">Photo</a> by WOCinTechChat / <a class="link b dim moon-gray" href="https://creativecommons.org/licenses/by/3.0/" target="_blank">CC BY 3.0</a>
author: Frederik Ring
bottom_cta: blog

# Episode Four — Managing data

Milestone 4 - "Managing data" - has been an important one for us. Finishing it means Offen is now close to being feature complete in the scope of our initial plans, and we can start transitioning into a Beta state, meaning we can finally offer a stable product for users to use in production environments.

Before removing the Alpha label, we'd still like to have external audits in Milestone 5, but we are already in touch with potential users and are starting to see installations in the wild. Exciting times ahead!

During Milestone 4 we have released the following versions:

- [v0.1.0-alpha.6](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.6)
- [v0.1.0-alpha.7](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.7)
- [v0.1.0-alpha.8](https://github.com/offen/offen/releases/tag/v0.1.0-alpha.8)

As always, you can download the latest release from [https://get.offen.dev](https://get.offen.dev) or pull it from Docker Hub.

---

## Achievements

### Full fledged account management

Account management for users has been a part of Offen for a while, but in this Milestone we took the time to bring it to a level that it satisfies the needs of real world teams. There are now read-only users, fine-grained controls for sharing access and other management options. We are now looking for feedback in how this works out for setups like smaller dev shops or agencies.

Relevant PRs are: [349](https://github.com/offen/offen/pull/349), [355](https://github.com/offen/offen/pull/355)

### Integration test setup

In Milestone 5, we want to add integration test coverage for all of our user-facing features. To prepare for this, we did research on what tools we can use and how to integrate them into our existing development and CI setup.

We ended up choosing and implementing a setup using [Cypress](https://www.cypress.io/){: target="_blank"}, which is a popular MIT-licensed tool that can run tests in multiple browsers like Chromium and Firefox.

Another great thing about this setup is that is allows us to run automated Accessibility and performance audits (for example using [Lighthouse](https://developers.google.com/web/tools/lighthouse){: target="_blank"} or [Pa11y](https://pa11y.org/){: target="_blank"}.

This has been implemented in PRs [362](https://github.com/offen/offen/pull/362), [365](https://github.com/offen/offen/pull/365) and [368](https://github.com/offen/offen/pull/368)

### Improved demo

For self hosted software like Offen, giving potential users an idea of what the software looks like without having to do a proper install. Many softwares do this by sharing the credentials for a demo account on their website, but in the case of Offen we do not want to do this as it would expose the usage data of our real world users - which is what we are trying to protect with Offen.

This is why we built a downloadable demo of Offen that you can run on your local machine. This demo exists for a while now, but with Milestone 4 we made major improvements to this feature:

- A demo is now populated with randomly generated usage data at start, so that users will get an idea of how an install that is already in use will look like, instead of having to generate usage data themselves beforehand.
- We added a dedicated landing page for demo users that explains them how to use the demo from both a user's and an operator's perspective.

<img class="screencast mt3 mb2" alt="Demo" src="/theme/images/offen-blog-0060-demo.gif"/>

You can try using the demo yourself by running the following snippet:

```bash
curl https://demo.offen.dev | bash
```

Relevant PRs are: [367](https://github.com/offen/offen/pull/367), [346](https://github.com/offen/offen/pull/346), [347](https://github.com/offen/offen/pull/347)

### UX and stats improvements

An ongoing part of our work on Offen is implementing features and fixes that come from our own experience with running our own Offen instance. This is why Milestone 4 contains a few UX improvements and fixes regarding the operator facing Auditorium. Among others, we improved the referrer stats, improved the mobile UX for tabular data and fixed issues with the user flow for resetting your password.

Relevant PRs are [361](https://github.com/offen/offen/pull/361), [363](https://github.com/offen/offen/pull/363), [364](https://github.com/offen/offen/pull/361https://github.com/offen/offen/pull/364),

---

## Next up

### Accessibility Audit

This week already we will have an Accessibility Audit by Stichting Accessibility. We look forward to implementing the feedback we receive and making Offen accessible for all users.

Where possible we will also combine these changes with the backlog of UX improvements we are planning to implement in any case.

### Security Audit

Securing user data is a key aspect of Offen, so it's important to make sure we did not accidentally leave any unwanted loopholes in our system architecture. This is why Milestone 5 also includes a Security Audit by "Radically Open Security". We'll look for proper use of cryptography and a hardened HTTP interface for the server specifically, but if we can pick up other improvements along the way we won't hesitate to implement these.

### Integration Test coverage

Now that we have built a solid foundation for Offen, we want the public to be able to hack on and participate in the development of Offen. To make sure this is a safe and enjoyable journey, we'll add comprehensive integration test coverage for all major user stories there are so that we can always be sure the software keeps working as intended when we review and merge patches and features by others (and ourselves of course).

### Getting ready for external contributions

Closely related to the above, we will also do a thorough check to make sure Offen is ready for external contributions. Is documentation up to date? Does our development setup work reliably across different OSes and hardware? Is it easy to open an issue and get in touch with us? We're definitely looking forward to having the community become a part of our efforts.

---

## Getting your hands dirty

### Adding an integration test

Offen tries to be a slim and lightweight solution but nevertheless, crucial user flows can break unexpectedly and cause frustration for users, operators and developers alike. To prevent such breakages we'll focus on adding integration tests in the next milestone. In case you're curious, why not have a peek at what this looks like right now?

### Testing Opt-In and Opt-Out in the context of the Auditorium

Offen collects data only after opt-in. In addition to the consent banner that is shown on websites that embed Offen, the Auditorium itself allows users to manage their consent status. As an exercise, let's write a test where a user first grants consent, reviews the Auditorium and then opts out again, seeing that data has been deleted.

As noted above integration tests are written using [Cypress](https://www.cypress.io/){: target="_blank"} which has a `mocha`-esque DSL for writing tests. In the `offen/offen` repository, create a new file called `integration/cypress/integration/consent.spec.js`. We're ready to write a basic test now.

N.B.: these examples use `.contains('some text')` for selecting elements as this is very obvious in the context of an example. Our real world tests will use dedicated `data-testid` selectors for targeting DOM elements.*


```jsx
describe('Consent', function () {
  it('displays options for opt-out and opt-in to a user without no decision set', function () {
    cy.visit('/') // visit the index page
    // next, we check whether both options are present and enabled
    cy.contains('Yes please').should('exist')
    cy.contains('Yes please').should('not.be.disabled')
    cy.contains('I do not allow').should('exist')
    cy.contains('I do not allow').should('not.be.disabled')
  })
})
```

Now that we have a basic idea of how such a test looks like, let's add  interaction and check for their immediate effects on the UI:

```jsx
it('displays a link to the Auditorium after opt-in only', function () {
  cy.visit('/')
  cy.contains('Open Auditorium').should('not.exist')
  cy.contains('Yes please').click()
  cy.contains('Open Auditorium').should('exist')
})

it('allows users to opt in after opt out', function () {
  cy.visit('/')
  cy.contains('Open Auditorium').should('not.exist')
  cy.contains('I do not allow').click()
  cy.contains('Open Auditorium').should('not.exist')
  cy.contains('I do not allow').should('be.disabled')
  cy.contains('Yes please').should('exist')
  cy.contains('Yes please').should('not.be.disabled')
  cy.contains('Yes please').click()
  cy.contains('Open Auditorium').should('exist')
})
```

Another very important feature is the ability to delete data:

```jsx
it('allows users to opt out and delete all of their data', function () {
  cy.visit('/')
  cy.contains('Yes please').click()
  cy.contains('Open Auditorium').click()
  cy.url().should('include', '/auditorium/')

  cy.contains('Opt-out').should('exist')
  cy.contains('Opt-out').click()

  cy.contains('Opt-out').should('not.exist')
  cy.contains('Unique websites').prev('p').should('eq', '0')
})
```

Assuming you have a running development environment set up, you can now use `make integration` to see the test runner run the tests you just added.

Of course, there are a lot of other cases to cover for this feature, but you probably have an idea of how the setup works by now and how it allows us to ensure we ship working software.

---

## Feedback? Found a bug?

If you have any feedback, comment or bug report on this milestone release, we'd love to hear from you. [Open an issue](https://github.com/offen/offen/issues) or send us an email at [hioffen@posteo.de.](mailto:hioffen@posteo.de)
