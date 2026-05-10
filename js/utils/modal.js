function showModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.add('open');
}
function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.remove('open');
}
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-bg')) {
    e.target.classList.remove('open');
  }
});
