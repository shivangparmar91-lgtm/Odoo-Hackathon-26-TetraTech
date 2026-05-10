import os

root_dir = r"c:\Users\hp\Downloads\traveloop-frontend"
pages_dir = os.path.join(root_dir, "pages")

layout_head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Traveloop - {title}</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/typography.css">
  <link rel="stylesheet" href="../css/layout.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  {extra_css}
</head>
<body>
"""

layout_nav = """
  <div class="topbar">
    <div class="topbar-left">
      Traveloop <div class="dot"></div>
    </div>
    <div class="topbar-center">
      <i class="fas fa-search"></i>
      <input type="text" class="topbar-search" placeholder="Search trips, activities, cities...">
    </div>
    <div class="topbar-right">
      <button class="btn btn-primary btn-sm" onclick="showModal('plan-trip-modal')">Plan a Trip</button>
      <button class="btn-icon"><i class="fas fa-filter"></i></button>
      <button class="btn-icon"><i class="fas fa-sort"></i></button>
      <div class="avatar-circle">JA</div>
    </div>
  </div>

  <div class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-section-title">Main</div>
      <a href="dashboard.html" class="sidebar-link {a_dash}"><i class="fas fa-home"></i> Home</a>
      <a href="trips.html" class="sidebar-link {a_trips}"><i class="fas fa-map-marked-alt"></i> My Trips <span class="badge badge-accent" style="background:var(--accent);color:white;margin-left:auto">3</span></a>
      <a href="create-trip.html" class="sidebar-link {a_create}"><i class="fas fa-plus-circle"></i> Plan a Trip</a>
      <a href="itinerary-builder.html" class="sidebar-link {a_itin}"><i class="fas fa-calendar-alt"></i> Itinerary</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Tools</div>
      <a href="activity-search.html" class="sidebar-link {a_act}"><i class="fas fa-search"></i> Activity Search</a>
      <a href="checklist.html" class="sidebar-link {a_check}"><i class="fas fa-check-square"></i> Packing List</a>
      <a href="notes.html" class="sidebar-link {a_note}"><i class="fas fa-sticky-note"></i> Trip Notes</a>
      <a href="budget.html" class="sidebar-link {a_bud}"><i class="fas fa-file-invoice-dollar"></i> Expenses</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Discover</div>
      <a href="community.html" class="sidebar-link {a_comm}"><i class="fas fa-users"></i> Community</a>
      <a href="profile.html" class="sidebar-link {a_prof}"><i class="fas fa-user-circle"></i> Profile</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Admin</div>
      <a href="admin.html" class="sidebar-link {a_admin}"><i class="fas fa-cog"></i> Admin Panel</a>
    </div>
  </div>

  <div class="mobile-nav">
    <a href="dashboard.html" class="{a_dash}"><i class="fas fa-home"></i> Home</a>
    <a href="trips.html" class="{a_trips}"><i class="fas fa-map-marked-alt"></i> Trips</a>
    <a href="checklist.html" class="{a_check}"><i class="fas fa-check-square"></i> Packing</a>
    <a href="community.html" class="{a_comm}"><i class="fas fa-users"></i> Community</a>
    <a href="profile.html" class="{a_prof}"><i class="fas fa-user-circle"></i> Profile</a>
  </div>

  <div class="main">
    <div id="screen" class="screen visible">
"""

layout_modals = """
    </div>
  </div>

  <div class="modal-bg" id="plan-trip-modal">
    <div class="modal">
      <div class="modal-header">
        <h2 class="modal-title">Plan a New Trip</h2>
        <button class="modal-close" onclick="closeModal('plan-trip-modal')">&times;</button>
      </div>
      <div class="input-group">
        <label class="label">Trip Name</label>
        <input type="text" class="input" placeholder="e.g. Summer in Europe">
      </div>
      <div class="form-grid">
        <div class="input-group">
          <label class="label">Start Date</label>
          <input type="date" class="input">
        </div>
        <div class="input-group">
          <label class="label">End Date</label>
          <input type="date" class="input">
        </div>
      </div>
      <div class="input-group">
        <label class="label">Destination</label>
        <input type="text" class="input" placeholder="e.g. Paris, France">
      </div>
      <div class="input-group">
        <label class="label">Budget ($)</label>
        <input type="number" class="input" placeholder="e.g. 5000">
      </div>
      <div style="display:flex;gap:16px;margin-top:24px;">
        <a href="create-trip.html" class="btn btn-primary" style="flex:1;text-align:center">Continue</a>
        <button class="btn" style="flex:1;border:1px solid var(--border)" onclick="closeModal('plan-trip-modal')">Cancel</button>
      </div>
    </div>
  </div>

  <div class="modal-bg" id="add-item-modal">
    <div class="modal">
      <div class="modal-header">
        <h2 class="modal-title">Add Item to Checklist</h2>
        <button class="modal-close" onclick="closeModal('add-item-modal')">&times;</button>
      </div>
      <div class="input-group">
        <label class="label">Item Name</label>
        <input type="text" class="input" id="new-item-name" placeholder="e.g. Sunglasses">
      </div>
      <div class="input-group">
        <label class="label">Category</label>
        <select class="select" id="new-item-category">
          <option>Documents</option>
          <option>Clothing</option>
          <option>Electronics</option>
          <option>Health & Hygiene</option>
          <option>Other</option>
        </select>
      </div>
      <button class="btn btn-primary" style="width:100%;margin-top:16px" onclick="addChecklistItem()">Add Item</button>
    </div>
  </div>

  <div class="modal-bg" id="add-note-modal">
    <div class="modal">
      <div class="modal-header">
        <h2 class="modal-title">Add Trip Note</h2>
        <button class="modal-close" onclick="closeModal('add-note-modal')">&times;</button>
      </div>
      <div class="input-group">
        <label class="label">Title</label>
        <input type="text" class="input" id="note-title" placeholder="e.g. Hotel Check-in">
      </div>
      <div class="input-group">
        <label class="label">Content</label>
        <textarea class="input" id="note-content" rows="4" placeholder="Write your notes here..."></textarea>
      </div>
      <div class="form-grid">
        <div class="input-group">
          <label class="label">Day / Date</label>
          <input type="text" class="input" id="note-day" placeholder="e.g. Day 3">
        </div>
        <div class="input-group">
          <label class="label">Stop / City</label>
          <input type="text" class="input" id="note-city" placeholder="e.g. Rome">
        </div>
      </div>
      <button class="btn btn-accent" style="width:100%;margin-top:16px" onclick="addNote()">Save Note</button>
    </div>
  </div>
