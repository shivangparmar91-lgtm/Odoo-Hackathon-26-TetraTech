import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    # Remove .trip-mode { display: none; } if it exists
    css_content = css_content.replace('.trip-mode { display: none; } /* Managed by JS */', '')
    css_content = css_content.replace('.trip-mode { display: none; }', '')
    # Remove .screen logic because we aren't using SPA screens anymore
    css_content = css_content.replace('.screen { display: none; opacity: 0; transition: opacity 0.3s; }', '')
    css_content = css_content.replace('.screen.visible { display: block; opacity: 1; }', '')
    os.makedirs('css', exist_ok=True)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Extract JS
script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
js_content = ""
if script_match:
    js_content = script_match.group(1).strip()
    
    # We want to remove showScreen completely from JS
    js_content = re.sub(r'function showScreen\(name\) \{.*?\n    \}', '', js_content, flags=re.DOTALL)
    
    # We want to remove handleAuth completely from JS
    js_content = re.sub(r'function handleAuth\(e, isSignup = false\) \{.*?\n    \}', '', js_content, flags=re.DOTALL)
    
    # We want to remove toggleAuthTab completely from JS
    js_content = re.sub(r'function toggleAuthTab\(tab\) \{.*?\n    \}', '', js_content, flags=re.DOTALL)

    os.makedirs('js', exist_ok=True)
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

# 3. Extract Screens
screens = {}
screen_matches = re.finditer(r'<div id="screen-([^"]+)" class="screen[^"]*">(.*?)</div>\s*<!-- Screen', content, re.DOTALL)
# Since the last screen doesn't end with <!-- Screen, let's just split by <div id="screen-
screen_parts = re.split(r'<div id="screen-', content)
for part in screen_parts[1:]:
    name_end = part.find('"')
    name = part[:name_end]
    
    # Find the end of the screen div. 
    # Since it's nested, regex is tricky. Let's just use string parsing to find matching </div>
    # But wait, each screen is just followed by <!-- Screen or <script>
    
    # Let's use a simpler heuristic: the screen ends before the next <!-- Screen or <!-- Modals
    end_idx1 = part.find('<!-- Screen')
    end_idx2 = part.find('<!-- Modals')
    end_idx3 = part.find('<script>')
    
    end_idx = min([i for i in [end_idx1, end_idx2, end_idx3] if i != -1])
    
    # The actual HTML
    screen_html = part[part.find('>')+1:end_idx].strip()
    if screen_html.endswith('</div>'):
        screen_html = screen_html[:-6].strip()
        
    screens[name] = screen_html

# Modals
modals_match = re.search(r'<!-- Modals -->(.*?)<script>', content, re.DOTALL)
modals_html = modals_match.group(1).strip() if modals_match else ""

# Layout templates
def get_head(title, is_root=False):
    prefix = "" if is_root else "../"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Traveloop - {title}</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body class="logged-in">
  <!-- Toast Container -->
  <div class="toast-container" id="toast-container"></div>
"""

def get_nav(active_page, is_root=False):
    prefix = "pages/" if is_root else ""
    return f"""
  <!-- Global Topbar -->
  <div class="topbar">
    <div class="topbar-left">Traveloop <div class="dot"></div></div>
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

  <!-- Global Sidebar -->
  <div class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-section-title">Main</div>
      <a class="sidebar-link {'active' if active_page=='home' else ''}" href="{prefix}dashboard.html"><i class="fas fa-home"></i> Home</a>
      <a class="sidebar-link {'active' if active_page=='trips' else ''}" href="{prefix}trips.html"><i class="fas fa-map-marked-alt"></i> My Trips <span class="badge badge-accent" style="background:var(--accent);color:white;margin-left:auto">3</span></a>
      <a class="sidebar-link {'active' if active_page=='plan' else ''}" href="{prefix}create-trip.html"><i class="fas fa-plus-circle"></i> Plan a Trip</a>
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

  <!-- Mobile Bottom Nav -->
  <div class="mobile-nav">
    <a class="{'active' if active_page=='home' else ''}" href="{prefix}dashboard.html"><i class="fas fa-home"></i> Home</a>
    <a class="{'active' if active_page=='trips' else ''}" href="{prefix}trips.html"><i class="fas fa-map-marked-alt"></i> Trips</a>
    <a class="{'active' if active_page=='checklist' else ''}" href="{prefix}checklist.html"><i class="fas fa-check-square"></i> Packing</a>
    <a class="{'active' if active_page=='community' else ''}" href="{prefix}community.html"><i class="fas fa-users"></i> Community</a>
    <a class="{'active' if active_page=='profile' else ''}" href="{prefix}profile.html"><i class="fas fa-user-circle"></i> Profile</a>
  </div>
