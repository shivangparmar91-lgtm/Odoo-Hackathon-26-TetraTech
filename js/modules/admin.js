function switchAdminTab(tab, el) {
  document.querySelectorAll('.admin-panel-content').forEach(c => c.style.display = 'none');
  document.getElementById('admin-tab-' + tab).style.display = 'block';
  document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
}
