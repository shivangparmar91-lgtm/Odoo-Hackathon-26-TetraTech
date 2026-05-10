import os

# --- CSS Content ---
css_content = """
:root {
  --primary: #1a1a2e;
  --accent: #e94560;
  --accent2: #f5a623;
  --teal: #16c79a;
  --surface: #ffffff;
  --surface2: #f7f7f9;
  --surface3: #eef0f4;
  --text: #1a1a2e;
  --text2: #5a6072;
  --text3: #9ba3b8;
  --border: #e2e5ed;
  --radius: 14px;
  --shadow: 0 2px 12px rgba(26,26,46,0.08);
  --nav-h: 64px;
  --font-heading: 'Syne', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'DM Mono', monospace;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 100%; height: 100%; overflow-x: hidden; }
body { font-family: var(--font-body); background-color: var(--surface2); color: var(--text); line-height: 1.5; }
a { text-decoration: none; color: inherit; }
ul, ol { list-style: none; }
button, input, select, textarea { font-family: inherit; border: none; outline: none; }
button { cursor: pointer; background: none; }
img { max-width: 100%; display: block; object-fit: cover; }

h1, h2, h3, h4, h5, h6 { font-family: var(--font-heading); font-weight: 700; color: var(--primary); line-height: 1.2; }
h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }
h4 { font-size: 1.25rem; }
p { font-size: 1rem; color: var(--text2); }
.text-mono { font-family: var(--font-mono); }
.text-small { font-size: 0.875rem; }

.topbar { position: fixed; top: 0; left: 0; right: 0; height: var(--nav-h); background-color: var(--primary); display: flex; align-items: center; justify-content: space-between; padding: 0 24px; z-index: 100; }
.topbar-left { display: flex; align-items: center; gap: 8px; color: var(--surface); font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; }
.topbar-left .dot { width: 8px; height: 8px; border-radius: 50%; background-color: var(--accent); }
.topbar-center { flex: 1; max-width: 400px; margin: 0 24px; position: relative; }
.topbar-search { width: 100%; height: 40px; border-radius: 20px; background-color: rgba(255,255,255,0.1); color: var(--surface); padding: 0 16px 0 40px; }
.topbar-search::placeholder { color: var(--text3); }
.topbar-center .fa-search { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: var(--text3); }
.topbar-right { display: flex; align-items: center; gap: 16px; }
.avatar-circle { width: 36px; height: 36px; border-radius: 50%; background-color: var(--accent); color: var(--surface); display: flex; align-items: center; justify-content: center; font-weight: bold; }

.sidebar { position: fixed; top: var(--nav-h); left: 0; bottom: 0; width: 220px; background-color: var(--surface); border-right: 1px solid var(--border); padding: 24px 0; overflow-y: auto; z-index: 90; display: block; }
.sidebar-section { margin-bottom: 24px; }
.sidebar-section-title { padding: 0 24px; font-size: 0.75rem; text-transform: uppercase; color: var(--text3); margin-bottom: 8px; font-weight: bold; }
.sidebar-link { display: flex; align-items: center; padding: 12px 24px; color: var(--text2); transition: all 0.2s; position: relative; gap: 12px; cursor: pointer; }
.sidebar-link:hover { background-color: var(--surface2); }
.sidebar-link.active { background-color: rgba(233, 69, 96, 0.1); color: var(--accent); border-left: 4px solid var(--accent); padding-left: 20px; }
.sidebar-link .badge { margin-left: auto; }

.main { margin-left: 220px; padding: 32px; margin-top: var(--nav-h); min-height: calc(100vh - var(--nav-h)); transition: margin-left 0.3s; }
.mobile-nav { display: none; }

.screen-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; }

.grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.grid-auto { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 24px; }

.btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 10px 20px; border-radius: var(--radius); font-weight: 600; transition: all 0.2s; cursor: pointer; }
.btn-primary { background-color: var(--primary); color: var(--surface); }
.btn-primary:hover { background-color: var(--accent); color: var(--surface); }
.btn-accent { background-color: var(--accent); color: var(--surface); }
.btn-teal { background-color: var(--teal); color: var(--surface); }
.btn-sm { padding: 6px 12px; font-size: 0.875rem; border-radius: 8px; }
.btn-icon { width: 36px; height: 36px; padding: 0; border-radius: 50%; display: flex; align-items: center; justify-content: center; background-color: var(--surface3); color: var(--text2); }
.btn-icon:hover { background-color: var(--accent); color: var(--surface); }

.card { background-color: var(--surface); border-radius: var(--radius); box-shadow: var(--shadow); padding: 24px; }
.card-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
.card-title { font-size: 1.25rem; }

.input { width: 100%; padding: 12px 16px; border: 1px solid var(--border); border-radius: 8px; background-color: var(--surface); color: var(--text); transition: border 0.2s; }
.input:focus { border-color: var(--accent); }
.select { width: 100%; padding: 12px 16px; border: 1px solid var(--border); border-radius: 8px; background-color: var(--surface); color: var(--text); appearance: none; }
.input-group { margin-bottom: 16px; }
.label { display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.875rem; color: var(--text2); }
.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

.badge { padding: 4px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }
.badge-green { background-color: rgba(22, 199, 154, 0.1); color: var(--teal); }
.badge-amber { background-color: rgba(245, 166, 35, 0.1); color: var(--accent2); }
.badge-red { background-color: rgba(233, 69, 96, 0.1); color: var(--accent); }
.badge-blue { background-color: rgba(0, 123, 255, 0.1); color: #007bff; }
.badge-gray { background-color: var(--surface3); color: var(--text2); }
.badge-pink { background-color: rgba(233, 69, 96, 0.1); color: var(--accent); }

.progress-bar { width: 100%; height: 8px; background-color: var(--surface3); border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; background-color: var(--accent); transition: width 0.3s; }
.progress-fill.teal { background-color: var(--teal); }

.chip { display: inline-flex; align-items: center; padding: 6px 12px; border-radius: 20px; background-color: var(--surface3); color: var(--text2); font-size: 0.875rem; cursor: pointer; transition: all 0.2s; margin-right: 8px; margin-bottom: 8px; }
.chip.active { background-color: var(--accent); color: var(--surface); }

.modal-bg { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background-color: rgba(26,26,46,0.8); z-index: 200; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.3s; backdrop-filter: blur(4px); }
.modal-bg.open { opacity: 1; pointer-events: auto; }
.modal { background-color: var(--surface); border-radius: var(--radius); width: 90%; max-width: 500px; padding: 24px; box-shadow: var(--shadow); transform: translateY(20px); transition: transform 0.3s; max-height: 90vh; overflow-y: auto; }
.modal-bg.open .modal { transform: translateY(0); }
.modal-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; }
.modal-title { font-size: 1.25rem; font-family: var(--font-heading); color: var(--primary); }
.modal-close { background: none; border: none; font-size: 1.5rem; color: var(--text3); cursor: pointer; }
.modal-close:hover { color: var(--accent); }

.data-table { width: 100%; border-collapse: collapse; }
.data-table th, .data-table td { padding: 16px; text-align: left; border-bottom: 1px solid var(--border); }
.data-table th { font-weight: 600; color: var(--text2); background-color: var(--surface2); font-size: 0.875rem; }
.data-table tr:hover td { background-color: var(--surface2); }

.trip-type-selector { display:flex; gap:8px; padding: 4px; background: var(--surface2); border-radius: 8px; margin-bottom: 24px; }
.trip-type-btn { flex: 1; border-radius: 6px; padding: 10px; color: var(--text2); font-weight: 500; background: transparent; transition: all 0.2s; border: none; }
.trip-type-btn.active { background: var(--surface); color: var(--primary); box-shadow: 0 2px 4px rgba(0,0,0,0.05); font-weight: bold; }

/* Dashboard elements */
.banner { background: linear-gradient(135deg, var(--primary), var(--accent)); border-radius: var(--radius); padding: 40px; color: var(--surface); margin-bottom: 32px; }
.banner h2 { color: var(--surface); margin-bottom: 8px; }
.banner p { color: rgba(255,255,255,0.8); margin-bottom: 24px; }
.banner-actions { display: flex; gap: 16px; }
.banner-btn { background-color: var(--surface); color: var(--primary); }
.banner-btn:hover { background-color: var(--surface2); }
.banner-btn-outline { border: 1px solid var(--surface); color: var(--surface); }
.banner-btn-outline:hover { background-color: rgba(255,255,255,0.1); }
.dest-card { background-color: var(--surface); border-radius: var(--radius); padding: 16px; text-align: center; box-shadow: var(--shadow); transition: transform 0.2s; cursor: pointer; }
.dest-card:hover { transform: translateY(-5px); }
.dest-thumb { font-size: 3rem; margin-bottom: 12px; }
.dest-label { font-weight: bold; margin-bottom: 4px; }
.dest-sublabel { font-size: 0.875rem; color: var(--text3); }
.trip-card { background-color: var(--surface); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); }
.trip-card-img { height: 140px; background: linear-gradient(135deg, var(--primary), var(--accent2)); }
.trip-card-body { padding: 16px; }
.trip-card-name { font-weight: bold; font-size: 1.125rem; margin-bottom: 8px; }
.trip-card-meta { font-size: 0.875rem; color: var(--text2); margin-bottom: 16px; }
.trip-card-footer { padding: 16px; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; font-weight: bold; }

/* Admin */
.admin-tabs { display: flex; gap: 16px; margin-bottom: 24px; border-bottom: 1px solid var(--border); }
.admin-tab { padding: 12px 24px; font-weight: bold; color: var(--text2); cursor: pointer; border-bottom: 3px solid transparent; }
.admin-tab.active { color: var(--primary); border-bottom-color: var(--primary); }
.stat-card { background-color: var(--surface); padding: 24px; border-radius: var(--radius); box-shadow: var(--shadow); display: flex; align-items: center; gap: 16px; }
.stat-icon { width: 48px; height: 48px; border-radius: 12px; background-color: rgba(233, 69, 96, 0.1); color: var(--accent); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; }
.stat-info { flex: 1; }
.stat-label { font-size: 0.875rem; color: var(--text3); margin-bottom: 4px; }
.stat-value { font-size: 1.5rem; font-weight: bold; color: var(--primary); }
.stat-delta { font-size: 0.875rem; color: var(--teal); font-weight: bold; }

/* Checklist */
.checklist-group { margin-bottom: 24px; }
.checklist-group-header { font-weight: bold; margin-bottom: 12px; display: flex; justify-content: space-between; color: var(--primary); }
.checklist-items { background-color: var(--surface); border-radius: var(--radius); box-shadow: var(--shadow); overflow: hidden; }
.check-item { display: flex; align-items: center; padding: 16px; border-bottom: 1px solid var(--border); cursor: pointer; transition: background-color 0.2s; }
.check-item:last-child { border-bottom: none; }
.check-item:hover { background-color: var(--surface2); }
.check-box { color: var(--text3); margin-right: 12px; font-size: 1.25rem; }
.check-item.checked { color: var(--text3); text-decoration: line-through; }
.check-item.checked .check-box { color: var(--teal); }

/* Toasts */
.toast-container { position: fixed; bottom: 24px; right: 24px; z-index: 9999; display: flex; flex-direction: column; gap: 12px; pointer-events: none; }
.toast { background-color: var(--primary); color: var(--surface); padding: 12px 24px; border-radius: 8px; box-shadow: var(--shadow); display: flex; align-items: center; gap: 12px; opacity: 0; transform: translateY(20px); transition: all 0.3s; }
.toast.show { opacity: 1; transform: translateY(0); }

/* Dynamic Mode Classes */
.trip-mode { display: block; } /* By default they show, JS hides the non-active ones */

@media (max-width: 900px) {
  .sidebar { display: none !important; }
  .main { margin-left: 0; padding: 16px; margin-bottom: 60px; }
  .mobile-nav { display: flex; position: fixed; bottom: 0; left: 0; right: 0; height: 60px; background-color: var(--surface); box-shadow: 0 -2px 10px rgba(0,0,0,0.05); z-index: 100; justify-content: space-around; align-items: center; border-top: 1px solid var(--border); }
  .mobile-nav a { display: flex; flex-direction: column; align-items: center; color: var(--text3); font-size: 0.75rem; gap: 4px; cursor: pointer; }
  .mobile-nav a.active { color: var(--accent); }
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
}
"""

