title: Consent
description: tbd
date: 2022-04-03
slug: consent-tool
url: /blog/consent-tool/
sitemap_priority: 0
image_url: /theme/images/offen-blog-0220-complete-stable.jpg
author: Hendrik Niefeld
bottom_cta: protocol

# Consent tool

<div class="tweet-container">  
</div>
<script src="https://consent.offen.dev/client.js"></script>
<script>
  const client = new window.ConsentClient({
    host: document.querySelector('.tweet-container'),
    ui: {
      styles: {
        position: 'relative'
      }
    }
  })
  client.acquire('twitter')
    .then(function (result) {
      if (result && result.decisions && result.decisions.twitter) {
        const blockquote = document.createElement('p')
        blockquote.innerHTML = '<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Once again; loud and slow for the people at the back:<br><br>COOKIE POPUPS DID NOT COME FROM THE GDPR. <br><br>Cookie popups came from the adtech industry’s disinclination to comply with ePrivacy law and make it so annoying to avoid surveillance advertising that people wouldn’t bother</p>&mdash; Miss IG Geek (she/her) 🏳️‍🌈 (@MissIG_Geek) <a href="https://twitter.com/MissIG_Geek/status/1524353593385574400?ref_src=twsrc%5Etfw">May 11, 2022</a></blockquote>'
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