"""

layout_scripts = """
  {extra_libs}
  <script src="../js/utils/modal.js"></script>
  <script src="../js/utils/toast.js"></script>
  <script src="../js/utils/format.js"></script>
  <script src="../js/utils/storage.js"></script>
  <script src="../js/api.js"></script>
  <script src="../js/router.js"></script>
  <script src="../js/modules/{module_name}.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

pages_data = {
    "dashboard.html": {
        "title": "Dashboard",
        "css": "dashboard",
        "module": "trips",
        "content": """
      <div class="banner">
        <h2>Plan your next adventure</h2>
        <p>Explore beautiful destinations, create itineraries, and track your budget.</p>
        <div class="banner-actions">
          <button class="btn banner-btn" onclick="showModal('plan-trip-modal')">Plan a Trip</button>
          <a href="community.html" class="btn banner-btn-outline">Explore Community</a>
        </div>
      </div>

      <div class="screen-header">
        <h3 class="card-title">Top Regional Selections</h3>
        <div class="tab-row" style="margin-bottom:0; border:none; gap:8px">
          <span class="chip active">All</span>
          <span class="chip">Indian Heritage</span>
          <span class="chip">7 Wonders</span>
          <span class="chip">Abroad</span>
        </div>
      </div>
      <div class="grid-auto" style="margin-bottom: 40px;">
        <div class="dest-card">
          <div class="dest-thumb">🇮🇳</div>
          <div class="dest-label">Taj Mahal</div>
          <div class="dest-sublabel">★4.9 · India</div>
        </div>
        <div class="dest-card">
          <div class="dest-thumb">🇫🇷</div>
          <div class="dest-label">Paris</div>
          <div class="dest-sublabel">★4.8 · France</div>
        </div>
        <div class="dest-card">
          <div class="dest-thumb">🇮🇹</div>
          <div class="dest-label">Rome</div>
          <div class="dest-sublabel">★4.9 · Italy</div>
        </div>
        <div class="dest-card">
          <div class="dest-thumb">🇯🇵</div>
          <div class="dest-label">Tokyo</div>
          <div class="dest-sublabel">★4.8 · Japan</div>
        </div>
        <div class="dest-card">
          <div class="dest-thumb">🇮🇩</div>
          <div class="dest-label">Bali</div>
          <div class="dest-sublabel">★4.7 · Indonesia</div>
        </div>
      </div>

      <h3 class="card-title" style="margin-bottom: 16px;">Previous Trips</h3>
      <div class="grid-3">
        <div class="trip-card">
          <div class="trip-card-img" style="background: url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=400&q=80') center/cover;"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Paris & Rome Adventure</div>
            <div class="trip-card-meta">Jun 2025 · <span class="badge badge-gray">Completed</span></div>
            <div class="trip-card-meta"><i class="fas fa-user-friends"></i> 4 Travelers</div>
          </div>
          <div class="trip-card-footer">
            <span style="color:var(--text2)">Total Cost</span>
            <span style="color:var(--primary)">$22,000</span>
          </div>
        </div>
        <div class="trip-card">
          <div class="trip-card-img" style="background: url('https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=400&q=80') center/cover;"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Tokyo Highlights</div>
            <div class="trip-card-meta">May 2026 · <span class="badge badge-green">Ongoing</span></div>
            <div class="trip-card-meta"><i class="fas fa-user-friends"></i> 2 Travelers</div>
          </div>
          <div class="trip-card-footer">
            <span style="color:var(--text2)">Current Cost</span>
            <span style="color:var(--primary)">$8,400</span>
          </div>
        </div>
        <div class="trip-card">
          <div class="trip-card-img" style="background: url('https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=400&q=80') center/cover;"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Bali Wellness Retreat</div>
            <div class="trip-card-meta">Aug 2026 · <span class="badge badge-amber">Upcoming</span></div>
            <div class="trip-card-meta"><i class="fas fa-user"></i> 1 Traveler</div>
          </div>
          <div class="trip-card-footer">
            <span style="color:var(--text2)">Budget</span>
            <span style="color:var(--primary)">$3,200</span>
          </div>
        </div>
      </div>
        """
    },
    "trips.html": {
        "title": "My Trips",
        "css": "trips",
        "module": "trips",
        "content": """
      <div class="screen-header">
        <h1>My Trips</h1>
        <button class="btn btn-primary" onclick="showModal('plan-trip-modal')"><i class="fas fa-plus"></i> New Trip</button>
      </div>

      <div class="section-title">
        <span class="badge badge-green">Ongoing</span>
        <h3 style="margin:0">Tokyo Highlights</h3>
      </div>
      <div class="card" style="margin-bottom:32px">
        <div class="card-header">
          <div>
            <div style="font-weight:bold; margin-bottom:4px">May 1-8 2026</div>
            <div style="color:var(--text2)">Day 4 of 8</div>
          </div>
          <a href="itinerary-builder.html" class="btn btn-teal btn-sm">View Details</a>
        </div>
        <div class="progress-bar">
          <div class="progress-fill teal" style="width: 60%"></div>
        </div>
      </div>

      <div class="section-title">
        <span class="badge badge-amber">Upcoming</span>
        <h3 style="margin:0">Bali Wellness Retreat</h3>
      </div>
      <div class="card" style="margin-bottom:32px">
        <div class="card-header" style="margin:0">
          <div>
            <div style="font-weight:bold; margin-bottom:4px">Aug 10-17 2026</div>
            <div style="color:var(--text2)">Budget $3,200</div>
          </div>
          <a href="itinerary-builder.html" class="btn btn-primary btn-sm">Manage Trip</a>
        </div>
      </div>

      <div class="section-title">
        <span class="badge badge-gray">Completed</span>
        <h3 style="margin:0">Past Journeys</h3>
      </div>
      <div class="grid-2">
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">Paris & Rome</div>
            <div class="trip-card-meta">Jun 2025</div>
          </div>
        </div>
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">London Winter</div>
            <div class="trip-card-meta">Dec 2024</div>
          </div>
        </div>
      </div>
        """
    },
    "create-trip.html": {
        "title": "Create Trip",
        "css": "dashboard",
        "module": "trips",
        "content": """
      <div class="screen-header">
        <h1>Create Trip</h1>
      </div>
      <div class="grid-2">
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 24px;">Trip Details</h3>
          <div class="input-group">
            <label class="label">Trip Name</label>
            <input type="text" class="input" placeholder="e.g. Summer Vacation">
          </div>
          <div class="form-grid">
            <div class="input-group">
              <label class="label">Start Date</label>
              <input type="date" class="input">
            </div>
            <div class="input-group">
              <label class="label">End Date</label>
              <input type="date" class="input">
            </div>
          </div>
          <div class="input-group">
            <label class="label">Select a Place</label>
            <select class="select">
              <option>Paris, France</option>
              <option>Rome, Italy</option>
              <option>Jaipur, India</option>
            </select>
          </div>
          <div class="form-grid">
            <div class="input-group">
              <label class="label">Number of Travelers</label>
              <input type="number" class="input" value="2">
            </div>
            <div class="input-group">
              <label class="label">Total Budget ($)</label>
              <input type="number" class="input" value="5000">
            </div>
          </div>
          <div class="input-group">
            <label class="label">Trip Notes</label>
            <textarea class="input" rows="3" placeholder="Any special requirements..."></textarea>
          </div>
          <div style="display:flex; gap:16px; margin-top:24px;">
            <a href="itinerary-builder.html" class="btn btn-primary" style="flex:1">Build Itinerary</a>
            <a href="dashboard.html" class="btn" style="flex:1; border:1px solid var(--border)">Cancel</a>
          </div>
        </div>
        <div>
          <div class="card" style="margin-bottom: 24px;">
            <h3 class="card-title" style="margin-bottom: 16px;">Suggested Places to Visit</h3>
            <div class="grid-3">
              <div class="dest-card"><div class="dest-thumb">🗼</div><div class="dest-label">Eiffel Tower</div></div>
              <div class="dest-card"><div class="dest-thumb">🏟️</div><div class="dest-label">Colosseum</div></div>
              <div class="dest-card"><div class="dest-thumb">🖼️</div><div class="dest-label">Louvre</div></div>
              <div class="dest-card"><div class="dest-thumb">⛪</div><div class="dest-label">Vatican</div></div>
              <div class="dest-card"><div class="dest-thumb">🍝</div><div class="dest-label">Food Tour</div></div>
              <div class="dest-card"><div class="dest-thumb">🛥️</div><div class="dest-label">Seine Cruise</div></div>
            </div>
          </div>
          <div class="card">
            <h3 class="card-title" style="margin-bottom: 16px;">Suggested Activities</h3>
            <div style="display:flex; flex-wrap:wrap;">
              <span class="chip active">Art & Culture</span>
              <span class="chip">Food & Dining</span>
              <span class="chip">Walking Tours</span>
              <span class="chip">Water Sports</span>
              <span class="chip">Adventure</span>
              <span class="chip active">Photography</span>
              <span class="chip">Theatre</span>
              <span class="chip">Shopping</span>
            </div>
          </div>
        </div>
      </div>
        """
    },
    "itinerary-builder.html": {
        "title": "Itinerary Builder",
        "css": "itinerary",
        "module": "itinerary",
        "content": """
      <div class="screen-header" style="margin-bottom:8px">
        <h1>Itinerary</h1>
        <div>
          <button class="btn btn-primary btn-sm">+ Add Section</button>
          <a href="budget.html" class="btn btn-accent btn-sm">View Budget</a>
        </div>
      </div>
      <p style="color:var(--text2); margin-bottom:24px">Paris & Rome Adventure · Jun 15-26</p>
      
      <div class="itinerary-toolbar">
        <span class="badge badge-amber">Physical & Cultural</span>
      </div>

      <div class="grid-2">
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 24px;">Build Itinerary</h3>
          
          <div style="border-left: 2px solid var(--border); padding-left: 24px; margin-left: 12px;">
            <div style="position:relative; margin-bottom: 32px;">
              <div style="position:absolute; left:-31px; top:0; width:16px; height:16px; border-radius:50%; background:var(--accent);"></div>
              <div style="font-weight:bold; font-size:1.125rem">Section 1: Paris Stay</div>
              <div style="color:var(--text2); font-size:0.875rem; margin-bottom:8px">hotel + tours — Jun 15-19</div>
              <div class="badge badge-teal" style="background:rgba(22,199,154,0.1); color:var(--teal)">Budget $9,000</div>
            </div>
            
            <div style="position:relative; margin-bottom: 32px;">
              <div style="position:absolute; left:-31px; top:0; width:16px; height:16px; border-radius:50%; background:var(--accent2);"></div>
              <div style="font-weight:bold; font-size:1.125rem">Section 2: Travel to Rome</div>
              <div style="color:var(--text2); font-size:0.875rem; margin-bottom:8px">flight + train — Jun 19-20</div>
              <div class="badge badge-teal" style="background:rgba(22,199,154,0.1); color:var(--teal)">Budget $12,000</div>
            </div>

            <div style="position:relative; margin-bottom: 16px;">
              <div style="position:absolute; left:-31px; top:0; width:16px; height:16px; border-radius:50%; background:var(--primary);"></div>
              <div style="font-weight:bold; font-size:1.125rem">Section 3: Rome Stay</div>
              <div style="color:var(--text2); font-size:0.875rem; margin-bottom:8px">hotel + Vatican + Colosseum — Jun 20-26</div>
              <div class="badge badge-teal" style="background:rgba(22,199,154,0.1); color:var(--teal)">Budget $1,000</div>
            </div>
          </div>
        </div>

        <div class="card">
          <h3 class="card-title" style="margin-bottom: 24px;">Day-by-Day View</h3>
          
          <div class="day-block">
            <div class="day-label">Day 1 Jun 15</div>
            <div class="itinerary-item">
              <div class="itinerary-time">09:00</div>
              <div class="itinerary-content">
                <h4>Flight DEL→PAR</h4>
              </div>
              <div class="itinerary-budget">$3,000</div>
            </div>
            <div class="itinerary-item">
              <div class="itinerary-time">19:30</div>
              <div class="itinerary-content">
                <h4>Hotel Check-in</h4>
              </div>
              <div class="itinerary-budget">$900/n</div>
            </div>
          </div>

          <div class="day-block">
            <div class="day-label">Day 2 Jun 16</div>
            <div class="itinerary-item">
              <div class="itinerary-time">09:00</div>
              <div class="itinerary-content">
                <h4>Eiffel Tower</h4>
              </div>
              <div class="itinerary-budget">$120</div>
            </div>
            <div class="itinerary-item">
              <div class="itinerary-time">14:00</div>
              <div class="itinerary-content">
                <h4>Louvre</h4>
              </div>
              <div class="itinerary-budget">$80</div>
            </div>
            <div class="itinerary-item">
              <div class="itinerary-time">20:00</div>
              <div class="itinerary-content">
                <h4>Seine Cruise</h4>
              </div>
              <div class="itinerary-budget">$200</div>
            </div>
          </div>

          <div class="day-block">
            <div class="day-label">Day 3 Jun 17</div>
            <div class="itinerary-item">
              <div class="itinerary-time">10:00</div>
              <div class="itinerary-content">
                <h4>Versailles</h4>
              </div>
              <div class="itinerary-budget">$150</div>
            </div>
          </div>

        </div>
      </div>
        """
    },
    "itinerary-view.html": {
        "title": "Itinerary View",
        "css": "itinerary",
        "module": "itinerary",
        "content": "<script>window.location.href='itinerary-builder.html';</script>"
    },
    "city-search.html": {
        "title": "City Search",
        "css": "search",
        "module": "search",
        "content": "<script>window.location.href='activity-search.html';</script>"
    },
    "shared-itinerary.html": {
        "title": "Shared Itinerary",
        "css": "itinerary",
        "module": "itinerary",
        "content": "<script>window.location.href='itinerary-builder.html';</script>"
    },
    "activity-search.html": {
        "title": "Activity Search",
        "css": "search",
        "module": "search",
        "content": """
      <div class="screen-header">
        <h1>Activity & City Search</h1>
      </div>
      
      <div class="card" style="margin-bottom: 24px;">
        <div class="search-bar-container">
          <input type="text" class="input" placeholder="Search for activities..." style="flex:1" id="searchInput">
          <select class="select" style="width: 200px;">
            <option>All Categories</option>
            <option>Adventure</option>
            <option>Culture</option>
            <option>Food</option>
          </select>
          <button class="btn btn-primary" onclick="runSearch()">Search</button>
        </div>
        <div style="display:flex; flex-wrap:wrap; margin-bottom:16px">
          <span class="chip active">Paragliding</span>
          <span class="chip">Hiking</span>
          <span class="chip">Food Tour</span>
          <span class="chip">Museum</span>
          <span class="chip">Beach</span>
          <span class="chip">Cycling</span>
        </div>
        <div id="searchResultLabel" style="font-weight:bold; color:var(--primary)">Showing 7 results for "Paragliding"</div>
      </div>

      <div class="search-result">
        <div class="search-result-icon">🪂</div>
        <div class="search-result-info">
          <div class="search-result-name">Paragliding in Interlaken</div>
          <div class="search-result-meta">Switzerland · 2h · ★4.9</div>
        </div>
        <div class="search-result-price">$180</div>
        <button class="btn btn-accent btn-sm">Add</button>
      </div>

      <div class="search-result">
        <div class="search-result-icon">🪂</div>
        <div class="search-result-info">
          <div class="search-result-name">Paragliding over Chamonix Alps</div>
          <div class="search-result-meta">France · 1.5h · ★4.8</div>
        </div>
        <div class="search-result-price">$220</div>
        <button class="btn btn-accent btn-sm">Add</button>
      </div>

      <div class="search-result">
        <div class="search-result-icon">🪂</div>
        <div class="search-result-info">
          <div class="search-result-name">Tandem Paragliding Queenstown</div>
          <div class="search-result-meta">New Zealand · 45min · ★4.9</div>
        </div>
        <div class="search-result-price">$265</div>
        <button class="btn btn-accent btn-sm">Add</button>
      </div>

      <div class="search-result">
        <div class="search-result-icon">🪂</div>
        <div class="search-result-info">
          <div class="search-result-name">Paragliding Bir Billing India</div>
          <div class="search-result-meta">Himachal Pradesh · 2h · ★4.7</div>
        </div>
        <div class="search-result-price">$45</div>
        <button class="btn btn-accent btn-sm">Add</button>
      </div>

      <div class="search-result">
        <div class="search-result-icon">🪂</div>
        <div class="search-result-info">
          <div class="search-result-name">Paragliding Oludeniz Turkey</div>
          <div class="search-result-meta">Fethiye · 30min · ★4.8</div>
        </div>
        <div class="search-result-price">$90</div>
        <button class="btn btn-accent btn-sm">Add</button>
      </div>

      <div class="search-result">
        <div class="search-result-icon">🪂</div>
        <div class="search-result-info">
          <div class="search-result-name">Sunrise Paragliding Pokhara</div>
          <div class="search-result-meta">Nepal · 1h · ★4.9</div>
        </div>
        <div class="search-result-price">$75</div>
        <button class="btn btn-accent btn-sm">Add</button>
      </div>

      <div class="search-result">
        <div class="search-result-icon">🪂</div>
        <div class="search-result-info">
          <div class="search-result-name">Paragliding Monte Baldo Lake Garda</div>
          <div class="search-result-meta">Italy · 1h · ★4.7</div>
        </div>
        <div class="search-result-price">$135</div>
        <button class="btn btn-accent btn-sm">Add</button>
      </div>
        """
    },
    "checklist.html": {
        "title": "Checklist",
        "css": "checklist",
        "module": "checklist",
        "content": """
      <div class="screen-header">
        <div>
          <h1 style="margin-bottom:8px">Packing Checklist</h1>
          <p style="color:var(--text2)">Paris & Rome Adventure</p>
        </div>
        <div style="display:flex;gap:16px">
          <button class="btn btn-sm" style="border:1px solid var(--border)" onclick="resetChecklist()">Reset</button>
          <button class="btn btn-primary btn-sm"><i class="fas fa-share-alt"></i> Share</button>
        </div>
      </div>

      <div class="card" style="margin-bottom: 24px; display:flex; align-items:center; gap:24px">
        <div style="flex:1">
          <div style="display:flex; justify-content:space-between; margin-bottom:8px">
            <span style="font-weight:bold" id="progress-text">5 / 12 items packed</span>
            <span class="badge badge-amber">Almost there</span>
          </div>
          <div class="progress-bar">
            <div class="progress-fill teal" style="width: 42%"></div>
          </div>
        </div>
      </div>

      <div class="grid-2">
        <div>
          <div class="checklist-group">
            <div class="checklist-group-header">
              <span>Documents</span>
              <span style="color:var(--text3)">3/4</span>
            </div>
            <div class="checklist-items">
              <div class="check-item checked" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-check-square"></i></div> <span>Passport</span>
              </div>
              <div class="check-item checked" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-check-square"></i></div> <span>Flight Tickets</span>
              </div>
              <div class="check-item checked" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-check-square"></i></div> <span>Travel Insurance</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Hotel Booking Confirmation</span>
              </div>
            </div>
          </div>

          <div class="checklist-group">
            <div class="checklist-group-header">
              <span>Clothing</span>
              <span style="color:var(--text3)">1/4</span>
            </div>
            <div class="checklist-items">
              <div class="check-item checked" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-check-square"></i></div> <span>Casual Shirts</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Trousers</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Walking Shoes</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Light Jacket</span>
              </div>
            </div>
          </div>
        </div>

        <div>
          <div class="checklist-group">
            <div class="checklist-group-header">
              <span>Electronics</span>
              <span style="color:var(--text3)">1/3</span>
            </div>
            <div class="checklist-items">
              <div class="check-item checked" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-check-square"></i></div> <span>Phone Charger</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Power Adapter</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Earphones</span>
              </div>
            </div>
          </div>

          <div class="checklist-group">
            <div class="checklist-group-header">
              <span>Health & Hygiene</span>
              <span style="color:var(--text3)">0/3</span>
            </div>
            <div class="checklist-items">
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Medicines</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>Sunscreen</span>
              </div>
              <div class="check-item" onclick="toggleCheck(this)">
                <div class="check-box"><i class="far fa-square"></i></div> <span>First Aid Kit</span>
              </div>
            </div>
          </div>

          <button class="btn btn-primary" style="width:100%" onclick="showModal('add-item-modal')">+ Add Item to Checklist</button>
        </div>
      </div>
        """
    },
    "notes.html": {
        "title": "Trip Notes",
        "css": "notes",
        "module": "notes",
        "content": """
      <div class="screen-header">
        <h1>Trip Notes & Journal</h1>
        <button class="btn btn-accent" onclick="showModal('add-note-modal')"><i class="fas fa-plus"></i> Add Note</button>
      </div>
      <div class="tab-row">
        <div class="tab active" onclick="filterNotes('all', this)">All Notes</div>
        <div class="tab" onclick="filterNotes('day', this)">By Day</div>
        <div class="tab" onclick="filterNotes('stop', this)">By Stop</div>
      </div>

      <div id="notes-container">
        <div class="note-card">
          <div class="note-header">
            <h3 class="note-title">Hotel Check-in Details – Rome Stop</h3>
            <div class="note-actions">
              <button class="btn-icon"><i class="fas fa-tag"></i></button>
              <button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove()"><i class="fas fa-trash"></i></button>
            </div>
          </div>
          <p class="note-body">Check in after 2pm, Room 302, Breakfast included 7-10am. Make sure to present booking confirmation #1920X.</p>
          <div class="note-meta">Day 3 · June 19, 2025 · Rome</div>
        </div>

        <div class="note-card">
          <div class="note-header">
            <h3 class="note-title">Best restaurants near Colosseum</h3>
            <div class="note-actions">
              <button class="btn-icon"><i class="fas fa-tag"></i></button>
              <button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove()"><i class="fas fa-trash"></i></button>
            </div>
          </div>
          <p class="note-body">Osteria Barberini – try the cacio e pepe. Book in advance! Also check out Trattoria Luzzi for good wood-fired pizza.</p>
          <div class="note-meta">Day 5 · June 21, 2025 · Rome</div>
        </div>

        <div class="note-card">
          <div class="note-header">
            <h3 class="note-title">Louvre Tips – Paris Stop</h3>
            <div class="note-actions">
              <button class="btn-icon"><i class="fas fa-tag"></i></button>
              <button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove()"><i class="fas fa-trash"></i></button>
            </div>
          </div>
          <p class="note-body">Enter through Richelieu wing to avoid crowds. Mona Lisa Level 1. Remember comfortable walking shoes.</p>
          <div class="note-meta">Day 2 · June 16, 2025 · Paris</div>
        </div>
      </div>
        """
    },
    "budget.html": {
        "title": "Expense & Invoice",
        "css": "budget",
        "module": "budget",
        "content": """
      <div class="screen-header">
        <h1>Expense & Invoice</h1>
        <div style="display:flex; gap:16px;">
          <input type="text" class="input" placeholder="Search invoices...">
          <a href="dashboard.html" class="btn" style="border:1px solid var(--border)">Back</a>
        </div>
      </div>

      <div class="grid-2">
        <div class="invoice-header">
          <div style="font-size: 2rem; margin-bottom: 8px;">🗺️</div>
          <h2>Trip to Europe Adventure</h2>
          <div class="invoice-info">
            <p>May 15 - Jun 05 2025</p>
            <p>4 cities · Created by James</p>
            <p><i class="fas fa-user-friends"></i> 4 Travelers</p>
          </div>
          <div style="margin-top: 16px;">
            <span class="badge badge-amber" style="background:rgba(255,255,255,0.2);color:white">Payment Pending</span>
          </div>
          <div style="position:absolute; top:24px; right:24px; font-family:var(--font-mono); font-size:0.875rem; color:rgba(255,255,255,0.7)">INV-xyz-30290</div>
        </div>

        <div class="card">
          <h3 class="card-title" style="margin-bottom:16px">Budget Insights</h3>
          <div style="display:flex; align-items:center; gap:24px">
            <div class="chart-container" style="width:120px; height:120px; border-radius:50%; background:conic-gradient(var(--accent) 0% 55%, var(--teal) 55% 96%, var(--surface3) 96% 100%);"></div>
            <div style="flex:1">
              <div style="margin-bottom:8px"><span style="color:var(--text2)">Total Budget:</span> <strong>$20,000</strong></div>
              <div style="margin-bottom:8px"><span style="color:var(--text2)">Total Spent:</span> <strong style="color:var(--accent)">$22,000</strong></div>
              <div style="margin-bottom:16px"><span style="color:var(--text2)">Remaining:</span> <strong style="color:var(--accent)">-$2,000</strong></div>
              <div style="display:flex; gap:12px; font-size:0.75rem;">
                <span style="display:flex;align-items:center;gap:4px"><div style="width:8px;height:8px;background:var(--teal);border-radius:50%"></div> Hotel 41%</span>
                <span style="display:flex;align-items:center;gap:4px"><div style="width:8px;height:8px;background:var(--accent);border-radius:50%"></div> Travel 55%</span>
                <span style="display:flex;align-items:center;gap:4px"><div style="width:8px;height:8px;background:var(--surface3);border-radius:50%"></div> Other 4%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="invoice-details">
        <div style="overflow-x:auto;">
          <table class="data-table" style="min-width:700px">
            <thead>
              <tr>
                <th>#</th>
                <th>Category</th>
                <th>Description</th>
                <th>Qty</th>
                <th>Unit Cost</th>
                <th style="text-align:right">Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td><span class="badge badge-blue">Hotel</span></td>
                <td>Hotel Booking Paris 3 nights</td>
                <td>3 nights</td>
                <td>$3,000</td>
                <td style="text-align:right">$9,000</td>
              </tr>
              <tr>
                <td>2</td>
                <td><span class="badge badge-pink">Travel</span></td>
                <td>Flight DEL→PAR</td>
                <td>4 tickets</td>
                <td>$3,000</td>
                <td style="text-align:right">$12,000</td>
              </tr>
              <tr>
                <td>3</td>
                <td><span class="badge badge-green">Activity</span></td>
                <td>Guided Tours & Entrances</td>
                <td>4 persons</td>
                <td>$250</td>
                <td style="text-align:right">$1,000</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <div class="invoice-totals" style="width:300px; margin-left:auto">
          <div class="invoice-total-row"><span>Subtotal</span><span>$21,000</span></div>
          <div class="invoice-total-row"><span>Tax 5%</span><span>$1,050</span></div>
          <div class="invoice-total-row"><span>Discount</span><span>-$50</span></div>
          <div class="invoice-total-row grand-total"><span>Grand Total</span><span>$22,000</span></div>
        </div>
      </div>

      <div style="display:flex; justify-content:flex-end; gap:16px; margin-top:24px">
        <button class="btn" style="border:1px solid var(--border)"><i class="fas fa-download"></i> Download Invoice</button>
        <button class="btn" style="border:1px solid var(--border)"><i class="fas fa-file-pdf"></i> Export as PDF</button>
        <button class="btn btn-teal">Mark as Paid</button>
      </div>
        """
    },
    "community.html": {
        "title": "Community",
        "css": "community",
        "module": "community",
        "content": """
      <div class="screen-header">
        <h1>Community</h1>
        <button class="btn btn-accent"><i class="fas fa-pen"></i> Write a Post</button>
      </div>

      <div class="card" style="margin-bottom: 32px; background: rgba(22, 199, 154, 0.1); border: 1px solid var(--teal)">
        <p style="color:var(--primary); font-weight:500">Welcome to the Traveloop Community! Connect with fellow travelers, share your experiences, and discover new destinations.</p>
      </div>

      <div class="grid-2">
        <div class="community-card">
          <div class="community-header">
            <div class="community-avatar" style="background-color: var(--accent);">MR</div>
            <div>
              <div class="community-author">Mrudul Mistri <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div>
              <div style="font-size:0.875rem; color:var(--text3)">2 days ago</div>
            </div>
          </div>
          <div class="community-content">
            Paragliding in Interlaken was simply breathtaking! The views of the Swiss Alps are unparalleled. Highly recommend doing it early morning for the best weather. 🪂🏔️
          </div>
          <div style="margin-bottom:16px">
            <span class="badge badge-gray">Switzerland</span>
            <span class="badge badge-gray">Adventure</span>
            <span class="badge badge-gray">Paragliding</span>
          </div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action"><i class="far fa-heart"></i> 142</div>
              <div class="community-action"><i class="far fa-comment"></i> 28</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>

        <div class="community-card">
          <div class="community-header">
            <div class="community-avatar" style="background-color: var(--teal);">YZ</div>
            <div>
              <div class="community-author">Yuvraj Zende <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div>
              <div style="font-size:0.875rem; color:var(--text3)">5 days ago</div>
            </div>
          </div>
          <div class="community-content">
            Rome in June is quite warm but absolutely magical. Don't skip the Vatican Museum, and definitely book your Colosseum tickets way in advance! 🏛️🍕
          </div>
          <div style="margin-bottom:16px">
            <span class="badge badge-gray">Italy</span>
            <span class="badge badge-gray">Rome</span>
            <span class="badge badge-gray">Culture</span>
          </div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action"><i class="far fa-heart"></i> 89</div>
              <div class="community-action"><i class="far fa-comment"></i> 15</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>

        <div class="community-card">
          <div class="community-header">
            <div class="community-avatar" style="background-color: #007bff;">SK</div>
            <div>
              <div class="community-author">Sakthi K <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div>
              <div style="font-size:0.875rem; color:var(--text3)">1 week ago</div>
            </div>
          </div>
          <div class="community-content">
            Just finished a 10-day food tour in Tokyo. From street food in Shinjuku to high-end sushi in Ginza, every meal was a 10/10. Here's my top 5 must-visit spots... 🍣🍜
          </div>
          <div style="margin-bottom:16px">
            <span class="badge badge-gray">Japan</span>
            <span class="badge badge-gray">Food</span>
            <span class="badge badge-gray">Tokyo</span>
          </div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action"><i class="far fa-heart"></i> 214</div>
              <div class="community-action"><i class="far fa-comment"></i> 41</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>

        <div class="community-card">
          <div class="community-header">
            <div class="community-avatar" style="background-color: var(--accent2);">HS</div>
            <div>
              <div class="community-author">Heshinth S <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div>
              <div style="font-size:0.875rem; color:var(--text3)">2 weeks ago</div>
            </div>
          </div>
          <div class="community-content">
            Backpacking through Southeast Asia on a $1200 budget for a whole month. It's totally doable! Stayed in hostels, ate local street food, and used night buses. Best experience ever. 🎒🌏
          </div>
          <div style="margin-bottom:16px">
            <span class="badge badge-gray">Southeast Asia</span>
            <span class="badge badge-gray">Budget Travel</span>
            <span class="badge badge-gray">Solo</span>
          </div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action"><i class="far fa-heart"></i> 376</div>
              <div class="community-action"><i class="far fa-comment"></i> 92</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>
      </div>
        """
    },
    "profile.html": {
        "title": "User Profile",
        "css": "profile",
        "module": "profile",
        "content": """
      <div class="screen-header">
        <h1>User Profile</h1>
        <button class="btn btn-primary"><i class="fas fa-edit"></i> Edit Profile</button>
      </div>

      <div class="profile-header">
        <div class="profile-avatar">JA</div>
        <div class="profile-info">
          <h1>James Arjun</h1>
          <p style="color:var(--text2); margin-bottom:8px">james.arjun@email.com · Mumbai, India</p>
          <p style="margin-bottom:12px; max-width:600px">Passionate traveler | Photography enthusiast | 22 countries visited</p>
          <div>
            <span class="badge badge-green">Verified</span>
            <span class="badge badge-blue">Premium Member</span>
          </div>
        </div>
        <div class="profile-stats">
          <div>
            <div class="profile-stat-val">22</div>
            <div class="profile-stat-label">Countries</div>
          </div>
          <div>
            <div class="profile-stat-val">47</div>
            <div class="profile-stat-label">Trips</div>
          </div>
          <div>
            <div class="profile-stat-val">312</div>
            <div class="profile-stat-label">Followers</div>
          </div>
        </div>
      </div>

      <h3 class="card-title" style="margin-bottom:16px">Preplanned Trips</h3>
      <div class="grid-3" style="margin-bottom:32px">
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">Bali Wellness Retreat</div>
            <div class="trip-card-meta">Upcoming Aug 2026</div>
          </div>
        </div>
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">Greek Island Hopping</div>
            <div class="trip-card-meta">Upcoming Oct 2026</div>
          </div>
        </div>
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">Machu Picchu Trek</div>
            <div class="trip-card-meta">Upcoming Jan 2027</div>
          </div>
        </div>
      </div>

      <h3 class="card-title" style="margin-bottom:16px">Previous Trips</h3>
      <div class="grid-3">
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">Paris & Rome Adventure</div>
            <div class="trip-card-meta">Completed Jun 2025</div>
          </div>
        </div>
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">London Winter Trip</div>
            <div class="trip-card-meta">Completed Dec 2024</div>
          </div>
        </div>
        <div class="trip-card">
          <div class="trip-card-body">
            <div class="trip-card-name">Thailand Backpacking</div>
            <div class="trip-card-meta">Completed Mar 2024</div>
          </div>
        </div>
      </div>
        """
    },
    "admin.html": {
        "title": "Admin Panel",
        "css": "admin",
        "module": "admin",
        "content": """
      <div class="screen-header">
        <div>
          <h1 style="margin-bottom:8px">Admin Panel</h1>
          <p style="color:var(--text2)">Platform management & analytics</p>
        </div>
      </div>

      <div class="admin-tabs">
        <div class="admin-tab active" onclick="switchAdminTab('users', this)">Manage Users</div>
        <div class="admin-tab" onclick="switchAdminTab('cities', this)">Popular Cities</div>
        <div class="admin-tab" onclick="switchAdminTab('activities', this)">Popular Activities</div>
        <div class="admin-tab" onclick="switchAdminTab('trends', this)">Trends & Analytics</div>
      </div>

      <div id="admin-tab-users" class="admin-panel-content" style="display:block">
        <div class="grid-4" style="margin-bottom:24px">
          <div class="stat-card">
            <div class="stat-icon"><i class="fas fa-users"></i></div>
            <div class="stat-info">
              <div class="stat-label">Total Users</div>
              <div class="stat-value">12,840</div>
              <div class="stat-delta">↑ 8.2%</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(22,199,154,0.1); color:var(--teal)"><i class="fas fa-map-marked-alt"></i></div>
            <div class="stat-info">
              <div class="stat-label">Active Trips</div>
              <div class="stat-value">3,421</div>
              <div class="stat-delta">↑ 14.1%</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(245,166,35,0.1); color:var(--accent2)"><i class="fas fa-dollar-sign"></i></div>
            <div class="stat-info">
              <div class="stat-label">Revenue May</div>
              <div class="stat-value">$84K</div>
              <div class="stat-delta">↑ 5.6%</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(0,123,255,0.1); color:#007bff"><i class="fas fa-star"></i></div>
            <div class="stat-info">
              <div class="stat-label">Avg Rating</div>
              <div class="stat-value">4.87</div>
              <div class="stat-delta">↑ 0.04</div>
            </div>
          </div>
        </div>

        <div class="card" style="overflow-x:auto">
          <table class="data-table">
            <thead>
              <tr>
                <th>User</th>
                <th>Email</th>
                <th>Trips</th>
                <th>Joined</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight:bold">James Arjun</td>
                <td>james@email.com</td>
                <td>47</td>
                <td>Jan 2023</td>
                <td><span class="badge badge-green">Active</span></td>
                <td><button class="btn btn-sm" style="border:1px solid var(--border)">View</button></td>
              </tr>
              <tr>
                <td style="font-weight:bold">Mrudul Mistri</td>
                <td>mrudul@email.com</td>
                <td>31</td>
                <td>Mar 2023</td>
                <td><span class="badge badge-green">Active</span></td>
                <td><button class="btn btn-sm" style="border:1px solid var(--border)">View</button></td>
              </tr>
              <tr>
                <td style="font-weight:bold">Yuvraj Zende</td>
                <td>yuvraj@email.com</td>
                <td>22</td>
                <td>Jun 2023</td>
                <td><span class="badge badge-green">Active</span></td>
                <td><button class="btn btn-sm" style="border:1px solid var(--border)">View</button></td>
              </tr>
              <tr>
                <td style="font-weight:bold">Sakthi K</td>
                <td>sakthi@email.com</td>
                <td>18</td>
                <td>Sep 2023</td>
                <td><span class="badge badge-gray">Inactive</span></td>
                <td><button class="btn btn-sm" style="border:1px solid var(--border)">View</button></td>
              </tr>
              <tr>
                <td style="font-weight:bold">Heshinth S</td>
                <td>heshinth@email.com</td>
                <td>56</td>
                <td>Nov 2022</td>
                <td><span class="badge badge-green">Active</span></td>
                <td><button class="btn btn-sm" style="border:1px solid var(--border)">View</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div id="admin-tab-cities" class="admin-panel-content">
        <div class="card" style="max-width:800px; margin:0 auto">
          <h3 class="card-title" style="margin-bottom:24px">Popular Cities</h3>
          <div class="chart-bar">
            <div class="chart-bar-label">Paris</div>
            <div class="chart-bar-track"><div class="chart-bar-fill" style="width:88%; background:var(--accent)">8820</div></div>
            <div style="font-weight:bold">88%</div>
          </div>
          <div class="chart-bar">
            <div class="chart-bar-label">Tokyo</div>
            <div class="chart-bar-track"><div class="chart-bar-fill" style="width:79%; background:var(--teal)">7940</div></div>
            <div style="font-weight:bold">79%</div>
          </div>
          <div class="chart-bar">
            <div class="chart-bar-label">Rome</div>
            <div class="chart-bar-track"><div class="chart-bar-fill" style="width:71%; background:var(--accent2)">7120</div></div>
            <div style="font-weight:bold">71%</div>
          </div>
          <div class="chart-bar">
            <div class="chart-bar-label">New York</div>
            <div class="chart-bar-track"><div class="chart-bar-fill" style="width:65%; background:#007bff">6510</div></div>
            <div style="font-weight:bold">65%</div>
          </div>
          <div class="chart-bar">
            <div class="chart-bar-label">Bali</div>
            <div class="chart-bar-track"><div class="chart-bar-fill" style="width:55%; background:#28a745">5530</div></div>
            <div style="font-weight:bold">55%</div>
          </div>
        </div>
      </div>

      <div id="admin-tab-activities" class="admin-panel-content">
        <div class="card" style="overflow-x:auto">
          <table class="data-table">
            <thead>
              <tr>
                <th>Activity</th>
                <th>Category</th>
                <th>Bookings</th>
                <th>Avg Rating</th>
                <th>Revenue</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight:bold">Paragliding</td>
                <td><span class="badge badge-gray">Adventure</span></td>
                <td>4,210</td>
                <td>★4.9</td>
                <td style="color:var(--teal);font-weight:bold">$840K</td>
              </tr>
              <tr>
                <td style="font-weight:bold">Guided City Tours</td>
                <td><span class="badge badge-gray">Culture</span></td>
                <td>9,830</td>
                <td>★4.7</td>
                <td style="color:var(--teal);font-weight:bold">$490K</td>
              </tr>
              <tr>
                <td style="font-weight:bold">Food & Wine Tasting</td>
                <td><span class="badge badge-gray">Food</span></td>
                <td>7,120</td>
                <td>★4.8</td>
                <td style="color:var(--teal);font-weight:bold">$356K</td>
              </tr>
              <tr>
                <td style="font-weight:bold">Scuba Diving</td>
                <td><span class="badge badge-gray">Adventure</span></td>
                <td>2,890</td>
                <td>★4.9</td>
                <td style="color:var(--teal);font-weight:bold">$578K</td>
              </tr>
              <tr>
                <td style="font-weight:bold">Museum Passes</td>
                <td><span class="badge badge-gray">Culture</span></td>
                <td>11,240</td>
                <td>★4.6</td>
                <td style="color:var(--teal);font-weight:bold">$224K</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div id="admin-tab-trends" class="admin-panel-content">
        <div class="grid-2">
          <div class="card">
             <h3 class="card-title" style="margin-bottom:24px">Revenue Distribution</h3>
             <div style="display:flex; justify-content:center; align-items:center; height:200px">
                <div style="width:160px; height:160px; border-radius:50%; background:conic-gradient(var(--accent) 0% 50%, var(--teal) 50% 80%, var(--accent2) 80% 100%); position:relative;">
                  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:var(--surface);width:100px;height:100px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:bold;">
                    Total
                    <span style="color:var(--teal)">$84K</span>
                  </div>
                </div>
             </div>
             <div style="display:flex; justify-content:center; gap:16px; margin-top:24px;">
               <span style="display:flex;align-items:center;gap:4px"><div style="width:12px;height:12px;background:var(--accent);border-radius:4px"></div> Hotels 50%</span>
               <span style="display:flex;align-items:center;gap:4px"><div style="width:12px;height:12px;background:var(--teal);border-radius:4px"></div> Flights 30%</span>
               <span style="display:flex;align-items:center;gap:4px"><div style="width:12px;height:12px;background:var(--accent2);border-radius:4px"></div> Activities 20%</span>
             </div>
          </div>
          <div class="grid-2">
            <div class="stat-card" style="flex-direction:column; align-items:flex-start">
              <div class="stat-label">Avg Trip Duration</div>
              <div class="stat-value" style="font-size:2rem">9.4 days</div>
            </div>
            <div class="stat-card" style="flex-direction:column; align-items:flex-start">
              <div class="stat-label">Avg Budget</div>
              <div class="stat-value" style="font-size:2rem">$4.2K</div>
              <div class="stat-delta">↑ 6%</div>
            </div>
            <div class="stat-card" style="flex-direction:column; align-items:flex-start">
              <div class="stat-label">Repeat Users</div>
              <div class="stat-value" style="font-size:2rem">68%</div>
              <div class="stat-delta">↑ 3.2%</div>
            </div>
            <div class="stat-card" style="flex-direction:column; align-items:flex-start">
              <div class="stat-label">NPS Score</div>
              <div class="stat-value" style="font-size:2rem">82</div>
              <div class="stat-delta">↑ 4pts</div>
            </div>
          </div>
        </div>
      </div>
        """
    }
}

