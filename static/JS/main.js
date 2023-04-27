// This file contains general JavaScript code for our web app.

// Display a confirmation dialog before deleting a product.
function confirmDelete() {
    return confirm('Are you sure you want to delete this product?');
}

// Disable the form submit button after it's clicked to prevent duplicate submissions.
function disableSubmitButton(form) {
    form.querySelector('button[type="submit"]').disabled = true;
}
