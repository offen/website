;(function () {
  var toggle = document.querySelector('#nav-toggle')
  if (!toggle) {
    return
  }
  toggle.addEventListener('click', function () {
    toggle.classList.toggle('active')
    var navList = document.querySelector('#navigation .nav-list')
    navList && navList.classList.toggle('active')
  })
})()
