async function login(e) {
  if(e) e.preventDefault();
  const form = e.target;
  const email = form.querySelector('input[type="email"]').value;
  const password = form.querySelector('input[type="password"]').value;

  const response = await API.postData('auth/login', { email, password });
  
  if (response.success) {
    localStorage.setItem('user', JSON.stringify(response.user));
    localStorage.setItem('token', response.token);
    
    // Check if the user is the admin
    if (response.user.email === 'admin@traveloop.com') {
      window.location.href = 'pages/admin.html';
    } else {
      window.location.href = 'pages/dashboard.html';
    }
  } else {
    alert(response.message || 'Login failed');
  }
}

async function signup(e) {
  if(e) e.preventDefault();
  const form = e.target;
  const name = form.querySelector('input[type="text"]').value;
  const email = form.querySelector('input[type="email"]').value;
  const password = form.querySelector('input[type="password"]').value;
  const confirmPassword = form.querySelectorAll('input[type="password"]')[1].value;

  if (password !== confirmPassword) {
    alert('Passwords do not match');
    return;
  }

  const response = await API.postData('auth/signup', { name, email, password });
  
  if (response.success) {
    alert('Signup successful! Please login.');
    toggleAuthTab('login');
  } else {
    alert(response.message || 'Signup failed');
  }
}

function toggleAuthTab(tab) {
  document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
  document.getElementById(tab + '-tab').classList.add('active');
  document.getElementById('login-form').style.display = tab === 'login' ? 'block' : 'none';
  document.getElementById('signup-form').style.display = tab === 'signup' ? 'block' : 'none';
}

