import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Traveloop</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
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

    .topbar { position: fixed; top: 0; left: 0; right: 0; height: var(--nav-h); background-color: var(--primary); display: none; align-items: center; justify-content: space-between; padding: 0 24px; z-index: 100; }
    body.logged-in .topbar { display: flex; }
    .topbar-left { display: flex; align-items: center; gap: 8px; color: var(--surface); font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; }
    .topbar-left .dot { width: 8px; height: 8px; border-radius: 50%; background-color: var(--accent); }
    .topbar-center { flex: 1; max-width: 400px; margin: 0 24px; position: relative; }
    .topbar-search { width: 100%; height: 40px; border-radius: 20px; background-color: rgba(255,255,255,0.1); color: var(--surface); padding: 0 16px 0 40px; }
    .topbar-search::placeholder { color: var(--text3); }
    .topbar-center .fa-search { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: var(--text3); }
    .topbar-right { display: flex; align-items: center; gap: 16px; }
    .avatar-circle { width: 36px; height: 36px; border-radius: 50%; background-color: var(--accent); color: var(--surface); display: flex; align-items: center; justify-content: center; font-weight: bold; }

    .sidebar { position: fixed; top: var(--nav-h); left: 0; bottom: 0; width: 220px; background-color: var(--surface); border-right: 1px solid var(--border); padding: 24px 0; overflow-y: auto; z-index: 90; display: none; }
    body.logged-in .sidebar { display: block; }
    .sidebar-section { margin-bottom: 24px; }
    .sidebar-section-title { padding: 0 24px; font-size: 0.75rem; text-transform: uppercase; color: var(--text3); margin-bottom: 8px; font-weight: bold; }
    .sidebar-link { display: flex; align-items: center; padding: 12px 24px; color: var(--text2); transition: all 0.2s; position: relative; gap: 12px; cursor: pointer; }
    .sidebar-link:hover { background-color: var(--surface2); }
    .sidebar-link.active { background-color: rgba(233, 69, 96, 0.1); color: var(--accent); border-left: 4px solid var(--accent); padding-left: 20px; }
    .sidebar-link .badge { margin-left: auto; }

    .main { margin-left: 0; min-height: 100vh; transition: margin-left 0.3s; }
    body.logged-in .main { margin-left: 220px; padding: 32px; margin-top: var(--nav-h); min-height: calc(100vh - var(--nav-h)); }
    
    .mobile-nav { display: none; }

    .screen { display: none; opacity: 0; transition: opacity 0.3s; }
    .screen.visible { display: block; opacity: 1; }
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
    .card-sm { padding: 16px; }
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

    .tab-row { display: flex; gap: 16px; border-bottom: 1px solid var(--border); margin-bottom: 24px; }
    .tab { padding: 12px 0; color: var(--text2); font-weight: 500; border-bottom: 2px solid transparent; cursor: pointer; transition: all 0.2s; }
    .tab.active { color: var(--accent); border-bottom-color: var(--accent); }

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

    /* Trip Type Toggle */
    .trip-type-selector { display:flex; gap:8px; padding: 4px; background: var(--surface2); border-radius: 8px; margin-bottom: 24px; }
    .trip-type-btn { flex: 1; border-radius: 6px; padding: 10px; color: var(--text2); font-weight: 500; background: transparent; transition: all 0.2s; }
    .trip-type-btn.active { background: var(--surface); color: var(--primary); box-shadow: 0 2px 4px rgba(0,0,0,0.05); font-weight: bold; }
    

    /* Login Screen */
    #screen-login { background: linear-gradient(135deg, rgba(26,26,46,0.9), rgba(233,69,96,0.9)), url('https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=1920&q=80') center/cover; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 24px; flex-direction: column; }
    #screen-login.intl-bg { background: linear-gradient(135deg, rgba(26,26,46,0.9), rgba(233,69,96,0.9)), url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=1920&q=80') center/cover; }
    .auth-card { width: 100%; max-width: 400px; }
    .auth-logo { text-align: center; font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--primary); margin-bottom: 24px; display: flex; justify-content: center; align-items: center; gap: 8px; }
    .auth-logo .dot { width: 10px; height: 10px; border-radius: 50%; background-color: var(--accent); }
    .auth-tabs { display: flex; border-bottom: 1px solid var(--border); margin-bottom: 24px; }
    .auth-tab { flex: 1; text-align: center; padding: 12px; font-weight: bold; color: var(--text2); cursor: pointer; border-bottom: 2px solid transparent; transition: all 0.2s; }
    .auth-tab.active { color: var(--accent); border-bottom-color: var(--accent); }

    /* Dashboard */
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
    
    /* Itinerary */
    .day-block { margin-bottom: 24px; }
    .day-label { font-weight: bold; font-family: var(--font-heading); margin-bottom: 12px; color: var(--primary); }
    .itinerary-item { display: flex; gap: 16px; padding: 16px; background-color: var(--surface2); border-radius: var(--radius); margin-bottom: 8px; }
    .itinerary-time { font-family: var(--font-mono); font-weight: bold; color: var(--accent); width: 60px; flex-shrink: 0; }
    .itinerary-content { flex: 1; }
    .itinerary-content h4 { font-size: 1rem; margin-bottom: 4px; }
    .itinerary-content p { font-size: 0.875rem; }
    .itinerary-budget { font-weight: bold; color: var(--teal); }

    /* Search */
    .search-result { display: flex; align-items: center; gap: 16px; padding: 16px; background-color: var(--surface); border-radius: var(--radius); margin-bottom: 12px; box-shadow: var(--shadow); }
    .search-result-icon { width: 48px; height: 48px; border-radius: 12px; background-color: var(--surface2); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: var(--accent); }
    .search-result-info { flex: 1; }
    .search-result-name { font-weight: bold; font-size: 1.125rem; }
    .search-result-meta { font-size: 0.875rem; color: var(--text2); }
    .search-result-price { font-weight: bold; font-size: 1.25rem; color: var(--teal); margin-right: 16px; }

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

    /* Notes */
    .note-card { background-color: var(--surface); border-radius: var(--radius); padding: 24px; margin-bottom: 16px; box-shadow: var(--shadow); }
    .note-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }
    .note-title { font-size: 1.25rem; }
    .note-body { color: var(--text2); margin-bottom: 16px; white-space: pre-wrap; }
    .note-meta { font-size: 0.875rem; color: var(--text3); font-weight: 500; }

    /* Budget */
    .invoice-header { background-color: var(--primary); color: var(--surface); border-radius: var(--radius); padding: 24px; position: relative; overflow: hidden; }
    .invoice-info { margin-top: 16px; }
    .invoice-details { background-color: var(--surface); border-radius: var(--radius); padding: 24px; box-shadow: var(--shadow); margin-top: 24px; }
    .invoice-totals { margin-top: 24px; padding-top: 24px; border-top: 2px solid var(--border); }
    .invoice-total-row { display: flex; justify-content: space-between; margin-bottom: 8px; font-weight: 500; }
    .invoice-total-row.grand-total { font-size: 1.25rem; font-weight: bold; color: var(--primary); margin-top: 12px; }
    .chart-container { width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(var(--accent) 0% 55%, var(--teal) 55% 96%, var(--surface3) 96% 100%); }

    /* Community */
    .community-card { background-color: var(--surface); border-radius: var(--radius); padding: 24px; margin-bottom: 24px; box-shadow: var(--shadow); }
    .community-header { display: flex; align-items: center; gap: 16px; margin-bottom: 16px; }
    .community-avatar { width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--surface); }
    .community-author { font-weight: bold; font-size: 1.125rem; }
    .community-content { margin-bottom: 16px; line-height: 1.6; }
    .community-footer { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); padding-top: 16px; color: var(--text3); }
    .community-actions { display: flex; gap: 16px; }
    .community-action { cursor: pointer; display: flex; align-items: center; gap: 6px; }
    .community-action:hover { color: var(--accent); }

    /* Profile */
    .profile-header { background-color: var(--surface); border-radius: var(--radius); padding: 32px; display: flex; align-items: center; gap: 32px; box-shadow: var(--shadow); margin-bottom: 32px; }
    .profile-avatar { width: 120px; height: 120px; border-radius: 50%; background-color: var(--primary); color: var(--surface); font-size: 2.5rem; display: flex; align-items: center; justify-content: center; font-weight: bold; }
    .profile-info { flex: 1; }
    .profile-stats { display: flex; gap: 24px; text-align: center; }
    .profile-stat-val { font-size: 1.5rem; font-weight: bold; color: var(--primary); }
    .profile-stat-label { font-size: 0.875rem; color: var(--text3); }

    /* Admin */
    .admin-tabs { display: flex; gap: 16px; margin-bottom: 24px; border-bottom: 1px solid var(--border); }
    .admin-tab { padding: 12px 24px; font-weight: bold; color: var(--text2); cursor: pointer; border-bottom: 3px solid transparent; }
    .admin-tab.active { color: var(--primary); border-bottom-color: var(--primary); }
    .admin-panel-content { display: none; }
    .stat-card { background-color: var(--surface); padding: 24px; border-radius: var(--radius); box-shadow: var(--shadow); display: flex; align-items: center; gap: 16px; }
    .stat-icon { width: 48px; height: 48px; border-radius: 12px; background-color: rgba(233, 69, 96, 0.1); color: var(--accent); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; }
    .stat-info { flex: 1; }
    .stat-label { font-size: 0.875rem; color: var(--text3); margin-bottom: 4px; }
    .stat-value { font-size: 1.5rem; font-weight: bold; color: var(--primary); }
    .stat-delta { font-size: 0.875rem; color: var(--teal); font-weight: bold; }
    .chart-bar { display: flex; align-items: center; margin-bottom: 12px; }
    .chart-bar-label { width: 100px; font-weight: 500; }
    .chart-bar-track { flex: 1; height: 24px; background-color: var(--surface2); border-radius: 12px; overflow: hidden; margin: 0 16px; }
    .chart-bar-fill { height: 100%; display: flex; align-items: center; padding-left: 12px; color: var(--surface); font-size: 0.75rem; font-weight: bold; }

    /* Toast */
    .toast-container { position: fixed; bottom: 24px; right: 24px; z-index: 9999; display: flex; flex-direction: column; gap: 12px; pointer-events: none; }
    .toast { background-color: var(--primary); color: var(--surface); padding: 12px 24px; border-radius: 8px; box-shadow: var(--shadow); display: flex; align-items: center; gap: 12px; opacity: 0; transform: translateY(20px); transition: all 0.3s; }
    .toast.show { opacity: 1; transform: translateY(0); }

    /* Animations */
    @keyframes fadeUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
    .screen.visible .card, .stat-card, .trip-card, .community-card { animation: fadeUp 0.4s ease-out forwards; }

    @media (max-width: 900px) {
      .sidebar { display: none !important; }
      body.logged-in .main { margin-left: 0; padding: 16px; margin-bottom: 60px; }
      body.logged-in .mobile-nav { display: flex; position: fixed; bottom: 0; left: 0; right: 0; height: 60px; background-color: var(--surface); box-shadow: 0 -2px 10px rgba(0,0,0,0.05); z-index: 100; justify-content: space-around; align-items: center; border-top: 1px solid var(--border); }
      .mobile-nav a { display: flex; flex-direction: column; align-items: center; color: var(--text3); font-size: 0.75rem; gap: 4px; cursor: pointer; }
      .mobile-nav a.active { color: var(--accent); }
      .mobile-nav a i { font-size: 1.25rem; }
      .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
    }
    @media (min-width: 601px) and (max-width: 900px) {
      .grid-2 { grid-template-columns: repeat(2, 1fr); }
      .grid-3 { grid-template-columns: repeat(2, 1fr); }
      .grid-4 { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .topbar-search { display: none; }
      .screen-header { flex-direction: column; align-items: flex-start; gap: 16px; }
    }
  </style>
</head>
<body>

  <!-- Toast Container -->
  <div class="toast-container" id="toast-container"></div>

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
      <a class="sidebar-link active" onclick="showScreen('home')"><i class="fas fa-home"></i> Home</a>
      <a class="sidebar-link" onclick="showScreen('trips')"><i class="fas fa-map-marked-alt"></i> My Trips <span class="badge badge-accent" style="background:var(--accent);color:white;margin-left:auto">3</span></a>
      <a class="sidebar-link" onclick="showScreen('plan')"><i class="fas fa-plus-circle"></i> Plan a Trip</a>
      <a class="sidebar-link" onclick="showScreen('itinerary')"><i class="fas fa-calendar-alt"></i> Itinerary</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Tools</div>
      <a class="sidebar-link" onclick="showScreen('search')"><i class="fas fa-search"></i> Activity Search</a>
      <a class="sidebar-link" onclick="showScreen('checklist')"><i class="fas fa-check-square"></i> Packing List</a>
      <a class="sidebar-link" onclick="showScreen('notes')"><i class="fas fa-sticky-note"></i> Trip Notes</a>
      <a class="sidebar-link" onclick="showScreen('budget')"><i class="fas fa-file-invoice-dollar"></i> Expenses</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Discover</div>
      <a class="sidebar-link" onclick="showScreen('community')"><i class="fas fa-users"></i> Community</a>
      <a class="sidebar-link" onclick="showScreen('profile')"><i class="fas fa-user-circle"></i> Profile</a>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-section-title">Admin</div>
      <a class="sidebar-link" onclick="showScreen('admin')"><i class="fas fa-cog"></i> Admin Panel</a>
    </div>
  </div>

  <!-- Mobile Bottom Nav -->
  <div class="mobile-nav">
    <a class="active" onclick="showScreen('home')"><i class="fas fa-home"></i> Home</a>
    <a onclick="showScreen('trips')"><i class="fas fa-map-marked-alt"></i> Trips</a>
    <a onclick="showScreen('checklist')"><i class="fas fa-check-square"></i> Packing</a>
    <a onclick="showScreen('community')"><i class="fas fa-users"></i> Community</a>
    <a onclick="showScreen('profile')"><i class="fas fa-user-circle"></i> Profile</a>
  </div>

  <div class="main">
    
    <!-- Screen 1: Login / Signup -->
    <div id="screen-login" class="screen visible">
      <div style="text-align:center; color:white; margin-bottom:24px;">
        <h2 style="color:white; margin-bottom:8px;">Where do you want to explore?</h2>
        <div class="trip-type-selector" style="display:inline-flex; width: 100%; max-width: 400px; background:rgba(255,255,255,0.2); backdrop-filter:blur(10px);">
          <button class="btn trip-type-btn active" data-type="india" onclick="switchTripType('india')">India Trip</button>
          <button class="btn trip-type-btn" data-type="intl" onclick="switchTripType('intl')">International Trip</button>
        </div>
      </div>
      <div class="card auth-card">
        <div class="auth-logo">Traveloop <div class="dot"></div></div>
        <div class="auth-tabs">
          <div class="auth-tab active" id="login-tab" onclick="toggleAuthTab('login')">Login</div>
          <div class="auth-tab" id="signup-tab" onclick="toggleAuthTab('signup')">Sign Up</div>
        </div>
        <form id="login-form" onsubmit="handleAuth(event)">
          <div class="input-group">
            <label class="label">Email Address</label>
            <input type="email" class="input" placeholder="name@example.com" required>
          </div>
          <div class="input-group">
            <label class="label">Password</label>
            <input type="password" class="input" placeholder="••••••••" required>
          </div>
          <div style="text-align: right; margin-bottom: 24px;">
            <a href="#" class="text-small" style="color: var(--accent);">Forgot Password?</a>
          </div>
          <button type="submit" class="btn btn-primary" style="width: 100%">Login</button>
        </form>
        <form id="signup-form" style="display: none;" onsubmit="handleAuth(event, true)">
          <div class="input-group">
            <label class="label">Full Name</label>
            <input type="text" class="input" placeholder="James Arjun" required>
          </div>
          <div class="input-group">
            <label class="label">Email Address</label>
            <input type="email" class="input" placeholder="name@example.com" required>
          </div>
          <div class="input-group">
            <label class="label">Password</label>
            <input type="password" class="input" placeholder="••••••••" required>
          </div>
          <div class="input-group">
            <label class="label">Confirm Password</label>
            <input type="password" class="input" placeholder="••••••••" required>
          </div>
          <button type="submit" class="btn btn-accent" style="width: 100%; margin-top: 8px;">Sign Up</button>
        </form>
      </div>
    </div>

    <!-- Screen 3: Home -->
    <div id="screen-home" class="screen">
      <div class="banner">
        <h2>Plan your next unforgettable journey</h2>
        <p class="trip-mode india-mode">From royal palaces to Himalayan adventures.</p>
        <p class="trip-mode intl-mode" style="display:none;">Explore beautiful destinations across the globe.</p>
        <div class="banner-actions">
          <button class="btn banner-btn" onclick="showModal('plan-trip-modal')">Plan a Trip</button>
          <button class="btn banner-btn-outline" onclick="showScreen('community')">Explore Community</button>
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
        <div class="dest-card"><div class="dest-thumb">🇯🇵</div><div class="dest-label">Tokyo</div><div class="dest-sublabel">★4.8 · Japan</div></div>
        <div class="dest-card"><div class="dest-thumb">🇮🇩</div><div class="dest-label">Bali</div><div class="dest-sublabel">★4.7 · Indonesia</div></div>
      </div>

      <h3 class="card-title" style="margin-bottom: 16px;">Previous Trips</h3>
      <div class="grid-3 trip-mode india-mode">
        <div class="trip-card">
          <div class="trip-card-img" style="background: linear-gradient(135deg, var(--primary), var(--accent2));"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Rajasthan Heritage Trail</div>
            <div class="trip-card-meta">Jun 2025 · <span class="badge badge-gray">Completed</span></div>
            <div class="trip-card-meta"><i class="fas fa-user-friends"></i> 4 Travelers</div>
          </div>
          <div class="trip-card-footer"><span style="color:var(--text2)">Total Cost</span><span style="color:var(--primary)">₹42,000</span></div>
        </div>
        <div class="trip-card">
          <div class="trip-card-img" style="background: linear-gradient(135deg, var(--teal), var(--primary));"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Goa Escape</div>
            <div class="trip-card-meta">May 2026 · <span class="badge badge-green">Ongoing</span></div>
            <div class="trip-card-meta"><i class="fas fa-user-friends"></i> 2 Travelers</div>
          </div>
          <div class="trip-card-footer"><span style="color:var(--text2)">Current Cost</span><span style="color:var(--primary)">₹18,400</span></div>
        </div>
        <div class="trip-card">
          <div class="trip-card-img" style="background: linear-gradient(135deg, var(--accent2), #ff7e5f);"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Kerala Wellness Retreat</div>
            <div class="trip-card-meta">Aug 2026 · <span class="badge badge-amber">Upcoming</span></div>
            <div class="trip-card-meta"><i class="fas fa-user"></i> 1 Traveler</div>
          </div>
          <div class="trip-card-footer"><span style="color:var(--text2)">Budget</span><span style="color:var(--primary)">₹32,000</span></div>
        </div>
      </div>
      <div class="grid-3 trip-mode intl-mode" style="display:none;">
        <div class="trip-card">
          <div class="trip-card-img" style="background: linear-gradient(135deg, var(--primary), var(--accent2));"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Paris & Rome Adventure</div>
            <div class="trip-card-meta">Jun 2025 · <span class="badge badge-gray">Completed</span></div>
            <div class="trip-card-meta"><i class="fas fa-user-friends"></i> 4 Travelers</div>
          </div>
          <div class="trip-card-footer"><span style="color:var(--text2)">Total Cost</span><span style="color:var(--primary)">$22,000</span></div>
        </div>
        <div class="trip-card">
          <div class="trip-card-img" style="background: linear-gradient(135deg, var(--teal), var(--primary));"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Tokyo Highlights</div>
            <div class="trip-card-meta">May 2026 · <span class="badge badge-green">Ongoing</span></div>
            <div class="trip-card-meta"><i class="fas fa-user-friends"></i> 2 Travelers</div>
          </div>
          <div class="trip-card-footer"><span style="color:var(--text2)">Current Cost</span><span style="color:var(--primary)">$8,400</span></div>
        </div>
        <div class="trip-card">
          <div class="trip-card-img" style="background: linear-gradient(135deg, var(--accent2), #ff7e5f);"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">Bali Wellness Retreat</div>
            <div class="trip-card-meta">Aug 2026 · <span class="badge badge-amber">Upcoming</span></div>
            <div class="trip-card-meta"><i class="fas fa-user"></i> 1 Traveler</div>
          </div>
          <div class="trip-card-footer"><span style="color:var(--text2)">Budget</span><span style="color:var(--primary)">$3,200</span></div>
        </div>
      </div>
    </div>

    <!-- Screen 6: My Trips -->
    <div id="screen-trips" class="screen">
      <div class="screen-header">
        <h1>My Trips</h1>
        <button class="btn btn-primary" onclick="showModal('plan-trip-modal')"><i class="fas fa-plus"></i> New Trip</button>
      </div>

      <!-- India Trips -->
      <div class="trip-mode india-mode">
        <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-green">Ongoing</span><h3 style="margin:0">Goa Escape</h3></div>
        <div class="card" style="margin-bottom:32px">
          <div class="card-header">
            <div><div style="font-weight:bold; margin-bottom:4px">May 1-8 2026</div><div style="color:var(--text2)">Day 4 of 8</div></div>
            <button class="btn btn-teal btn-sm" onclick="showScreen('itinerary')">View Details</button>
          </div>
          <div class="progress-bar"><div class="progress-fill teal" style="width: 60%"></div></div>
        </div>
        <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-amber">Upcoming</span><h3 style="margin:0">Kerala Retreat</h3></div>
        <div class="card" style="margin-bottom:32px">
          <div class="card-header" style="margin:0">
            <div><div style="font-weight:bold; margin-bottom:4px">Aug 10-17 2026</div><div style="color:var(--text2)">Budget ₹32,000</div></div>
            <button class="btn btn-primary btn-sm" onclick="showScreen('itinerary')">Manage Trip</button>
          </div>
        </div>
        <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-gray">Completed</span><h3 style="margin:0">Past Journeys</h3></div>
        <div class="grid-2">
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Rajasthan Heritage Trail</div><div class="trip-card-meta">Jun 2025</div></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Manali Snow Trip</div><div class="trip-card-meta">Dec 2024</div></div></div>
        </div>
      </div>
      
      <!-- Intl Trips -->
      <div class="trip-mode intl-mode" style="display:none;">
        <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-green">Ongoing</span><h3 style="margin:0">Tokyo Highlights</h3></div>
        <div class="card" style="margin-bottom:32px">
          <div class="card-header">
            <div><div style="font-weight:bold; margin-bottom:4px">May 1-8 2026</div><div style="color:var(--text2)">Day 4 of 8</div></div>
            <button class="btn btn-teal btn-sm" onclick="showScreen('itinerary')">View Details</button>
          </div>
          <div class="progress-bar"><div class="progress-fill teal" style="width: 60%"></div></div>
        </div>
        <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-amber">Upcoming</span><h3 style="margin:0">Bali Wellness Retreat</h3></div>
        <div class="card" style="margin-bottom:32px">
          <div class="card-header" style="margin:0">
            <div><div style="font-weight:bold; margin-bottom:4px">Aug 10-17 2026</div><div style="color:var(--text2)">Budget $3,200</div></div>
            <button class="btn btn-primary btn-sm" onclick="showScreen('itinerary')">Manage Trip</button>
          </div>
        </div>
        <div style="margin: 32px 0 16px 0; display:flex; align-items:center; gap:12px;"><span class="badge badge-gray">Completed</span><h3 style="margin:0">Past Journeys</h3></div>
        <div class="grid-2">
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Paris & Rome</div><div class="trip-card-meta">Jun 2025</div></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">London Winter</div><div class="trip-card-meta">Dec 2024</div></div></div>
        </div>
      </div>
    </div>

    <!-- Screen 4: Plan a Trip -->
    <div id="screen-plan" class="screen">
      <div class="screen-header"><h1>Create Trip</h1></div>
      <div class="grid-2">
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 24px;">Trip Details</h3>
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
          <div class="input-group">
            <label class="label">Select a Place</label>
            <select class="select trip-mode india-mode">
              <option>Jaipur, Rajasthan</option><option>Goa, India</option><option>Munnar, Kerala</option><option>Leh, Ladakh</option>
            </select>
            <select class="select trip-mode intl-mode" style="display:none;">
              <option>Paris, France</option><option>Rome, Italy</option><option>Tokyo, Japan</option><option>Bali, Indonesia</option>
            </select>
          </div>
          <div class="form-grid">
            <div class="input-group"><label class="label">Number of Travelers</label><input type="number" class="input" value="2"></div>
            <div class="input-group"><label class="label">Total Budget (<span class="currency-symbol">₹</span>)</label><input type="number" class="input" value="5000"></div>
          </div>
          <div class="input-group"><label class="label">Trip Notes</label><textarea class="input" rows="3" placeholder="Any special requirements..."></textarea></div>
          <div style="display:flex; gap:16px; margin-top:24px;">
            <button class="btn btn-primary" style="flex:1" onclick="showScreen('itinerary')">Build Itinerary</button>
            <button class="btn" style="flex:1; border:1px solid var(--border)" onclick="showScreen('home')">Cancel</button>
          </div>
        </div>
        <div>
          <div class="card" style="margin-bottom: 24px;">
            <h3 class="card-title" style="margin-bottom: 16px;">Suggested Places to Visit</h3>
            <div class="grid-3 trip-mode india-mode">
              <div class="dest-card"><div class="dest-thumb">🕌</div><div class="dest-label">Taj Mahal</div></div>
              <div class="dest-card"><div class="dest-thumb">🏯</div><div class="dest-label">Hawa Mahal</div></div>
              <div class="dest-card"><div class="dest-thumb">🛕</div><div class="dest-label">Golden Temple</div></div>
              <div class="dest-card"><div class="dest-thumb">🛶</div><div class="dest-label">Backwaters Kerala</div></div>
              <div class="dest-card"><div class="dest-thumb">🏍️</div><div class="dest-label">Leh Roads</div></div>
              <div class="dest-card"><div class="dest-thumb">🏜️</div><div class="dest-label">Rann of Kutch</div></div>
            </div>
            <div class="grid-3 trip-mode intl-mode" style="display:none;">
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
            <div style="display:flex; flex-wrap:wrap;" class="trip-mode india-mode">
              <span class="chip active" onclick="this.classList.toggle('active')">Camel Safari</span>
              <span class="chip" onclick="this.classList.toggle('active')">Temple Visit</span>
              <span class="chip active" onclick="this.classList.toggle('active')">River Rafting</span>
              <span class="chip" onclick="this.classList.toggle('active')">Beach Party</span>
              <span class="chip" onclick="this.classList.toggle('active')">Tea Garden Tour</span>
              <span class="chip" onclick="this.classList.toggle('active')">Houseboat Stay</span>
              <span class="chip" onclick="this.classList.toggle('active')">Photography</span>
              <span class="chip active" onclick="this.classList.toggle('active')">Trekking</span>
            </div>
            <div style="display:flex; flex-wrap:wrap; display:none;" class="trip-mode intl-mode">
              <span class="chip active" onclick="this.classList.toggle('active')">Art & Culture</span>
              <span class="chip" onclick="this.classList.toggle('active')">Food & Dining</span>
              <span class="chip active" onclick="this.classList.toggle('active')">Walking Tours</span>
              <span class="chip" onclick="this.classList.toggle('active')">Water Sports</span>
              <span class="chip" onclick="this.classList.toggle('active')">Adventure</span>
              <span class="chip" onclick="this.classList.toggle('active')">Photography</span>
              <span class="chip" onclick="this.classList.toggle('active')">Theatre</span>
              <span class="chip" onclick="this.classList.toggle('active')">Shopping</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Screen 5 & 9: Itinerary Builder / View -->
    <div id="screen-itinerary" class="screen">
      <div class="screen-header" style="margin-bottom:8px">
        <h1>Itinerary</h1>
        <div style="display:flex; gap:8px;">
          <button class="btn btn-primary btn-sm" onclick="addItinerarySection()">+ Add Section</button>
          <button class="btn btn-accent btn-sm" onclick="showScreen('budget')">View Budget</button>
        </div>
      </div>
      <p class="trip-mode india-mode" style="color:var(--text2); margin-bottom:24px">Rajasthan Royal Journey · Dec 15-22</p>
      <p class="trip-mode intl-mode" style="color:var(--text2); margin-bottom:24px; display:none;">Paris & Rome Adventure · Jun 15-26</p>
      <div style="margin-bottom: 24px;"><span class="badge badge-amber">Physical & Cultural</span></div>
      
      <div class="grid-2 trip-mode india-mode">
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 24px;">Build Itinerary</h3>
          <div id="itinerary-sections-container-india" style="border-left: 2px solid var(--border); padding-left: 24px; margin-left: 12px;">
            <div style="position:relative; margin-bottom: 32px;">
              <div style="position:absolute; left:-31px; top:0; width:16px; height:16px; border-radius:50%; background:var(--accent);"></div>
              <div style="font-weight:bold; font-size:1.125rem">Section 1: Jaipur Stay</div>
              <div style="color:var(--text2); font-size:0.875rem; margin-bottom:8px">Hawa Mahal / Amer Fort / Hotel</div>
              <div class="badge badge-teal" style="background:rgba(22,199,154,0.1); color:var(--teal)">Budget ₹12,000</div>
            </div>
            <div style="position:relative; margin-bottom: 32px;">
              <div style="position:absolute; left:-31px; top:0; width:16px; height:16px; border-radius:50%; background:var(--accent2);"></div>
              <div style="font-weight:bold; font-size:1.125rem">Section 2: Travel to Udaipur</div>
              <div style="color:var(--text2); font-size:0.875rem; margin-bottom:8px">Train + Taxi</div>
              <div class="badge badge-teal" style="background:rgba(22,199,154,0.1); color:var(--teal)">Budget ₹5,000</div>
            </div>
            <div style="position:relative; margin-bottom: 16px;">
              <div style="position:absolute; left:-31px; top:0; width:16px; height:16px; border-radius:50%; background:var(--primary);"></div>
              <div style="font-weight:bold; font-size:1.125rem">Section 3: Udaipur Stay</div>
              <div style="color:var(--text2); font-size:0.875rem; margin-bottom:8px">Lake Pichola / City Palace</div>
              <div class="badge badge-teal" style="background:rgba(22,199,154,0.1); color:var(--teal)">Budget ₹10,000</div>
            </div>
          </div>
        </div>
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 24px;">Day-by-Day View</h3>
          <div class="day-block">
            <div class="day-label">Day 1 Dec 15</div>
            <div class="itinerary-item">
              <div class="itinerary-time">09:00</div>
              <div class="itinerary-content"><h4>Flight AMD→JAI</h4></div>
              <div class="itinerary-budget">₹3,500</div>
            </div>
            <div class="itinerary-item">
              <div class="itinerary-time">18:00</div>
              <div class="itinerary-content"><h4>Hotel Check-in</h4></div>
              <div class="itinerary-budget">₹2,000</div>
            </div>
          </div>
          <div class="day-block">
            <div class="day-label">Day 2 Dec 16</div>
            <div class="itinerary-item"><div class="itinerary-time">09:30</div><div class="itinerary-content"><h4>Amer Fort</h4></div><div class="itinerary-budget">₹500</div></div>
            <div class="itinerary-item"><div class="itinerary-time">14:00</div><div class="itinerary-content"><h4>Hawa Mahal</h4></div><div class="itinerary-budget">₹200</div></div>
            <div class="itinerary-item"><div class="itinerary-time">18:00</div><div class="itinerary-content"><h4>Local Market</h4></div><div class="itinerary-budget">₹1,000</div></div>
          </div>
        </div>
      </div>

      <div class="grid-2 trip-mode intl-mode" style="display:none;">
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 24px;">Build Itinerary</h3>
          <div id="itinerary-sections-container-intl" style="border-left: 2px solid var(--border); padding-left: 24px; margin-left: 12px;">
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
              <div class="itinerary-content"><h4>Flight DEL→PAR</h4><p>Air France AF225</p></div>
              <div class="itinerary-budget">$3,000</div>
            </div>
            <div class="itinerary-item">
              <div class="itinerary-time">19:30</div>
              <div class="itinerary-content"><h4>Hotel Check-in</h4><p>The Paris Hotel</p></div>
              <div class="itinerary-budget">$900/n</div>
            </div>
          </div>
          <div class="day-block">
            <div class="day-label">Day 2 Jun 16</div>
            <div class="itinerary-item"><div class="itinerary-time">09:00</div><div class="itinerary-content"><h4>Eiffel Tower</h4></div><div class="itinerary-budget">$120</div></div>
            <div class="itinerary-item"><div class="itinerary-time">14:00</div><div class="itinerary-content"><h4>Louvre</h4></div><div class="itinerary-budget">$80</div></div>
            <div class="itinerary-item"><div class="itinerary-time">20:00</div><div class="itinerary-content"><h4>Seine Cruise</h4></div><div class="itinerary-budget">$200</div></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Screen 8: Activity / City Search -->
    <div id="screen-search" class="screen">
      <div class="screen-header"><h1>Activity Search</h1></div>
      <div class="card" style="margin-bottom: 24px;">
        <div style="display:flex; gap:16px; margin-bottom:24px;">
          <input type="text" class="input" placeholder="Search for activities..." style="flex:1" id="search-input" value="Adventure">
          <select class="select" style="width: 200px;"><option>All Categories</option><option>Adventure</option><option>Culture</option></select>
          <button class="btn btn-primary" onclick="runSearch()">Search</button>
        </div>
        <div style="display:flex; flex-wrap:wrap; margin-bottom:16px" class="trip-mode india-mode">
          <span class="chip active">River Rafting</span><span class="chip">Camel Safari</span><span class="chip">Trekking</span>
          <span class="chip">Scuba Diving</span><span class="chip">Houseboat</span><span class="chip">Paragliding</span>
        </div>
        <div style="display:flex; flex-wrap:wrap; margin-bottom:16px; display:none;" class="trip-mode intl-mode">
          <span class="chip active">Paragliding</span><span class="chip">Hiking</span><span class="chip">Food Tour</span>
          <span class="chip">Museum</span><span class="chip">Beach</span><span class="chip">Cycling</span>
        </div>
        <div id="search-result-label" style="font-weight:bold; color:var(--primary)">Showing 7 results for "Adventure"</div>
      </div>
      <div id="search-results-container"></div>
    </div>

    <!-- Screen 11: Packing Checklist -->
    <div id="screen-checklist" class="screen">
      <div class="screen-header">
        <div><h1 style="margin-bottom:8px">Packing Checklist</h1><p style="color:var(--text2)">Trip Essentials</p></div>
        <div style="display:flex;gap:16px"><button class="btn btn-sm" style="border:1px solid var(--border)" onclick="resetChecklist()">Reset All</button></div>
      </div>
      <div class="card" style="margin-bottom: 24px; display:flex; align-items:center; gap:24px">
        <div style="flex:1">
          <div style="display:flex; justify-content:space-between; margin-bottom:8px"><span style="font-weight:bold" id="progress-text">5 / 12 items packed</span><span class="badge badge-amber">Almost there</span></div>
          <div class="progress-bar"><div class="progress-fill teal" id="progress-fill" style="width: 42%"></div></div>
        </div>
      </div>
      <div class="grid-2">
        <div id="check-left-col">
          <div class="checklist-group" data-group="Documents">
            <div class="checklist-group-header"><span>Documents</span><span style="color:var(--text3)" class="group-count">3/4</span></div>
            <div class="checklist-items">
              <div class="check-item checked" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-check-square"></i></div><span>Passport</span></div>
              <div class="check-item checked trip-mode india-mode" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-check-square"></i></div><span>Aadhaar Card</span></div>
              <div class="check-item checked trip-mode intl-mode" onclick="toggleCheck(this)" style="display:none;"><div class="check-box"><i class="far fa-check-square"></i></div><span>Visa</span></div>
              <div class="check-item checked trip-mode india-mode" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-check-square"></i></div><span>Train Tickets</span></div>
              <div class="check-item checked trip-mode intl-mode" onclick="toggleCheck(this)" style="display:none;"><div class="check-box"><i class="far fa-check-square"></i></div><span>Flight Tickets</span></div>
              <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Hotel Booking</span></div>
            </div>
          </div>
          <div class="checklist-group" data-group="Clothing">
            <div class="checklist-group-header"><span>Clothing</span><span style="color:var(--text3)" class="group-count">1/4</span></div>
            <div class="checklist-items">
              <div class="check-item checked" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-check-square"></i></div><span>Casual Shirts</span></div>
              <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Trousers</span></div>
              <div class="check-item trip-mode india-mode" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Traditional Wear</span></div>
              <div class="check-item trip-mode intl-mode" onclick="toggleCheck(this)" style="display:none;"><div class="check-box"><i class="far fa-square"></i></div><span>Walking Shoes</span></div>
              <div class="check-item trip-mode india-mode" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Trekking Shoes</span></div>
              <div class="check-item trip-mode intl-mode" onclick="toggleCheck(this)" style="display:none;"><div class="check-box"><i class="far fa-square"></i></div><span>Light Jacket</span></div>
            </div>
          </div>
        </div>
        <div id="check-right-col">
          <div class="checklist-group" data-group="Electronics">
            <div class="checklist-group-header"><span>Electronics</span><span style="color:var(--text3)" class="group-count">1/3</span></div>
            <div class="checklist-items">
              <div class="check-item checked trip-mode india-mode" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-check-square"></i></div><span>Power Bank</span></div>
              <div class="check-item checked trip-mode intl-mode" onclick="toggleCheck(this)" style="display:none;"><div class="check-box"><i class="far fa-check-square"></i></div><span>Phone Charger</span></div>
              <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Power Adapter</span></div>
              <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Earphones</span></div>
            </div>
          </div>
          <div class="checklist-group" data-group="Health & Hygiene">
            <div class="checklist-group-header"><span>Health & Hygiene</span><span style="color:var(--text3)" class="group-count">0/3</span></div>
            <div class="checklist-items">
              <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Medicines</span></div>
              <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>Sunscreen</span></div>
              <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><i class="far fa-square"></i></div><span>First Aid Kit</span></div>
            </div>
          </div>
          <button class="btn btn-primary" style="width:100%" onclick="showModal('add-item-modal')">+ Add Item to Checklist</button>
        </div>
      </div>
    </div>

    <!-- Screen 13: Trip Notes -->
    <div id="screen-notes" class="screen">
      <div class="screen-header">
        <h1>Trip Notes & Journal</h1>
        <button class="btn btn-accent" onclick="showModal('add-note-modal')"><i class="fas fa-plus"></i> Add Note</button>
      </div>
      <div id="notes-container" class="trip-mode india-mode">
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">Jaipur Hotel Check-in Details</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">Check in after 2pm. Beautiful heritage hotel near Hawa Mahal. Make sure to present booking confirmation #1920X.</p>
          <div class="note-meta">Day 1 · Dec 15, 2026 · Jaipur</div>
        </div>
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">Best Cafes in Udaipur</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">Ambrai Restaurant for dinner. Try to get a lakeside table! Jheel's Ginger Coffee Bar for morning views.</p>
          <div class="note-meta">Day 3 · Dec 17, 2026 · Udaipur</div>
        </div>
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">Leh Oxygen Tips</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">Drink plenty of water. Rest on day 1 to acclimatize. Don't exert too much physically immediately after landing.</p>
          <div class="note-meta">General Tip</div>
        </div>
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">Kerala Houseboat Timing</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">Check-in exactly at 12 PM in Alleppey. Food is provided onboard. Don't miss the sunset.</p>
          <div class="note-meta">Kerala Retreat</div>
        </div>
      </div>
      
      <div id="notes-container-intl" class="trip-mode intl-mode" style="display:none;">
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">Hotel Check-in Details – Rome Stop</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">Check in after 2pm, Room 302, Breakfast included 7-10am. Make sure to present booking confirmation #1920X.</p>
          <div class="note-meta">Day 3 · June 19, 2025 · Rome</div>
        </div>
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">Best restaurants near Colosseum</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">Osteria Barberini – try the cacio e pepe. Book in advance! Also check out Trattoria Luzzi for good wood-fired pizza.</p>
          <div class="note-meta">Day 5 · June 21, 2025 · Rome</div>
        </div>
        <div class="note-card">
          <div class="note-header"><h3 class="note-title">Louvre Tips – Paris Stop</h3><div class="note-actions"><button class="btn-icon" style="color: var(--accent)" onclick="this.closest('.note-card').remove(); showToast('Note deleted')"><i class="fas fa-trash"></i></button></div></div>
          <p class="note-body">Enter through Richelieu wing to avoid crowds. Mona Lisa Level 1. Remember comfortable walking shoes.</p>
          <div class="note-meta">Day 2 · June 16, 2025 · Paris</div>
        </div>
      </div>
    </div>

    <!-- Screen 14: Expense Invoice -->
    <div id="screen-budget" class="screen">
      <div class="screen-header"><h1>Expense & Invoice</h1></div>
      
      <div class="trip-mode india-mode">
        <div class="grid-2">
          <div class="invoice-header">
            <div style="font-size: 2rem; margin-bottom: 8px;">🗺️</div>
            <h2>Trip to Rajasthan Adventure</h2>
            <div class="invoice-info"><p>May 15 - May 22 2026</p><p>Jaipur, Jodhpur, Udaipur, Jaisalmer · Created by James Arjun</p><p><i class="fas fa-user-friends"></i> 4 Travelers</p></div>
            <div style="margin-top: 16px;"><span class="badge badge-amber" style="background:rgba(255,255,255,0.2);color:white">Payment Pending</span></div>
            <div style="position:absolute; top:24px; right:24px; font-family:var(--font-mono); font-size:0.875rem; color:rgba(255,255,255,0.7)">INV-xyz-30290</div>
          </div>
          <div class="card">
            <h3 class="card-title" style="margin-bottom:16px">Budget Insights</h3>
            <div style="display:flex; align-items:center; gap:24px">
              <div class="chart-container"></div>
              <div style="flex:1">
                <div style="margin-bottom:8px"><span style="color:var(--text2)">Total Budget:</span> <strong>₹40,000</strong></div>
                <div style="margin-bottom:8px"><span style="color:var(--text2)">Total Spent:</span> <strong style="color:var(--accent)">₹43,500</strong></div>
                <div style="margin-bottom:16px"><span style="color:var(--text2)">Remaining:</span> <strong style="color:var(--accent)">-₹3,500</strong></div>
              </div>
            </div>
          </div>
        </div>
        <div class="invoice-details">
          <div style="overflow-x:auto;">
            <table class="data-table">
              <thead><tr><th>Category</th><th>Description</th><th>Qty</th><th>Unit Cost</th><th style="text-align:right">Amount</th></tr></thead>
              <tbody>
                <tr><td><span class="badge badge-blue">Hotel</span></td><td>Hotel Jaipur 3 Nights</td><td>3 nights</td><td>₹3,000</td><td style="text-align:right">₹9,000</td></tr>
                <tr><td><span class="badge badge-pink">Travel</span></td><td>Train Jaipur→Jodhpur</td><td>4 tickets</td><td>₹800</td><td style="text-align:right">₹3,200</td></tr>
                <tr><td><span class="badge badge-green">Activity</span></td><td>Desert Safari</td><td>4 persons</td><td>₹1,000</td><td style="text-align:right">₹4,000</td></tr>
                <tr><td><span class="badge badge-gray">Food</span></td><td>Meals</td><td>4 persons</td><td>-</td><td style="text-align:right">₹5,500</td></tr>
              </tbody>
            </table>
          </div>
          <div class="invoice-totals" style="width:300px; margin-left:auto">
            <div class="invoice-total-row"><span>Subtotal</span><span>₹21,700</span></div>
            <div class="invoice-total-row"><span>Tax 5%</span><span>₹1,085</span></div>
            <div class="invoice-total-row"><span>Discount</span><span>-₹285</span></div>
            <div class="invoice-total-row grand-total"><span>Grand Total</span><span>₹22,500</span></div>
          </div>
        </div>
      </div>
      
      <div class="trip-mode intl-mode" style="display:none;">
        <div class="grid-2">
          <div class="invoice-header">
            <div style="font-size: 2rem; margin-bottom: 8px;">🗺️</div>
            <h2>Trip to Europe Adventure</h2>
            <div class="invoice-info"><p>May 15 - Jun 05 2025</p><p>4 cities · Created by James</p><p><i class="fas fa-user-friends"></i> 4 Travelers</p></div>
            <div style="margin-top: 16px;"><span class="badge badge-amber" style="background:rgba(255,255,255,0.2);color:white">Payment Pending</span></div>
            <div style="position:absolute; top:24px; right:24px; font-family:var(--font-mono); font-size:0.875rem; color:rgba(255,255,255,0.7)">INV-xyz-30290</div>
          </div>
          <div class="card">
            <h3 class="card-title" style="margin-bottom:16px">Budget Insights</h3>
            <div style="display:flex; align-items:center; gap:24px">
              <div class="chart-container"></div>
              <div style="flex:1">
                <div style="margin-bottom:8px"><span style="color:var(--text2)">Total Budget:</span> <strong>$20,000</strong></div>
                <div style="margin-bottom:8px"><span style="color:var(--text2)">Total Spent:</span> <strong style="color:var(--accent)">$22,000</strong></div>
                <div style="margin-bottom:16px"><span style="color:var(--text2)">Remaining:</span> <strong style="color:var(--accent)">-$2,000</strong></div>
              </div>
            </div>
          </div>
        </div>
        <div class="invoice-details">
          <div style="overflow-x:auto;">
            <table class="data-table">
              <thead><tr><th>Category</th><th>Description</th><th>Qty</th><th>Unit Cost</th><th style="text-align:right">Amount</th></tr></thead>
              <tbody>
                <tr><td><span class="badge badge-blue">Hotel</span></td><td>Hotel Booking Paris 3 nights</td><td>3 nights</td><td>$3,000</td><td style="text-align:right">$9,000</td></tr>
                <tr><td><span class="badge badge-pink">Travel</span></td><td>Flight DEL→PAR</td><td>4 tickets</td><td>$3,000</td><td style="text-align:right">$12,000</td></tr>
                <tr><td><span class="badge badge-green">Activity</span></td><td>Guided Tours & Entrances</td><td>4 persons</td><td>$250</td><td style="text-align:right">$1,000</td></tr>
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
      </div>

      <div style="display:flex; justify-content:flex-end; gap:16px; margin-top:24px">
        <button class="btn" style="border:1px solid var(--border)" onclick="showToast('Invoice Downloaded')"><i class="fas fa-download"></i> Download Invoice</button>
        <button class="btn" style="border:1px solid var(--border)" onclick="showToast('PDF Exported')"><i class="fas fa-file-pdf"></i> Export as PDF</button>
        <button class="btn btn-teal" onclick="showToast('Marked as Paid')">Mark as Paid</button>
      </div>
    </div>

    <!-- Screen 10: Community -->
    <div id="screen-community" class="screen">
      <div class="screen-header"><h1>Community</h1><button class="btn btn-accent"><i class="fas fa-pen"></i> Write a Post</button></div>
      <div class="grid-2 trip-mode india-mode">
        <div class="community-card">
          <div class="community-header"><div class="community-avatar" style="background-color: var(--accent);">MR</div><div><div class="community-author">Mrudul Mistri <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div><div style="font-size:0.875rem; color:var(--text3)">2 days ago</div></div></div>
          <div class="community-content">The sunset at the Rann of Kutch is simply breathtaking! The white salt desert stretching to infinity is a must-see. Highly recommend visiting during the Rann Utsav. 🏜️✨</div>
          <div style="margin-bottom:16px"><span class="badge badge-gray">India</span><span class="badge badge-gray">Rajasthan</span><span class="badge badge-gray">Solo</span></div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action" onclick="likePost(this)"><i class="far fa-heart"></i> <span>142</span></div>
              <div class="community-action"><i class="far fa-comment"></i> 28</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>
        <div class="community-card">
          <div class="community-header"><div class="community-avatar" style="background-color: var(--teal);">YZ</div><div><div class="community-author">Yuvraj Zende <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div><div style="font-size:0.875rem; color:var(--text3)">5 days ago</div></div></div>
          <div class="community-content">Goa during monsoon is a completely different vibe! Lush green, fewer crowds, and stunning waterfalls. Don't skip Dudhsagar trek! 🌴🌧️</div>
          <div style="margin-bottom:16px"><span class="badge badge-gray">India</span><span class="badge badge-gray">Goa</span><span class="badge badge-gray">Adventure</span></div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action" onclick="likePost(this)"><i class="far fa-heart"></i> <span>89</span></div>
              <div class="community-action"><i class="far fa-comment"></i> 15</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>
        <div class="community-card">
          <div class="community-header"><div class="community-avatar" style="background-color: var(--primary);">SK</div><div><div class="community-author">Sakthi K <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div><div style="font-size:0.875rem; color:var(--text3)">1 week ago</div></div></div>
          <div class="community-content">Just finished a 5-day food trail in Kerala. From appam with stew to karimeen pollichathu, every meal was a 10/10. God's own country indeed! 🍛🛶</div>
          <div style="margin-bottom:16px"><span class="badge badge-gray">Kerala</span><span class="badge badge-gray">Food</span></div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action" onclick="likePost(this)"><i class="far fa-heart"></i> <span>214</span></div>
              <div class="community-action"><i class="far fa-comment"></i> 41</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>
        <div class="community-card">
          <div class="community-header"><div class="community-avatar" style="background-color: var(--accent2);">HS</div><div><div class="community-author">Heshinth S <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div><div style="font-size:0.875rem; color:var(--text3)">2 weeks ago</div></div></div>
          <div class="community-content">Ladakh on a ₹18k budget for a whole week. It's totally doable! Stayed in homestays, ate local thukpa, and shared cabs. Best experience ever. 🏔️🎒</div>
          <div style="margin-bottom:16px"><span class="badge badge-gray">Ladakh</span><span class="badge badge-gray">Budget Travel</span></div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action" onclick="likePost(this)"><i class="far fa-heart"></i> <span>376</span></div>
              <div class="community-action"><i class="far fa-comment"></i> 92</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>
      </div>
      
      <div class="grid-2 trip-mode intl-mode" style="display:none;">
        <div class="community-card">
          <div class="community-header"><div class="community-avatar" style="background-color: var(--accent);">MR</div><div><div class="community-author">Mrudul Mistri <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div><div style="font-size:0.875rem; color:var(--text3)">2 days ago</div></div></div>
          <div class="community-content">Paragliding in Interlaken was simply breathtaking! Highly recommend doing it early morning. 🪂🏔️</div>
          <div style="margin-bottom:16px"><span class="badge badge-gray">Switzerland</span><span class="badge badge-gray">Adventure</span></div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action" onclick="likePost(this)"><i class="far fa-heart"></i> <span>142</span></div>
              <div class="community-action"><i class="far fa-comment"></i> 28</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>
        <div class="community-card">
          <div class="community-header"><div class="community-avatar" style="background-color: var(--teal);">YZ</div><div><div class="community-author">Yuvraj Zende <i class="fas fa-check-circle" style="color:var(--teal);font-size:0.875rem"></i></div><div style="font-size:0.875rem; color:var(--text3)">5 days ago</div></div></div>
          <div class="community-content">Rome in June is quite warm but absolutely magical. Don't skip the Vatican Museum! 🏛️🍕</div>
          <div style="margin-bottom:16px"><span class="badge badge-gray">Italy</span><span class="badge badge-gray">Rome</span></div>
          <div class="community-footer">
            <div class="community-actions">
              <div class="community-action" onclick="likePost(this)"><i class="far fa-heart"></i> <span>89</span></div>
              <div class="community-action"><i class="far fa-comment"></i> 15</div>
            </div>
            <div class="community-action"><i class="far fa-bookmark"></i></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Screen 7: Profile -->
    <div id="screen-profile" class="screen">
      <div class="screen-header"><h1>User Profile</h1></div>
      <div class="profile-header">
        <div class="profile-avatar">JA</div>
        <div class="profile-info">
          <h1>James Arjun</h1>
          <p style="color:var(--text2); margin-bottom:8px">james.arjun@email.com · Mumbai, India</p>
          <p style="margin-bottom:12px;">Passionate traveler | Photography enthusiast | 22 countries visited</p>
        </div>
        <div class="profile-stats">
          <div><div class="profile-stat-val">22</div><div class="profile-stat-label">Countries</div></div>
          <div><div class="profile-stat-val">47</div><div class="profile-stat-label">Trips</div></div>
          <div><div class="profile-stat-val">312</div><div class="profile-stat-label">Followers</div></div>
        </div>
      </div>
      
      <div class="trip-mode india-mode">
        <h3 class="card-title" style="margin-bottom:16px">Preplanned Trips</h3>
        <div class="grid-3" style="margin-bottom:32px">
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Kerala Retreat</div><div class="trip-card-meta">Upcoming Aug 2026</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Leh Ladakh Ride</div><div class="trip-card-meta">Upcoming Sep 2026</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Andaman Escape</div><div class="trip-card-meta">Upcoming Nov 2026</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
        </div>
        <h3 class="card-title" style="margin-bottom:16px">Previous Trips</h3>
        <div class="grid-3">
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Rajasthan Heritage</div><div class="trip-card-meta">Completed Jun 2025</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Goa Escape</div><div class="trip-card-meta">Completed Dec 2024</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Thailand Backpacking</div><div class="trip-card-meta">Completed Mar 2024</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
        </div>
      </div>
      
      <div class="trip-mode intl-mode" style="display:none;">
        <h3 class="card-title" style="margin-bottom:16px">Preplanned Trips</h3>
        <div class="grid-3" style="margin-bottom:32px">
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Bali Wellness Retreat</div><div class="trip-card-meta">Upcoming Aug 2026</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Greek Island Hopping</div><div class="trip-card-meta">Upcoming Oct 2026</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Machu Picchu Trek</div><div class="trip-card-meta">Upcoming Jan 2027</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
        </div>
        <h3 class="card-title" style="margin-bottom:16px">Previous Trips</h3>
        <div class="grid-3">
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Paris & Rome Adventure</div><div class="trip-card-meta">Completed Jun 2025</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">London Winter Trip</div><div class="trip-card-meta">Completed Dec 2024</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
          <div class="trip-card"><div class="trip-card-body"><div class="trip-card-name">Thailand Backpacking</div><div class="trip-card-meta">Completed Mar 2024</div><button class="btn btn-sm btn-primary" onclick="showScreen('itinerary')">View</button></div></div>
        </div>
      </div>
    </div>

    <!-- Screen 12: Admin Panel -->
    <div id="screen-admin" class="screen">
      <div class="screen-header"><h1>Admin Panel</h1></div>
      <div class="admin-tabs">
        <div class="admin-tab active" onclick="switchAdminTab('users', this)">Manage Users</div>
        <div class="admin-tab" onclick="switchAdminTab('cities', this)">Popular Cities</div>
        <div class="admin-tab" onclick="switchAdminTab('activities', this)">Popular Activities</div>
        <div class="admin-tab" onclick="switchAdminTab('trends', this)">Trends & Analytics</div>
      </div>
      <div id="admin-tab-users" class="admin-panel-content" style="display:block">
        <div class="grid-4" style="margin-bottom:24px">
          <div class="stat-card"><div class="stat-icon"><i class="fas fa-users"></i></div><div class="stat-info"><div class="stat-label">Total Users</div><div class="stat-value">12,840</div></div></div>
          <div class="stat-card"><div class="stat-icon" style="color:var(--teal)"><i class="fas fa-map-marked-alt"></i></div><div class="stat-info"><div class="stat-label">Active Trips</div><div class="stat-value">3,421</div></div></div>
        </div>
        <div class="card" style="overflow-x:auto">
          <table class="data-table">
            <thead><tr><th>User</th><th>Email</th><th>Trips</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:bold">James Arjun</td><td>james@email.com</td><td>47</td><td><span class="badge badge-green">Active</span></td></tr>
              <tr><td style="font-weight:bold">Sakthi K</td><td>sakthi@email.com</td><td>18</td><td><span class="badge badge-gray">Inactive</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div id="admin-tab-cities" class="admin-panel-content">
        <div class="card trip-mode india-mode" style="max-width:800px; margin:0 auto">
          <h3 class="card-title" style="margin-bottom:24px">Popular Cities</h3>
          <div class="chart-bar"><div class="chart-bar-label">Jaipur</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:88%; background:var(--accent)">8820</div></div><div style="font-weight:bold">88%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">Goa</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:79%; background:var(--teal)">7940</div></div><div style="font-weight:bold">79%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">Manali</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:71%; background:var(--accent2)">7120</div></div><div style="font-weight:bold">71%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">Udaipur</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:65%; background:#007bff">6510</div></div><div style="font-weight:bold">65%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">Kerala</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:55%; background:#28a745">5530</div></div><div style="font-weight:bold">55%</div></div>
        </div>
        <div class="card trip-mode intl-mode" style="max-width:800px; margin:0 auto; display:none;">
          <h3 class="card-title" style="margin-bottom:24px">Popular Cities</h3>
          <div class="chart-bar"><div class="chart-bar-label">Paris</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:88%; background:var(--accent)">8820</div></div><div style="font-weight:bold">88%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">Tokyo</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:79%; background:var(--teal)">7940</div></div><div style="font-weight:bold">79%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">Rome</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:71%; background:var(--accent2)">7120</div></div><div style="font-weight:bold">71%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">New York</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:65%; background:#007bff">6510</div></div><div style="font-weight:bold">65%</div></div>
          <div class="chart-bar"><div class="chart-bar-label">Bali</div><div class="chart-bar-track"><div class="chart-bar-fill" style="width:55%; background:#28a745">5530</div></div><div style="font-weight:bold">55%</div></div>
        </div>
      </div>
      <div id="admin-tab-activities" class="admin-panel-content">
        <div class="card trip-mode india-mode" style="overflow-x:auto">
          <table class="data-table">
            <thead><tr><th>Activity</th><th>Category</th><th>Bookings</th><th>Revenue</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:bold">Camel Safari</td><td><span class="badge badge-amber">Adventure</span></td><td>4,210</td><td style="color:var(--teal);font-weight:bold">₹8.4M</td></tr>
              <tr><td style="font-weight:bold">River Rafting</td><td><span class="badge badge-blue">Adventure</span></td><td>9,830</td><td style="color:var(--teal);font-weight:bold">₹4.9M</td></tr>
              <tr><td style="font-weight:bold">Scuba Diving</td><td><span class="badge badge-teal">Adventure</span></td><td>7,120</td><td style="color:var(--teal);font-weight:bold">₹3.5M</td></tr>
              <tr><td style="font-weight:bold">Temple Tours</td><td><span class="badge badge-pink">Culture</span></td><td>11,240</td><td style="color:var(--teal);font-weight:bold">₹2.2M</td></tr>
              <tr><td style="font-weight:bold">Houseboat Stay</td><td><span class="badge badge-gray">Leisure</span></td><td>2,890</td><td style="color:var(--teal);font-weight:bold">₹5.7M</td></tr>
            </tbody>
          </table>
        </div>
        <div class="card trip-mode intl-mode" style="overflow-x:auto; display:none;">
          <table class="data-table">
            <thead><tr><th>Activity</th><th>Category</th><th>Bookings</th><th>Revenue</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:bold">Paragliding</td><td><span class="badge badge-gray">Adventure</span></td><td>4,210</td><td style="color:var(--teal);font-weight:bold">$840K</td></tr>
              <tr><td style="font-weight:bold">Guided City Tours</td><td><span class="badge badge-gray">Culture</span></td><td>9,830</td><td style="color:var(--teal);font-weight:bold">$490K</td></tr>
              <tr><td style="font-weight:bold">Food & Wine Tasting</td><td><span class="badge badge-gray">Food</span></td><td>7,120</td><td style="color:var(--teal);font-weight:bold">$356K</td></tr>
              <tr><td style="font-weight:bold">Scuba Diving</td><td><span class="badge badge-gray">Adventure</span></td><td>2,890</td><td style="color:var(--teal);font-weight:bold">$578K</td></tr>
              <tr><td style="font-weight:bold">Museum Passes</td><td><span class="badge badge-gray">Culture</span></td><td>11,240</td><td style="color:var(--teal);font-weight:bold">$224K</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div id="admin-tab-trends" class="admin-panel-content">
        <div class="grid-2">
          <div class="card">
            <h3 class="card-title">Revenue Distribution</h3>
            <div style="width:160px; height:160px; border-radius:50%; background:conic-gradient(var(--accent) 0% 50%, var(--teal) 50% 80%, var(--accent2) 80% 100%); margin:24px auto;"></div>
          </div>
        </div>
      </div>
    </div>

  </div> <!-- main -->

  <!-- Modals -->
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
        <button class="btn btn-primary" style="flex:1" onclick="closeModal('plan-trip-modal'); showScreen('plan'); showToast('Started planning trip')">Continue</button>
        <button class="btn" style="flex:1;border:1px solid var(--border)" onclick="closeModal('plan-trip-modal')">Cancel</button>
      </div>
    </div>
  </div>

  <div class="modal-bg" id="add-item-modal">
    <div class="modal">
      <div class="modal-header"><h2 class="modal-title">Add Item to Checklist</h2><button class="modal-close" onclick="closeModal('add-item-modal')">&times;</button></div>
      <div class="input-group"><label class="label">Item Name</label><input type="text" class="input" id="new-item-name" placeholder="e.g. Sunglasses"></div>
      <div class="input-group">
        <label class="label">Category</label>
        <select class="select" id="new-item-category">
          <option>Documents</option><option>Clothing</option><option>Electronics</option><option>Health & Hygiene</option>
        </select>
      </div>
      <button class="btn btn-primary" style="width:100%;margin-top:16px" onclick="addChecklistItem()">Add Item</button>
    </div>
  </div>

  <div class="modal-bg" id="add-note-modal">
    <div class="modal">
      <div class="modal-header"><h2 class="modal-title">Add Trip Note</h2><button class="modal-close" onclick="closeModal('add-note-modal')">&times;</button></div>
      <div class="input-group"><label class="label">Title</label><input type="text" class="input" id="note-title" placeholder="e.g. Hotel Check-in"></div>
      <div class="input-group"><label class="label">Content</label><textarea class="input" id="note-content" rows="4" placeholder="Write your notes here..."></textarea></div>
      <div class="form-grid">
        <div class="input-group"><label class="label">Day / Date</label><input type="text" class="input" id="note-day" placeholder="e.g. Day 3"></div>
        <div class="input-group"><label class="label">Stop / City</label><input type="text" class="input" id="note-city" placeholder="e.g. Jaipur"></div>
      </div>
      <button class="btn btn-accent" style="width:100%;margin-top:16px" onclick="addNote()">Save Note</button>
    </div>
  </div>

  <!-- JavaScript -->
  <script>
    let currentTripType = localStorage.getItem('tripType') || 'india';

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
        el.innerText = type === 'india' ? '₹' : '$';
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
    function toggleAuthTab(tab) {
      document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('form').forEach(f => f.style.display = 'none');
      document.getElementById(tab + '-tab').classList.add('active');
      document.getElementById(tab + '-form').style.display = 'block';
    }

    function handleAuth(e, isSignup = false) {
      e.preventDefault();
      document.body.classList.add('logged-in');
      showScreen('home');
      showToast(isSignup ? 'Account created successfully!' : 'Logged in successfully!');
    }

    function showScreen(name) {
      document.querySelectorAll('.screen').forEach(s => {
        s.classList.remove('visible');
      });
      document.getElementById('screen-' + name).classList.add('visible');
      
      document.querySelectorAll('.sidebar-link, .mobile-nav a').forEach(l => l.classList.remove('active'));
      document.querySelectorAll(`a[onclick="showScreen('${name}')"]`).forEach(l => l.classList.add('active'));
      window.scrollTo(0,0);
    }

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
    });
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("India-first index.html built successfully.")
