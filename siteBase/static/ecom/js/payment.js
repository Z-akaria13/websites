document.addEventListener('DOMContentLoaded', function () {
    var orderForm = document.getElementById('order-form');
    var stripeButton = orderForm.querySelector('.stripe-button-el');

    orderForm.addEventListener('submit', function (event) {
        event.preventDefault();
        stripeButton.disabled = true;

        fetch('/ecommerce/make_payment/', {  // Update this line to use the correct view name
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': orderForm.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: new URLSearchParams(new FormData(orderForm)),
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                alert(data.message);
                if (data.message === 'Payment successful!') {
                    window.location.href = '/ecommerce/';
                } else {
                    stripeButton.disabled = false;
                }
            })
            .catch(function (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
                stripeButton.disabled = false;
            });
    });
});