# --- JS Content ---
js_content = """
document.addEventListener('DOMContentLoaded', () => {
    let currentTripType = localStorage.getItem('tripType') || 'india';
    
    // Auto-apply on load
    switchTripType(currentTripType);
    updateProgress();
});

function switchTripType(type) {
    currentTripType = type;
    localStorage.setItem('tripType', type);
    
    // Only display content matching current mode
    document.querySelectorAll('.trip-mode').forEach(el => {
        el.style.display = 'none';
    });
    document.querySelectorAll('.' + type + '-mode').forEach(el => {
        el.style.display = ''; // revert to CSS default
    });
    
    // Update currency
    document.querySelectorAll('.currency-symbol').forEach(el => {
        el.innerText = type === 'india' ? '₹' : '$';
    });
    
    // Update active button state
    document.querySelectorAll('.trip-type-btn').forEach(btn => {
        btn.classList.remove('active');
        if(btn.dataset.type === type) btn.classList.add('active');
    });

    if(window.runSearch) runSearch();
    if(window.updateProgress) updateProgress();
}

function showModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }
document.addEventListener('click', e => { if (e.target.classList.contains('modal-bg')) e.target.classList.remove('open'); });

function showToast(message) {
    const container = document.getElementById('toast-container');
    if (!container) return;
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

// Checklist logic
function toggleCheck(el) {
    el.classList.toggle('checked');
    const icon = el.querySelector('.check-box i');
    if(el.classList.contains('checked')) icon.className = 'far fa-check-square';
    else icon.className = 'far fa-square';
    updateProgress();
}
function updateProgress() {
    const progressText = document.getElementById('progress-text');
    if(!progressText) return;
    
    let total = 0;
    let checked = 0;
    document.querySelectorAll('.check-item').forEach(el => {
        if (window.getComputedStyle(el).display !== 'none') {
            total++;
            if(el.classList.contains('checked')) checked++;
        }
    });
    progressText.innerText = `${checked} / ${total} items packed`;
    const fill = document.getElementById('progress-fill');
    if(fill) fill.style.width = (total === 0 ? 0 : checked / total * 100) + '%';
    
    document.querySelectorAll('.checklist-group').forEach(group => {
        let gt = 0, gc = 0;
        group.querySelectorAll('.check-item').forEach(el => {
            if (window.getComputedStyle(el).display !== 'none') {
                gt++;
                if(el.classList.contains('checked')) gc++;
            }
        });
        const cnt = group.querySelector('.group-count');
        if(cnt) cnt.innerText = `${gc}/${gt}`;
    });
}
function resetChecklist() {
    document.querySelectorAll('.check-item.checked').forEach(el => {
        if (window.getComputedStyle(el).display !== 'none') toggleCheck(el);
    });
    showToast('Checklist reset');
}

// Note Logic
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

// Like functionality
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

// Admin Tab Logic
function switchAdminTab(tab, el) {
    document.querySelectorAll('.admin-panel-content').forEach(c => c.style.display = 'none');
    document.getElementById('admin-tab-' + tab).style.display = 'block';
    document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
}
"""

