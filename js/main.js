let currentTripType = localStorage.getItem('tripType') || 'india';

document.addEventListener('DOMContentLoaded', () => {
  const userStr = localStorage.getItem('user');
  if (userStr) {
    try {
      const user = JSON.parse(userStr);
      if (user && user.full_name) {
        const initials = user.full_name.split(' ').map(n => n[0]).join('').toUpperCase();
        document.querySelectorAll('.avatar-circle').forEach(el => {
          el.innerText = initials;
        });
      }
    } catch (e) {
      console.error('Error parsing user data for avatar:', e);
    }
  }
});


    // Toggle India / Intl globally
    function switchTripType(type) {
      currentTripType = type;
      localStorage.setItem('tripType', type);
      
      // Toggle visibility of specific content sections
      document.querySelectorAll('.trip-mode').forEach(el => {
        el.style.display = 'none';
      });
      document.querySelectorAll('.' + type + '-mode').forEach(el => {
        // preserve inline-flex/flex etc if needed, but since we rely on CSS display logic mostly, let's reset to ''
        el.style.display = '';
      });
      
      // Update currency symbols dynamically
      document.querySelectorAll('.currency-symbol').forEach(el => {
        el.innerText = type === 'india' ? '\u20B9' : '$';
      });
      
      // Update UI active buttons
      document.querySelectorAll('.trip-type-btn').forEach(btn => {
        btn.classList.remove('active');
        if(btn.dataset.type === type) btn.classList.add('active');
      });

      // Update background of login screen
      const loginScreen = document.getElementById('screen-login');
      if(loginScreen) {
        if(type === 'intl') loginScreen.classList.add('intl-bg');
        else loginScreen.classList.remove('intl-bg');
      }

      runSearch(); // re-render search to update list dynamically
      updateProgress();
    }

    // Navigation & Auth
    

    

    

    // Modals
    function showModal(id) { document.getElementById(id).classList.add('open'); }
    function closeModal(id) { document.getElementById(id).classList.remove('open'); }
    document.addEventListener('click', e => { if (e.target.classList.contains('modal-bg')) e.target.classList.remove('open'); });

    // Toasts
    function showToast(message) {
      const container = document.getElementById('toast-container');
      const toast = document.createElement('div');
      toast.className = 'toast';
      toast.innerHTML = `<i class="fas fa-check-circle"></i> <span>${message}</span>`;
      container.appendChild(toast);
      setTimeout(() => toast.classList.add('show'), 10);
      setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
      }, 3000);
    }

    // Search
    const searchDataIndia = [
      { name: 'Paragliding Bir Billing', meta: 'Himachal · 2h · ⭐4.8', price: '₹3,500', icon: '🪂' },
      { name: 'River Rafting Rishikesh', meta: 'Uttarakhand · 3h · ⭐4.9', price: '₹2,200', icon: '🚣' },
      { name: 'Camel Safari Jaisalmer', meta: 'Rajasthan · ⭐4.7', price: '₹1,800', icon: '🐪' },
      { name: 'Scuba Diving Goa', meta: 'Goa · ⭐4.8', price: '₹4,500', icon: '🤿' },
      { name: 'Houseboat Kerala', meta: 'Kerala · ⭐4.9', price: '₹6,500', icon: '🛶' },
      { name: 'Trek Triund', meta: 'Himachal · ⭐4.7', price: '₹1,200', icon: '🧗' },
      { name: 'Jeep Safari Ranthambore', meta: 'Rajasthan · ⭐4.8', price: '₹3,000', icon: '🚙' }
    ];
    const searchDataIntl = [
      { name: 'Paragliding in Interlaken', meta: 'Switzerland · 2h · ⭐4.9', price: '$180', icon: '🪂' },
      { name: 'Paragliding over Chamonix Alps', meta: 'France · 1.5h · ⭐4.8', price: '$220', icon: '🪂' },
      { name: 'Tandem Paragliding Queenstown', meta: 'New Zealand · 45min · ⭐4.9', price: '$265', icon: '🪂' },
      { name: 'Paragliding Oludeniz Turkey', meta: 'Fethiye · 30min · ⭐4.8', price: '$90', icon: '🪂' },
      { name: 'Sunrise Paragliding Pokhara', meta: 'Nepal · 1h · ⭐4.9', price: '$75', icon: '🪂' },
      { name: 'Paragliding Monte Baldo Lake Garda', meta: 'Italy · 1h · ⭐4.7', price: '$135', icon: '🪂' },
    ];
    
    function renderSearch() {
      const container = document.getElementById('search-results-container');
      const data = currentTripType === 'india' ? searchDataIndia : searchDataIntl;
      container.innerHTML = data.map(item => `
        <div class="search-result">
          <div class="search-result-icon">${item.icon}</div>
          <div class="search-result-info">
            <div class="search-result-name">${item.name}</div>
            <div class="search-result-meta">${item.meta}</div>
          </div>
          <div class="search-result-price">${item.price}</div>
          <button class="btn btn-accent btn-sm" onclick="showToast('Added to Trip')">Add</button>
        </div>
      `).join('');
    }
    
    function runSearch() {
      const q = document.getElementById('search-input').value || 'Adventure';
      const count = currentTripType === 'india' ? searchDataIndia.length : searchDataIntl.length;
      document.getElementById('search-result-label').innerText = `Showing ${count} results for "${q}"`;
      renderSearch();
    }
    
    // Checklist
    function toggleCheck(el) {
      el.classList.toggle('checked');
      const icon = el.querySelector('.check-box i');
      if(el.classList.contains('checked')) icon.className = 'far fa-check-square';
      else icon.className = 'far fa-square';
      updateProgress();
    }
    function updateProgress() {
      // only count visible items based on current mode
      let total = 0;
      let checked = 0;
      document.querySelectorAll('.check-item').forEach(el => {
        // check if element is visible
        if (window.getComputedStyle(el).display !== 'none') {
          total++;
          if(el.classList.contains('checked')) checked++;
        }
      });
      document.getElementById('progress-text').innerText = `${checked} / ${total} items packed`;
      document.getElementById('progress-fill').style.width = (total === 0 ? 0 : checked / total * 100) + '%';
      
      // Update groups
      document.querySelectorAll('.checklist-group').forEach(group => {
        let gt = 0;
        let gc = 0;
        group.querySelectorAll('.check-item').forEach(el => {
          if (window.getComputedStyle(el).display !== 'none') {
            gt++;
            if(el.classList.contains('checked')) gc++;
          }
        });
        group.querySelector('.group-count').innerText = `${gc}/${gt}`;
      });
    }
    function resetChecklist() {
      document.querySelectorAll('.check-item.checked').forEach(el => {
         if (window.getComputedStyle(el).display !== 'none') toggleCheck(el);
      });
      showToast('Checklist reset');
    }
    function addChecklistItem() {
      const name = document.getElementById('new-item-name').value;
      const cat = document.getElementById('new-item-category').value;
      if(!name) return;
      const group = document.querySelector(`.checklist-group[data-group="${cat}"] .checklist-items`);
      if(group) {
        const div = document.createElement('div');
        div.className = 'check-item ' + currentTripType + '-mode trip-mode';
        div.setAttribute('onclick', 'toggleCheck(this)');
        div.innerHTML = `<div class="check-box"><i class="far fa-square"></i></div><span>${name}</span>`;
        group.appendChild(div);
        
        // force display to match current mode
        div.style.display = '';
      }
      closeModal('add-item-modal');
      updateProgress();
      document.getElementById('new-item-name').value = '';
      showToast('Item added');
    }

    // Notes
    function addNote() {
      const title = document.getElementById('note-title').value;
      const content = document.getElementById('note-content').value;
      const day = document.getElementById('note-day').value;
      const city = document.getElementById('note-city').value;
      if(!title || !content) return;
      const html = `
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">${title}</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">${content}</p>
          <div class="note-meta">${day} · ${city}</div>
        </div>`;
      const containerId = currentTripType === 'india' ? 'notes-container' : 'notes-container-intl';
      document.getElementById(containerId).insertAdjacentHTML('afterbegin', html);
      closeModal('add-note-modal');
      document.getElementById('note-title').value = '';
      document.getElementById('note-content').value = '';
      showToast('Note saved!');
    }

    // Itinerary
    function addItinerarySection() {
      const containerId = currentTripType === 'india' ? 'itinerary-sections-container-india' : 'itinerary-sections-container-intl';
      const container = document.getElementById(containerId);
      const count = container.children.length + 1;
      const budget = currentTripType === 'india' ? '₹0' : '$0';
      const html = `
        <div style="position:relative; margin-bottom: 16px;">
          <div style="position:absolute; left:-31px; top:0; width:16px; height:16px; border-radius:50%; background:var(--teal);"></div>
          <div style="font-weight:bold; font-size:1.125rem">Section ${count}: New Section</div>
          <div style="color:var(--text2); font-size:0.875rem; margin-bottom:8px">custom activities</div>
          <div class="badge badge-teal" style="background:rgba(22,199,154,0.1); color:var(--teal)">Budget ${budget}</div>
        </div>
      `;
      container.insertAdjacentHTML('beforeend', html);
      showToast('Section added');
    }

    // Community
    function likePost(btn) {
      const icon = btn.querySelector('i');
      const span = btn.querySelector('span');
      let count = parseInt(span.innerText);
      if(icon.classList.contains('far')) {
        icon.classList.replace('far', 'fas');
        btn.style.color = 'var(--accent)';
        span.innerText = count + 1;
      } else {
        icon.classList.replace('fas', 'far');
        btn.style.color = '';
        span.innerText = count - 1;
      }
    }

    // Admin
    function switchAdminTab(tab, el) {
      document.querySelectorAll('.admin-panel-content').forEach(c => c.style.display = 'none');
      document.getElementById('admin-tab-' + tab).style.display = 'block';
      document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
      el.classList.add('active');
    }

    // Init App
    document.addEventListener('DOMContentLoaded', () => {
      switchTripType(currentTripType);

      // Dynamic Trips Badge
      setTimeout(() => {
        const tripsIndia = document.querySelectorAll('#trips-container-india .trip-card').length;
        const tripsIntl = document.querySelectorAll('#trips-container-intl .trip-card').length;
        let totalTrips = tripsIndia + tripsIntl;
        
        const hasContainers = document.getElementById('trips-container-india') || document.getElementById('trips-container-intl');
        if (hasContainers) {
          localStorage.setItem('totalTripsCount', totalTrips);
        } else {
          totalTrips = parseInt(localStorage.getItem('totalTripsCount')) || 0;
        }

        // Update badge in sidebar
        const badge = document.querySelector('.sidebar .badge-accent');
        if (badge) {
          badge.innerText = totalTrips;
          if (totalTrips === 0) {
            badge.style.display = 'none';
          } else {
            badge.style.display = 'inline-block';
          }
        }
      }, 500);
    });