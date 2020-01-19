title: Untold roads to v1.0 | Offen
description: Onboarding users onto a product that is still in development needs a thorough plan. These are our conclusions as we work our way to a v1.0 release of Offen.
date: 2020-01-19
slug: untold-roads-versioning-early-stage-software
sitemap_priority: 0.7
sm_image_url: /theme/images/offen-blog-0020-untoldRoads.jpg

<figure class="larger-image mb5">
<img alt="Untold roads" src="/theme/images/offen-blog-0020-untoldRoads.jpg"/>
</figure>

###### 19 Jan 2020, Frederik Ring
# [Untold roads to v1.0](/blog/untold-roads-versioning-early-stage-software/)

After a lot of experimenting, taking detours and having unanticipated revelations while building the foundation for Offen over the last months, the state of the project is starting to settle, and we are eager to get ready for users to install our software, and use it for transparently collecting usage statistics for their websites and applications.

Yet, onboarding users onto a product that is still being developed and that will stay pretty volatile in the near future needs a thorough plan so you do not burn and churn your early adopters by locking them into buggy software without an upgrade path. At the same time, you do not want to lose the velocity and flexibility of an early stage product, enabling you to iterate fast and add well architected features of real value.

While there is lots of theory and writing about how to version and release software that is already established, the way to get there is mostly uncharted territory and has developers figure this journey out for themselves over and over again. In this post we try to collect our considerations, options and conclusions when trying to define *how we want to handle the versioning of Offen on its way from an alpha stage product to a stable v1.0*.

---

## Happy hacking in Alpha

In the earliest stage of any project, you will still be figuring out the interfaces your software has to the outside world. Requirements will evolve, be defined and change yet again - and so will your interfaces. Which is fine for quite a while: as long as your development setup allows you to recreate a fresh environment to work against easily, you are free to break basically anything with every commit.

It's interesting to think about the opportunities this gives you, especially when you consider that they won't last forever. Right now, you still can easily refactor everything in any way you want it to look like. If something in your codebase feels awkward, go refactor and try to find that interface that your application should expose now. Venturing into large refactors because something just doesn't "feel right" might feel counter intuitive when you're at an early stage, and want to get features out of the door and users on board, but large changes will never be as easy for you as they are right now. Once you have users that rely on an established versioning scheme, any refactor will come with a significant toll of compatibility layers and migration scripts. And these will hurt you just like your users.

The only decision that affects the outside world at this point is the following: *how do you communicate the volatile nature of your project to the outside world?* Do you supply packaged releases at all, or do potential users need to build the software from source if they want to use it? In case you do supply releases, a commit-based versioning scheme is probably fine. If people are courageous enough to start using what you are building already, it's best for both parties if you're clear about what you are up to.

<img class="smaller-image mt4" alt="Lots of ways to break your software" src="/theme/images/offen-blog-0020-untoldRoads-A.png"/>

## Lots of ways to break your software

Another thing you will need to think about before you can even start versioning your software are the interfaces you expect your users to use, and those that your users will actually use. Just because you do not document a method of your library, it doesn't necessarily mean it will not be used in the wild. And just because your database migration script assumes a well defined set of tables in the application database, it doesn't mean some user might have started storing other data in there. Applications like Offen will have different constraints than libraries or developer tools do. It's important to know if *you need to interface with data, code or humans* as all of these interfaces come with their own set of constraints.

Steering the code being written and the interfaces exposed into a direction where its usage is as unambiguous as possible will pay off when it comes to knowing what you can actually break with a release. If you explicitly consider something to be unstable and internal, communicating this clearly will be of great help to anyone who's trying to use your product or build upon it.

## When do you even start versioning?

If you develop software, you want others to use it. If you're a user, you want your software to be reliably versioned and updated. This means that at some point, a project will have to start versioning, and its *users will start to project their expectations onto the version numbers being applied*.

When exactly you choose to start doing this depends on what you are focusing on.

### Feature completeness

Depending on your product, it might not make sense to use it before all of the features you are planning to build are included. Venturing down this path, it's a good opportunity for deferring versioning a little longer. If the lack of features makes adoption impossible anyways, you won't hurt it any further if you don't release versioned software.

### Establishing a userbase

Alternatively - assuming your product allows you to do so - you might also want to start shipping way before you are feature complete, establish a userbase, and gain understanding on what these users are doing with your product. These insights come with a price: you need to start versioning. Users that don't have clear and documented ways of upgrading their software without any unexpected surprises stop being users once the version they are using stops being on par with what both you and others are offering. If it's just as easy to install something else as it would be to upgrade to a newer version, why should your users stick?

