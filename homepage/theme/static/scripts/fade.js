;(function () {
  var icon = document.querySelector('body.index .icon')
  if (!icon) {
    return
  }
  window.addEventListener('scroll', function () {
    var scrollTop = parseInt(window.document.documentElement.scrollTop, 10)
    icon.style.opacity = Math.min(scrollTop / 100, 1)
  })
})()