"""

def get_footer(is_root=False):
    prefix = "" if is_root else "../"
    return f"""
  {modals_html}
  <script src="{prefix}js/main.js"></script>
</body>
</html>
"""

def fix_links(html, is_root=False):
    prefix = "pages/" if is_root else ""
    html = html.replace("showScreen('home')", f"window.location.href='{prefix}dashboard.html'")
    html = html.replace("showScreen('trips')", f"window.location.href='{prefix}trips.html'")
    html = html.replace("showScreen('plan')", f"window.location.href='{prefix}create-trip.html'")
    html = html.replace("showScreen('itinerary')", f"window.location.href='{prefix}itinerary.html'")
    html = html.replace("showScreen('search')", f"window.location.href='{prefix}search.html'")
    html = html.replace("showScreen('checklist')", f"window.location.href='{prefix}checklist.html'")
    html = html.replace("showScreen('notes')", f"window.location.href='{prefix}notes.html'")
    html = html.replace("showScreen('budget')", f"window.location.href='{prefix}budget.html'")
    html = html.replace("showScreen('community')", f"window.location.href='{prefix}community.html'")
    html = html.replace("showScreen('profile')", f"window.location.href='{prefix}profile.html'")
    html = html.replace("showScreen('admin')", f"window.location.href='{prefix}admin.html'")
    return html

os.makedirs('pages', exist_ok=True)

# Generate login page (index.html)
login_html_raw = screens.get('login', '')
login_html_raw = login_html_raw.replace('onsubmit="handleAuth(event)"', 'onsubmit="event.preventDefault(); window.location.href=\'pages/dashboard.html\';"')
login_html_raw = login_html_raw.replace('onsubmit="handleAuth(event, true)"', 'onsubmit="event.preventDefault(); window.location.href=\'pages/dashboard.html\';"')

# We need custom logic to toggle login/signup tabs since we removed handleAuth from main.js
login_script = """
<script>
function toggleAuthTab(tab) {
  document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
  document.getElementById(tab + '-tab').classList.add('active');
  document.getElementById('login-form').style.display = tab === 'login' ? 'block' : 'none';
  document.getElementById('signup-form').style.display = tab === 'signup' ? 'block' : 'none';
}
</script>
"""

# The login page does NOT have the topbar or sidebar, so we construct it manually
index_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Traveloop - Login</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body id="screen-login">
  {login_html_raw}
  <script src="js/main.js"></script>
  {login_script}
</body>
</html>
"""
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_out)

# Generate other pages
page_mapping = {
    'home': 'dashboard.html',
    'trips': 'trips.html',
    'plan': 'create-trip.html',
    'itinerary': 'itinerary.html',
    'search': 'search.html',
    'checklist': 'checklist.html',
    'notes': 'notes.html',
    'budget': 'budget.html',
    'community': 'community.html',
    'profile': 'profile.html',
    'admin': 'admin.html'
}

for screen_name, filename in page_mapping.items():
    if screen_name in screens:
        content_html = f'<div class="main">\n{screens[screen_name]}\n</div>'
        content_html = fix_links(content_html)
        
        full_html = get_head(filename.replace('.html', '').capitalize()) + get_nav(screen_name) + content_html + fix_links(get_footer())
        
        with open(f'pages/{filename}', 'w', encoding='utf-8') as f:
            f.write(full_html)

print("Conversion to multipage completed successfully.")
