function toggleCheck(el) {
  el.classList.toggle('checked');
  const checkbox = el.querySelector('.check-box i');
  if (el.classList.contains('checked')) {
    checkbox.classList.replace('fa-square', 'fa-check-square');
  } else {
    checkbox.classList.replace('fa-check-square', 'fa-square');
  }
  updateCheckProgress();
}

function updateCheckProgress() {
  const items = document.querySelectorAll('.check-item');
  const checked = document.querySelectorAll('.check-item.checked');
  const total = items.length;
  const count = checked.length;
  const fill = document.querySelector('.progress-fill');
  const text = document.getElementById('progress-text');
  
  if (total > 0 && fill && text) {
    const percentage = Math.round((count / total) * 100);
    fill.style.width = percentage + '%';
    text.innerText = count + ' / ' + total + ' items packed';
  }
}

function resetChecklist() {
  document.querySelectorAll('.check-item.checked').forEach(el => toggleCheck(el));
}

function addChecklistItem() {
  const nameInput = document.getElementById('new-item-name');
  const catSelect = document.getElementById('new-item-category');
  if (!nameInput.value) return;

  const groupContainers = document.querySelectorAll('.checklist-group');
  let targetGroup = groupContainers[groupContainers.length - 1].querySelector('.checklist-items');
  
  const newItem = document.createElement('div');
  newItem.className = 'check-item';
  newItem.setAttribute('onclick', 'toggleCheck(this)');
  newItem.innerHTML = '<div class="check-box"><i class="far fa-square"></i></div> <span>' + nameInput.value + '</span>';
  
  targetGroup.appendChild(newItem);
  nameInput.value = '';
  closeModal('add-item-modal');
  updateCheckProgress();
}