import os

# Create directories
os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)
os.makedirs('pages', exist_ok=True)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# HTML Layouts
def get_head(title, is_root=False):
    prefix = "" if is_root else "../"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Traveloop - {title}</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
  <div class="toast-container" id="toast-container"></div>
'''

def get_navigation(active_page, is_root=False):
    prefix = "pages/" if is_root else ""
    return f'''
  <div class="topbar" style="display:flex;">
    <div class="topbar-left">Traveloop <div class="dot"></div></div>
    <div class="topbar-center">
      <i class="fas fa-search"></i>
      <input type="text" class="topbar-search" placeholder="Search trips, activities, cities...">
    </div>
    <div class="topbar-right">
      <button class="btn btn-primary btn-sm" onclick="showModal('plan-trip-modal')">Plan a Trip</button>
      <div class="avatar-circle">JA</div>
    </div>
  </div>

  <div class="sidebar" style="display:block;">
    <div class="sidebar-section">
      <div class="sidebar-section-title">Main</div>
      <a class="sidebar-link {'active' if active_page=='dashboard' else ''}" href="{prefix}dashboard.html"><i class="fas fa-home"></i> Home</a>
      <a class="sidebar-link {'active' if active_page=='trips' else ''}" href="{prefix}trips.html"><i class="fas fa-map-marked-alt"></i> My Trips</a>
      <a class="sidebar-link {'active' if active_page=='create' else ''}" href="{prefix}create-trip.html"><i class="fas fa-plus-circle"></i> Plan a Trip</a>
      <a class="sidebar-link {'active' if active_page=='itinerary' else ''}" href="{prefix}itinerary.html"><i class="fas fa-calendar-alt"></i> Itinerary</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Tools</div>
      <a class="sidebar-link {'active' if active_page=='search' else ''}" href="{prefix}search.html"><i class="fas fa-search"></i> Activity Search</a>
      <a class="sidebar-link {'active' if active_page=='checklist' else ''}" href="{prefix}checklist.html"><i class="fas fa-check-square"></i> Packing List</a>
      <a class="sidebar-link {'active' if active_page=='notes' else ''}" href="{prefix}notes.html"><i class="fas fa-sticky-note"></i> Trip Notes</a>
      <a class="sidebar-link {'active' if active_page=='budget' else ''}" href="{prefix}budget.html"><i class="fas fa-file-invoice-dollar"></i> Expenses</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Discover</div>
      <a class="sidebar-link {'active' if active_page=='community' else ''}" href="{prefix}community.html"><i class="fas fa-users"></i> Community</a>
      <a class="sidebar-link {'active' if active_page=='profile' else ''}" href="{prefix}profile.html"><i class="fas fa-user-circle"></i> Profile</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Admin</div>
      <a class="sidebar-link {'active' if active_page=='admin' else ''}" href="{prefix}admin.html"><i class="fas fa-cog"></i> Admin Panel</a>
    </div>
  </div>
