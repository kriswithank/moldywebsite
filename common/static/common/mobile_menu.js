function toggleMenu() {
  var navMenu = document.getElementsByClassName('nav-menu')[0];
  var menuButton = document.getElementsByClassName('menu-button')[0];

  if (navMenu.className == 'nav-menu mobile-menu-inactive') {
    navMenu.className = 'nav-menu mobile-menu-active';
    menuButton.style.backgroundImage = "url(/static/common/images/menu-icon-active.png)";
  } else {
    navMenu.className = 'nav-menu mobile-menu-inactive';
    menuButton.style.backgroundImage = "url(/static/common/images/menu-icon.png)";
  }
}
