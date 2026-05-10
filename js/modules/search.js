function runSearch() {
  const input = document.querySelector('.topbar-search');
  const label = document.getElementById('searchResultLabel');
  if (input && label && input.value) {
    label.innerText = 'Showing results for "' + input.value + '"';
  }
}