'''

def get_modals():
    return '''
  <div class="modal-bg" id="plan-trip-modal">
    <div class="modal">
      <div class="modal-header"><h2 class="modal-title">Plan a New Trip</h2><button class="modal-close" onclick="closeModal('plan-trip-modal')">&times;</button></div>
      <div class="input-group">
        <label class="label">Trip Type</label>
        <div class="trip-type-selector" style="margin-bottom:0">
          <button class="btn trip-type-btn active" data-type="india" onclick="switchTripType('india')" type="button">India Trip</button>
          <button class="btn trip-type-btn" data-type="intl" onclick="switchTripType('intl')" type="button">International Trip</button>
        </div>
      </div>
      <div class="input-group"><label class="label">Trip Name</label><input type="text" class="input" placeholder="e.g. Summer Vacation"></div>
      <div class="form-grid">
        <div class="input-group"><label class="label">Start Date</label><input type="date" class="input"></div>
        <div class="input-group"><label class="label">End Date</label><input type="date" class="input"></div>
      </div>
      <div class="input-group"><label class="label">Destination</label><input type="text" class="input" placeholder="e.g. Jaipur, Rajasthan"></div>
      <div class="input-group"><label class="label">Budget (<span class="currency-symbol">₹</span>)</label><input type="number" class="input" placeholder="e.g. 15000"></div>
      <div style="display:flex;gap:16px;margin-top:24px;">
        <button class="btn btn-primary" style="flex:1" onclick="window.location.href='itinerary.html'">Continue</button>
        <button class="btn" style="flex:1;border:1px solid var(--border)" onclick="closeModal('plan-trip-modal')">Cancel</button>
      </div>
    </div>
  </div>
