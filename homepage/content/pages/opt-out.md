Title: Opt-out | Offen
description: Prevent Offen from aggregating the actions you have taken on participating websites.
save_as: opt-out/index.html
exclude_from_sitemap: true
sm_image_url: /theme/images/offen-logo-social-media.jpg

## You are opted out

This will prevent Offen from aggregating the actions you have taken on participating websites.

Operators now cannot draw any conclusions from your actions via Offen. At the same time, however, they *cannot create a better experience* for you and other users.

<script>
  var vault = document.createElement('iframe')
  vault.style.display = 'none'
  vault.setAttribute('width', '0')
  vault.setAttribute('height', '0')
  vault.setAttribute('frameBorder', '0')
  vault.setAttribute('scrolling', 'no')
  vault.addEventListener('load', function (e) {
    vault.contentWindow.postMessage({
      type: 'OPTOUT',
      payload: {
        status: true
      }
    }, '*')
  })
  vault.src = 'https://vault-alpha.offen.dev'
  document.body.append(vault)
</script>