Just like when working without any approach to versioning *communicating what you are planning to do now that you started versioning* is key. Do you already know how often are you going to release new versions? Where can users find migration and update instructions? If you plan to release breaking versions without an upgrade path: will you backport and patch possible security issues in older versions?

<div class="flex justify-end pb3">
<img class="smaller-image mt4" alt="Detour" src="/theme/images/offen-blog-0020-untoldRoads-B.png"/>
</div>

## Detour: What's in a version number

If you're planning to label a release with a version number any time soon, it's a good idea to reflect on what this new version number actually means. Both to you, and to your users.

While there are lots of debates and fighting going on around that topic many grown up projects seem to adopt a versioning scheme called [Semantic Versioning](https://semver.org/), short SemVer. The idea behind it is to have a `major.minor.patch` version with the following implications:

- If your release contains bugfixes only, only the patch version will be incremented
- If your release contains new features while staying backwards compatible, you increment the minor version
- If your release contains changes that are breaking backwards-compatibility you increment the major version

As a consumer of a software that uses SemVer, this will give you hints about how your upgrade path looks like. If you're currently on version `2.1.0` and `2.2.8` is the latest release, the guarantees given by SemVer tell you that you are able to upgrade without any breakage. Once a `3.0.0` is released, you will need to check what the breaking changes in between versions 2 and 3 are and if you are affected by them.

If this appeals to you, and makes versioning sound like a solved problem for you, you'll be surprised to see how many people oppose its idea. The arguments brought up against it will range from aesthetics - yes, some authors want to see [beauty in their version numbers](http://sentimentalversioning.org/), and I can definitely understand what they're after - to concerns about how you will never be able to tell how your users actually use your software, and you will therefore never be able to determine what defines a breaking change. A simple example: does fixing that bug break someone else's code that is unknowingly relying on that bug or actively working around it? A knee jerk reaction at first sight, publishing the once popular JavaScript library Underscore both at a "standard" versioning scheme (v1.9.1 at the time of writing) and adhering to SemVer (v170.0.0) demonstrates well how much human judgement is still involved in such a seemingly technical and bureaucratic decision.

Another important factor to consider here is which target audience you are actually serving. Will non-technical people really value a version number that tells them about API stability, upgrade paths and such? Could a product like Microsoft Windows really work with such a purely technical versioning scheme? If your audience is far, far away from implementation details, they are probably just interested in you making it work for them.

### SemVer and early stage software

For what their spec calls "initial development", SemVer uses `0.x.x` versions that come with no guarantees at all, which in the scope of this article doesn't leave us with much but the underlying concepts of *breaking changes, features and patches*. Certain scenarios might want to map these to a pre-v1 scheme or at least adopt the same vocabulary when communicating about the changes included in a new release in your changelog.

---

## Flexibility vs Stability

Moving towards a v1.0 every slightly larger project will find itself oscillating between these two goals. What makes decisions in this regard even harder is the fact that both opposites are of equal importance to your project. *Adding new features to a product requires flexibility and stability* at the same time. 

A common approach towards solving this antagonism is the introduction of budgets for both sides. Maybe each iteration has a dedicated budget for breakage and experimenting, just like it has a budget for areas that remain stable and will only change when their interfaces can be guaranteed to stay the same. Maybe every other iteration will focus on stability while the alternating ones will allow for breakage and experimenting. The latter is a concept adopted early on by the Node.js project where an odd version number will signal "punk rock", i.e. unstable and rapid progress, and even version numbers will signal "Fortune 500", i.e. stability.

Whatever approach a project picks, finding a suitable way of balancing these two requirements will be a major enabler of adoption. 

## Migration plans and pains

Sometimes, breakage you want to or have to introduce, can be cushioned softly when you are able to supply *scripts and tooling for users* to adjust their setup so that is is compatible with a new version.

If you are working on a library and its public API has changed, it's sometimes possible to supply users with automated codemods that adjust the usage of deprecated methods so that they match the updated methods. This approach is heavily utilized by for example the React Library. The maintainers are doing a fantastic job in maintaining backwards compatibility and progress. API changes are planned and announced early on, and come with user friendly deprecation messages and [automated codemods](https://github.com/reactjs/react-codemod) that can update your codebase for you.

The same can be done for configuration changes. If an update requires new or changed settings, a script that prompts for the new values and updates the system accordingly will make a great incentive for upgrading.

<img class="smaller-image mt4" alt="Eat your own dogfood" src="/theme/images/offen-blog-0020-untoldRoads-C.png"/>

## Eat your own dogfood

While this is a scenario you cannot easily create just for its own sake, a setup where *you are a user of your own product* - a.k.a. dogfooding - will be pretty insightful in this context.

You as a user will certainly cover only a single use case, yet this one use case will already give you hints on how hard or how easy it is to adopt a new release. Does the effort invested in upgrading justify the improvements made? If you don't feel like it's a good idea to upgrade, other users probably won't do it either.

Keep in mind though that when you represent one usecase, the first hand knowledge your userbase has can give you the big picture. If your project allows, reach out to them and gain understanding on what they actually do and how it compares to what you think they do.

## 1.0 like you mean it

It's impossible to tell how your project will get to a v1.0, but it's very likely it will do so at some point. This will likely feel very good, but *putting that label onto a piece of software will come with certain expectations*.

If you can embrace v1.0 and all the new requirements it brings, they will allow the pace and mode you develop at to change and become more formalized. It makes it easier for yourself to prioritize future goals. It's also easier for external contributors to join something that has stabilized further. In case you feel this is what you want to do, go ahead and draft those release notes.

---

## How we are going to version Offen

Offen's main channel of distribution will be via packaged binary files. Users can run them supervised or unsupervised against a supported set of OSes and database solutions. While we are indeed planning to enable the use Offen's code as the building blocks for other developers to create tailor made, privacy friendly analytics solutions, versioning the code-level interfaces is a non-goal for us at the moment.

Upgrade paths for our users will mostly be bound to the event and key data that is stored in the database, and the way this data is being encrypted and decrypted in the browser, as well as application configuration. Our key considerations here are:

- Can the changes to the database schema included in the changeset be covered by a migration script? Does encrypted data need to be changed as well? Once subject to a versioning scheme, we will aim for only making changes a database migration script can handle.
- Can a compatibility layer be introduced that handles both old and new data at runtime and possibly even upgrades old data when it is decrypted in the browser? For a multitude of reasons, we are planning to use such techniques sparingly and may err on the side of introducing breaking changes instead.
- Does the user need to change or augment runtime configuration in order for Offen to continue functioning? Can these changes be performed automatically or can we supply users with a script that does it for them?
- The user interface is not something we are planning to keep stable from a programmatic perspective. We are working hard to create a consistent and accessible user experience for everyone, but the underlying implementation will be considered private. This means we do not plan to guarantee any stability for things like scraping and headless automation.
- The `/script.js` URI exposed by the web server is locked so that pages that embed the script can always expect a sensible response. We will try to keep the rest of the exposed routes stable, yet if it helps us improving the product in some way, we will change these too.
- The development setup is kept subject to change at any time. Renaming a `make` target may be annoying to contributors once, but we prefer to keep things lean in this regard, and we hope our contributors will do the same.

### Initial development

Right now, Offen is still in the stages of initial development. During this period we will *release an alpha version on each milestone* we hit. We invite users to start using Offen by deploying these releases (or by building any revision themselves), but we also need to make sure that while we are still in initial development, we will possibly *introduce breaking changes* or changes that are *hard to upgrade*.

### From v0.1 to v1.0

Once all features we deem necessary for Offen to be used in the wild are included, we are planning to continue as following: kicking off, we will release an officially supported *v0.1.0*.

Working our way from there to a v1.0 we will follow these principles:

- Bugfixes and new features that do not require any particular actions when upgrading other than replacing binaries will be released on a rolling basis and increment the *patch version*. This means deployment can be kept up to date by downloading and re-deploying new versions.
- A new *minor version* is released in the following cases:
    - There is an upgrade path from the previous minor version, yet *it requires manual interaction* before upgrading. This might mean following instructions for changing configuration values supplied by us or running scripts against your installation that perform necessary updated.
    - The new version *contains a breaking change* that does not have an upgrade path. We hope this rarely happens, but we also need to guard against unforeseen changes, so it's probably a good idea to state the possibility of such a release happening upfront. Longterm quality of the product will benefit massively from keeping this option.
- *Security related bugfixes will be backported to the previous minor version* (if it exists). This means that even if you cannot or do not want to upgrade to the next minor version, your application will stay safe in the near future. Note that these backports will stop once a deployment is two minor versions behind though.

When releasing a *v1.0* we will have worked hard to have a good upgrade story for users of early versions, but we'll also spare you the fortune telling we'd have to do to predict when and how this is going to happen.

We definitely do invite you to start experimenting with Offen right now and also to start using it in user-facing scenarios once we are at *v0.1.0*. Get in touch if you have feedback or need help with configuring, running or upgrading Offen.

---

## Where are we right now?

Laying out detailed plans for the future is one thing, seeing how they came into life and changed is yet another. If you want to see how we managed to translate the plans described above into reality check our [GitHub repository](https://github.com/offen/offen) and the [releases we have done by now](https://github.com/offen/offen/releases).