'''

def get_footer(is_root=False):
    prefix = "" if is_root else "../"
    return f'''
  <script src="{prefix}js/main.js"></script>
</body>
</html>
'''

# 1. Login Page (index.html)
login_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Traveloop - Login</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body {{ background: linear-gradient(135deg, rgba(26,26,46,0.9), rgba(233,69,96,0.9)), url('https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=1920&q=80') center/cover; display: flex; align-items: center; justify-content: center; min-height: 100vh; flex-direction: column; padding: 24px; }}
    body.intl-bg {{ background: linear-gradient(135deg, rgba(26,26,46,0.9), rgba(233,69,96,0.9)), url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=1920&q=80') center/cover; }}
    .auth-card {{ width: 100%; max-width: 400px; }}
    .auth-logo {{ text-align: center; font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--primary); margin-bottom: 24px; display: flex; justify-content: center; align-items: center; gap: 8px; }}
    .auth-logo .dot {{ width: 10px; height: 10px; border-radius: 50%; background-color: var(--accent); }}
  </style>
</head>
<body>
  <div class="toast-container" id="toast-container"></div>
  <div style="text-align:center; color:white; margin-bottom:24px;">
    <h2 style="color:white; margin-bottom:8px;">Where do you want to explore?</h2>
    <div class="trip-type-selector" style="display:inline-flex; width: 100%; max-width: 400px; background:rgba(255,255,255,0.2); backdrop-filter:blur(10px);">
      <button class="btn trip-type-btn active" data-type="india" onclick="switchTripType('india')">India Trip</button>
      <button class="btn trip-type-btn" data-type="intl" onclick="switchTripType('intl')">International Trip</button>
    </div>
  </div>
  <div class="card auth-card">
    <div class="auth-logo">Traveloop <div class="dot"></div></div>
    <form onsubmit="event.preventDefault(); window.location.href='pages/dashboard.html';">
      <div class="input-group">
        <label class="label">Email Address</label>
        <input type="email" class="input" placeholder="name@example.com" required>
      </div>
      <div class="input-group">
        <label class="label">Password</label>
        <input type="password" class="input" placeholder="••••••••" required>
      </div>
      <button type="submit" class="btn btn-primary" style="width: 100%">Login to Dashboard</button>
    </form>
  </div>
  <script src="js/main.js"></script>
  <script>
    function switchTripType(type) {{
      localStorage.setItem('tripType', type);
      document.querySelectorAll('.trip-type-btn').forEach(b => b.classList.remove('active'));
      document.querySelector(`[data-type="${{type}}"]`).classList.add('active');
      if(type === 'intl') document.body.classList.add('intl-bg');
      else document.body.classList.remove('intl-bg');
    }}
    switchTripType(localStorage.getItem('tripType') || 'india');
  </script>
</body>
</html>
'''
with open('index.html', 'w', encoding='utf-8') as f: f.write(login_html)

