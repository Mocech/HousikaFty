// Password visibility toggle
const togglePassword = document.getElementById('togglePassword');
const password = document.getElementById('password');

togglePassword.addEventListener('click', function() {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    
    // Toggle eye icon
    const icon = this.querySelector('i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
});


// Close button handler
const closeBtn = document.querySelector('.close-btn');
closeBtn.addEventListener('click', function() {
    // Here you would typically close the modal or redirect
    console.log('Close button clicked');
});
