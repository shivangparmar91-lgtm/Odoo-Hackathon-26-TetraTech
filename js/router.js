function showScreen(name) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('visible'));
  const target = document.getElementById(name);
  if (target) {
    target.classList.add('visible');
    window.scrollTo(0, 0);
  }
  document.querySelectorAll('.sidebar-link, .mobile-nav a').forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') && link.getAttribute('href').includes(name)) {
      link.classList.add('active');
    }
  });
}