# Dashboard
dash_html = get_head("Dashboard") + get_navigation("dashboard") + '''
  <div class="main">
    <div class="banner">
      <h2>Plan your next unforgettable journey</h2>
      <p class="trip-mode india-mode">From royal palaces to Himalayan adventures.</p>
      <p class="trip-mode intl-mode" style="display:none;">Explore beautiful destinations across the globe.</p>
      <div class="banner-actions">
        <button class="btn banner-btn" onclick="showModal('plan-trip-modal')">Plan a Trip</button>
        <a class="btn banner-btn-outline" href="community.html">Explore Community</a>
      </div>
    </div>
    <div class="screen-header"><h3 class="card-title">Top Regional Selections</h3></div>
    <div class="grid-auto trip-mode india-mode" style="margin-bottom: 40px;">
      <div class="dest-card"><div class="dest-thumb">🏰</div><div class="dest-label">Jaipur</div><div class="dest-sublabel">Royal Heritage · ⭐4.8</div></div>
      <div class="dest-card"><div class="dest-thumb">🏖️</div><div class="dest-label">Goa</div><div class="dest-sublabel">Beaches & Nightlife · ⭐4.7</div></div>
      <div class="dest-card"><div class="dest-thumb">⛰️</div><div class="dest-label">Kashmir</div><div class="dest-sublabel">Heaven on Earth · ⭐4.9</div></div>
      <div class="dest-card"><div class="dest-thumb">🛶</div><div class="dest-label">Kerala</div><div class="dest-sublabel">Backwaters Escape · ⭐4.8</div></div>
      <div class="dest-card"><div class="dest-thumb">🏍️</div><div class="dest-label">Leh Ladakh</div><div class="dest-sublabel">Adventure Route · ⭐4.9</div></div>
      <div class="dest-card"><div class="dest-thumb">🌅</div><div class="dest-label">Udaipur</div><div class="dest-sublabel">Lakes & Palaces · ⭐4.7</div></div>
    </div>
    <div class="grid-auto trip-mode intl-mode" style="margin-bottom: 40px; display:none;">
      <div class="dest-card"><div class="dest-thumb">🗼</div><div class="dest-label">Paris</div><div class="dest-sublabel">★4.8 · France</div></div>
      <div class="dest-card"><div class="dest-thumb">🏟️</div><div class="dest-label">Rome</div><div class="dest-sublabel">★4.9 · Italy</div></div>
      <div class="dest-card"><div class="dest-thumb">🗽</div><div class="dest-label">New York</div><div class="dest-sublabel">★4.7 · USA</div></div>
    </div>
    <h3 class="card-title" style="margin-bottom: 16px;">Previous Trips</h3>
    <div class="grid-3 trip-mode india-mode">
      <div class="trip-card">
        <div class="trip-card-img" style="background: linear-gradient(135deg, var(--primary), var(--accent2));"></div>
        <div class="trip-card-body">
          <div class="trip-card-name">Rajasthan Heritage Trail</div>
          <div class="trip-card-meta">Jun 2025 · <span class="badge badge-gray">Completed</span></div>
        </div>
        <div class="trip-card-footer"><span style="color:var(--text2)">Total Cost</span><span style="color:var(--primary)">₹42,000</span></div>
      </div>
      <div class="trip-card">
        <div class="trip-card-img" style="background: linear-gradient(135deg, var(--teal), var(--primary));"></div>
        <div class="trip-card-body">
          <div class="trip-card-name">Goa Escape</div>
          <div class="trip-card-meta">May 2026 · <span class="badge badge-green">Ongoing</span></div>
        </div>
        <div class="trip-card-footer"><span style="color:var(--text2)">Current Cost</span><span style="color:var(--primary)">₹18,400</span></div>
      </div>
    </div>
    <div class="grid-3 trip-mode intl-mode" style="display:none;">
      <div class="trip-card">
        <div class="trip-card-img" style="background: linear-gradient(135deg, var(--primary), var(--accent2));"></div>
        <div class="trip-card-body">
          <div class="trip-card-name">Paris & Rome Adventure</div>
          <div class="trip-card-meta">Jun 2025 · <span class="badge badge-gray">Completed</span></div>
        </div>
        <div class="trip-card-footer"><span style="color:var(--text2)">Total Cost</span><span style="color:var(--primary)">$22,000</span></div>
      </div>
    </div>
  </div>
''' + get_modals() + get_footer()
with open('pages/dashboard.html', 'w', encoding='utf-8') as f: f.write(dash_html)

# Trips
trips_html = get_head("My Trips") + get_navigation("trips") + '''
  <div class="main">
    <div class="screen-header">
      <h1>My Trips</h1>
      <button class="btn btn-primary" onclick="showModal('plan-trip-modal')"><i class="fas fa-plus"></i> New Trip</button>
    </div>
    <div class="trip-mode india-mode">
      <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-green">Ongoing</span><h3 style="margin:0">Goa Escape</h3></div>
      <div class="card" style="margin-bottom:32px">
        <div class="card-header">
          <div><div style="font-weight:bold; margin-bottom:4px">May 1-8 2026</div><div style="color:var(--text2)">Day 4 of 8</div></div>
          <a class="btn btn-teal btn-sm" href="itinerary.html">View Details</a>
        </div>
        <div class="progress-bar"><div class="progress-fill teal" style="width: 60%"></div></div>
      </div>
    </div>
    <div class="trip-mode intl-mode" style="display:none;">
      <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-green">Ongoing</span><h3 style="margin:0">Tokyo Highlights</h3></div>
      <div class="card" style="margin-bottom:32px">
        <div class="card-header">
          <div><div style="font-weight:bold; margin-bottom:4px">May 1-8 2026</div><div style="color:var(--text2)">Day 4 of 8</div></div>
          <a class="btn btn-teal btn-sm" href="itinerary.html">View Details</a>
        </div>
        <div class="progress-bar"><div class="progress-fill teal" style="width: 60%"></div></div>
      </div>
    </div>
  </div>
''' + get_modals() + get_footer()
with open('pages/trips.html', 'w', encoding='utf-8') as f: f.write(trips_html)

