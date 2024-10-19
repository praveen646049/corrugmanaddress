document.getElementById('address-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;

    // Simple validation example
    const emailField = form.email_id.value;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailField)) {
        document.getElementById('error-message').innerText = 'Please enter a valid email address.';
        document.getElementById('error-message').style.display = 'block';
        return;
    }

    // Proceed with form submission
    alert('Form submitted!'); // Replace with actual submission logic
});

function goBack() {
    window.history.back();
}
