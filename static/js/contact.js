const form = document.getElementById('contactForm');

if (form) {

    form.addEventListener('submit', async function (e) {

        e.preventDefault();

        const button =
            document.getElementById('submitBtn');

        const successAlert =
            document.getElementById('successAlert');

        const errorAlert =
            document.getElementById('errorAlert');

        button.classList.add('loading');

        successAlert.classList.remove('show');
        errorAlert.classList.remove('show');

        const formData = new FormData(form);

        try {

            const response = await fetch('', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.success) {

                form.reset();

                successAlert.classList.add('show');

            } else {

                errorAlert.innerHTML =
                    'Please check your form and try again.';

                errorAlert.classList.add('show');
            }

        } catch (error) {

            errorAlert.innerHTML =
                'Server error. Please try again later.';

            errorAlert.classList.add('show');
        }

        button.classList.remove('loading');

    });

}