# Plan
plan_html = get_head("Plan a Trip") + get_navigation("create") + '''
  <div class="main">
    <div class="screen-header"><h1>Create Trip</h1></div>
    <div class="grid-2">
      <div class="card">
        <h3 class="card-title" style="margin-bottom: 24px;">Trip Details</h3>
        <div class="input-group">
          <label class="label">Trip Type</label>
          <div class="trip-type-selector" style="margin-bottom:0">
            <button class="btn trip-type-btn active" data-type="india" onclick="switchTripType('india')">India Trip</button>
            <button class="btn trip-type-btn" data-type="intl" onclick="switchTripType('intl')">International Trip</button>
          </div>
        </div>
        <div class="input-group"><label class="label">Trip Name</label><input type="text" class="input" placeholder="e.g. Summer Vacation"></div>
        <div class="input-group"><label class="label">Total Budget (<span class="currency-symbol">₹</span>)</label><input type="number" class="input" value="5000"></div>
        <div style="display:flex; gap:16px; margin-top:24px;">
          <a class="btn btn-primary" style="flex:1" href="itinerary.html">Build Itinerary</a>
          <a class="btn" style="flex:1; border:1px solid var(--border)" href="dashboard.html">Cancel</a>
        </div>
      </div>
      <div>
        <div class="card" style="margin-bottom: 24px;">
          <h3 class="card-title" style="margin-bottom: 16px;">Suggested Places to Visit</h3>
          <div class="grid-3 trip-mode india-mode">
            <div class="dest-card"><div class="dest-thumb">🕌</div><div class="dest-label">Taj Mahal</div></div>
            <div class="dest-card"><div class="dest-thumb">🏯</div><div class="dest-label">Hawa Mahal</div></div>
            <div class="dest-card"><div class="dest-thumb">🛕</div><div class="dest-label">Golden Temple</div></div>
          </div>
          <div class="grid-3 trip-mode intl-mode" style="display:none;">
            <div class="dest-card"><div class="dest-thumb">🗼</div><div class="dest-label">Eiffel Tower</div></div>
            <div class="dest-card"><div class="dest-thumb">🏟️</div><div class="dest-label">Colosseum</div></div>
            <div class="dest-card"><div class="dest-thumb">🖼️</div><div class="dest-label">Louvre</div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
''' + get_modals() + get_footer()
with open('pages/create-trip.html', 'w', encoding='utf-8') as f: f.write(plan_html)

# Keep creating other pages briefly but accurately
iti_html = get_head("Itinerary") + get_navigation("itinerary") + '''
  <div class="main">
    <div class="screen-header" style="margin-bottom:8px">
      <h1>Itinerary</h1>
      <a class="btn btn-accent btn-sm" href="budget.html">View Budget</a>
    </div>
    <div class="grid-2 trip-mode india-mode">
      <div class="card">
        <h3 class="card-title" style="margin-bottom: 24px;">Day-by-Day View</h3>
        <div class="day-block">
          <div class="day-label">Day 1 Dec 15</div>
          <div class="itinerary-item"><div class="itinerary-time">09:00</div><div class="itinerary-content"><h4>Flight AMD→JAI</h4></div><div class="itinerary-budget">₹3,500</div></div>
        </div>
      </div>
    </div>
    <div class="grid-2 trip-mode intl-mode" style="display:none;">
      <div class="card">
        <h3 class="card-title" style="margin-bottom: 24px;">Day-by-Day View</h3>
        <div class="day-block">
          <div class="day-label">Day 1 Jun 15</div>
          <div class="itinerary-item"><div class="itinerary-time">09:00</div><div class="itinerary-content"><h4>Flight DEL→PAR</h4></div><div class="itinerary-budget">$3,000</div></div>
        </div>
      </div>
    </div>
  </div>
''' + get_modals() + get_footer()
with open('pages/itinerary.html', 'w', encoding='utf-8') as f: f.write(iti_html)

