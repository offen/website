new window.Vue({ // eslint-disable-line no-new
  el: '#navigation',
  data: {
    active: false
  },
  methods: {
    toggle: function () {
      this.active = !this.active
    }
  }
})
