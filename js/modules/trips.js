async function initializeTrips() {
  console.log("Fetching trips...");
  const response = await API.fetchData('trips');
  
  if (response.success) {
    const trips = response.data;
    const indiaContainer = document.getElementById('trips-container-india');
    const intlContainer = document.getElementById('trips-container-intl');
    
    if (indiaContainer) indiaContainer.innerHTML = '';
    if (intlContainer) intlContainer.innerHTML = '';
    
    if (trips.length === 0) {
      if (indiaContainer) indiaContainer.innerHTML = '<div style="grid-column: 1/-1; text-align: center; color: var(--text2); padding: 40px; font-size: 1.1rem;">No trips planned yet. Click "Plan a Trip" in the sidebar to get started! ✈️</div>';
      return;
    }
    
    trips.forEach(trip => {
      const tripHtml = `
        <div class="trip-card" onclick="viewTrip(${trip.id})">
          <div class="trip-card-img" style="background: linear-gradient(135deg, var(--primary), var(--accent2));"></div>
          <div class="trip-card-body">
            <div class="trip-card-name">${trip.trip_name}</div>
            <div class="trip-card-meta">${formatDateRange(trip.start_date, trip.end_date)} · <span class="badge badge-gray">${trip.status || 'Plan'}</span></div>
            <div class="trip-card-meta"><i class="fas fa-map-marker-alt"></i> ${trip.destination}</div>
          </div>
          <div class="trip-card-footer">
            <span style="color:var(--text2)">Budget</span>
            <span style="color:var(--primary)">${trip.trip_type === 'india' ? '₹' : '$'}${trip.total_budget}</span>
          </div>
        </div>
      `;
      
      if (trip.trip_type === 'india' && indiaContainer) {
        indiaContainer.insertAdjacentHTML('beforeend', tripHtml);

      } else if (trip.trip_type === 'intl' && intlContainer) {
        intlContainer.insertAdjacentHTML('beforeend', tripHtml);
      }
    });
  } else {
    console.error('Failed to load trips:', response.message);
  }
}

function formatDateRange(startStr, endStr) {
  if (!startStr) return 'TBD';
  const start = new Date(startStr);
  const options = { day: 'numeric', month: 'short' };
  const startFormatted = start.toLocaleDateString('en-US', options);
  
  if (endStr) {
    const end = new Date(endStr);
    const endFormatted = end.toLocaleDateString('en-US', { ...options, year: 'numeric' });
    return `${startFormatted} - ${endFormatted}`;
  }
  return start.toLocaleDateString('en-US', { ...options, year: 'numeric' });
}

window.viewTrip = function(tripId) {
  localStorage.setItem('currentTripId', tripId);
  window.location.href = 'itinerary.html'; // Redirect to itinerary or budget
}