for filename, data in pages_data.items():
    a_dash = 'active' if filename == 'dashboard.html' else ''
    a_trips = 'active' if filename == 'trips.html' else ''
    a_create = 'active' if filename == 'create-trip.html' else ''
    a_itin = 'active' if 'itinerary' in filename else ''
    a_act = 'active' if 'search' in filename else ''
    a_check = 'active' if filename == 'checklist.html' else ''
    a_note = 'active' if filename == 'notes.html' else ''
    a_bud = 'active' if filename == 'budget.html' else ''
    a_comm = 'active' if filename == 'community.html' else ''
    a_prof = 'active' if filename == 'profile.html' else ''
    a_admin = 'active' if filename == 'admin.html' else ''
    
    extra_css = f'<link rel="stylesheet" href="../css/screens/{data["css"]}.css">' if data["css"] else ''
    
    nav_rendered = layout_nav.format(
        a_dash=a_dash, a_trips=a_trips, a_create=a_create, a_itin=a_itin, 
        a_act=a_act, a_check=a_check, a_note=a_note, a_bud=a_bud, 
        a_comm=a_comm, a_prof=a_prof, a_admin=a_admin
    )
    
    extra_libs = ''
    if data["css"] == "budget":
        extra_libs = '<script src="../libs/chart.min.js"></script>'
    if data["css"] == "itinerary" or data["css"] == "dashboard":
        extra_libs += '<script src="../libs/leaflet/leaflet.min.js"></script>'
        extra_css += '<link rel="stylesheet" href="../libs/leaflet/leaflet.min.css">'
        
    head_rendered = layout_head.format(title=data["title"], extra_css=extra_css)
    scripts_rendered = layout_scripts.format(extra_libs=extra_libs, module_name=data["module"])
    
    full_html = head_rendered + nav_rendered + data["content"] + layout_modals + scripts_rendered
    
    filepath = os.path.join(pages_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {filepath}")

# Create empty dummy files for libs
def touch(p):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f: f.write('')

touch(os.path.join(root_dir, 'libs', 'chart.min.js'))
touch(os.path.join(root_dir, 'libs', 'leaflet', 'leaflet.min.js'))
touch(os.path.join(root_dir, 'libs', 'leaflet', 'leaflet.min.css'))

# Create README.md
with open(os.path.join(root_dir, 'README.md'), 'w') as f:
    f.write("# Traveloop\\n\\nA multi-page travel planning web application built with HTML5, CSS3, and Vanilla JS.\\n")

print("Done")
