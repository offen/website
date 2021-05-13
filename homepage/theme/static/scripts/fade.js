new window.Vue({ // eslint-disable-line no-new
  el: 'body.index .icon',
  data: {
    progress: 0
  },
  mounted: function () {
    var self = this
    window.addEventListener('scroll', function () {
      var scrollTop = parseInt(window.document.documentElement.scrollTop, 10)
      self.progress = Math.min(scrollTop / 100, 1)
    })
  }
})