search_html = get_head("Search") + get_navigation("search") + '''
  <div class="main">
    <div class="screen-header"><h1>Activity Search</h1></div>
    <div class="card" style="margin-bottom: 24px;">
      <div style="display:flex; gap:16px; margin-bottom:24px;">
        <input type="text" class="input" placeholder="Search for activities..." style="flex:1" id="search-input" value="Adventure">
        <button class="btn btn-primary" onclick="runSearch()">Search</button>
      </div>
    </div>
    <div id="search-results-container"></div>
  </div>
  <script>
    const searchDataIndia = [{ name: 'Paragliding Bir Billing', meta: 'Himachal · 2h · ⭐4.8', price: '₹3,500', icon: '🪂' }, { name: 'River Rafting Rishikesh', meta: 'Uttarakhand · 3h · ⭐4.9', price: '₹2,200', icon: '🚣' }];
    const searchDataIntl = [{ name: 'Paragliding in Interlaken', meta: 'Switzerland · 2h · ⭐4.9', price: '$180', icon: '🪂' }];
    function runSearch() {
      const data = localStorage.getItem('tripType') === 'intl' ? searchDataIntl : searchDataIndia;
      document.getElementById('search-results-container').innerHTML = data.map(item => `
        <div class="card" style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">
          <div style="font-size: 2rem;">${item.icon}</div>
          <div style="flex:1"><h4>${item.name}</h4><p class="text-small">${item.meta}</p></div>
          <div style="font-weight:bold; color:var(--teal); font-size:1.25rem;">${item.price}</div>
        </div>
      `).join('');
    }
    document.addEventListener('DOMContentLoaded', runSearch);
  </script>
''' + get_modals() + get_footer()
with open('pages/search.html', 'w', encoding='utf-8') as f: f.write(search_html)

# Add minimal forms for others, since the user said "Ensure every page content container is visible by default".
# I'll just write them dynamically.
chk_html = get_head("Checklist") + get_navigation("checklist") + '''
  <div class="main">
    <div class="screen-header"><h1>Packing Checklist</h1></div>
    <div class="grid-2">
      <div class="card">
        <div class="checklist-group">
          <div class="checklist-items">
            <div class="check-item checked" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-check-square"></i></div><span>Passport</span></div>
            <div class="check-item trip-mode india-mode" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Aadhaar Card</span></div>
            <div class="check-item trip-mode intl-mode" style="display:none;" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Visa</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
''' + get_modals() + get_footer()
with open('pages/checklist.html', 'w', encoding='utf-8') as f: f.write(chk_html)

notes_html = get_head("Notes") + get_navigation("notes") + '''
  <div class="main">
    <div class="screen-header"><h1>Trip Notes</h1></div>
    <div id="notes-container" class="trip-mode india-mode">
      <div class="card"><h3 class="card-title">Jaipur Hotel Details</h3><p>Check in after 2pm.</p></div>
    </div>
    <div id="notes-container-intl" class="trip-mode intl-mode" style="display:none;">
      <div class="card"><h3 class="card-title">Rome Hotel Details</h3><p>Check in after 2pm.</p></div>
    </div>
  </div>
''' + get_modals() + get_footer()
with open('pages/notes.html', 'w', encoding='utf-8') as f: f.write(notes_html)

budget_html = get_head("Budget") + get_navigation("budget") + '''
  <div class="main">
    <div class="screen-header"><h1>Expenses</h1></div>
    <div class="trip-mode india-mode"><div class="card"><h3>Total Spent: ₹43,500</h3></div></div>
    <div class="trip-mode intl-mode" style="display:none;"><div class="card"><h3>Total Spent: $22,000</h3></div></div>
  </div>
''' + get_modals() + get_footer()
with open('pages/budget.html', 'w', encoding='utf-8') as f: f.write(budget_html)

comm_html = get_head("Community") + get_navigation("community") + '''
  <div class="main">
    <div class="screen-header"><h1>Community</h1></div>
    <div class="grid-2 trip-mode india-mode"><div class="card"><h4>Rann of Kutch</h4><p>Amazing sunset!</p></div></div>
    <div class="grid-2 trip-mode intl-mode" style="display:none;"><div class="card"><h4>Interlaken</h4><p>Amazing paragliding!</p></div></div>
  </div>
''' + get_modals() + get_footer()
with open('pages/community.html', 'w', encoding='utf-8') as f: f.write(comm_html)

prof_html = get_head("Profile") + get_navigation("profile") + '''
  <div class="main">
    <div class="screen-header"><h1>Profile</h1></div>
    <div class="card"><h3 class="card-title">James Arjun</h3><p>Mumbai, India</p></div>
  </div>
''' + get_modals() + get_footer()
with open('pages/profile.html', 'w', encoding='utf-8') as f: f.write(prof_html)

admin_html = get_head("Admin") + get_navigation("admin") + '''
  <div class="main">
    <div class="screen-header"><h1>Admin Panel</h1></div>
    <div class="card"><h3>Total Users: 12,840</h3></div>
  </div>
''' + get_modals() + get_footer()
with open('pages/admin.html', 'w', encoding='utf-8') as f: f.write(admin_html)

print("Multi-page project successfully generated.")
