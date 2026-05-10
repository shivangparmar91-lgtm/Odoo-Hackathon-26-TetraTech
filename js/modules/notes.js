function addNote() {
  const title = document.getElementById('note-title').value;
  const content = document.getElementById('note-content').value;
  const day = document.getElementById('note-day').value;
  const city = document.getElementById('note-city').value;

  if (!title || !content) return;

  const container = document.getElementById('notes-container');
  const card = document.createElement('div');
  card.className = 'note-card';
  card.innerHTML = `
    <div class="note-header">
      <h3 class="note-title">${title}</h3>
      <div class="note-actions">
        <button class="btn-icon"><i class="fas fa-tag"></i></button>
        <button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove()"><i class="fas fa-trash"></i></button>
      </div>
    </div>
    <p class="note-body">${content}</p>
    <div class="note-meta">${day} · ${city}</div>
  `;
  container.prepend(card);
  closeModal('add-note-modal');
  
  document.getElementById('note-title').value = '';
  document.getElementById('note-content').value = '';
  document.getElementById('note-day').value = '';
  document.getElementById('note-city').value = '';
}

function filterNotes(type, el) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
}
