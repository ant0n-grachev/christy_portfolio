(function () {
    document.addEventListener('DOMContentLoaded', function () {
        const mediaTypeInputs = document.querySelectorAll('input[name="media_type"]');
        const imageRow = document.querySelector('.form-row.field-image');
        const videoRow = document.querySelector('.form-row.field-video');
        const imageInput = document.getElementById('id_image');
        const videoInput = document.getElementById('id_video');
        const imageLabel = document.querySelector('label[for="id_image"]');

        function updateVisibility() {
            const selected = document.querySelector('input[name="media_type"]:checked');
            if (!selected) {
                imageRow.style.display = 'none';
                videoRow.style.display = 'none';
                imageInput.required = false;
                videoInput.required = false;
                return;
            }
            if (selected.value === 'image') {
                imageRow.style.display = '';
                videoRow.style.display = 'none';
                imageInput.required = true;
                videoInput.required = false;
                imageLabel.textContent = 'Image:';
            } else if (selected.value === 'video') {
                imageRow.style.display = '';
                videoRow.style.display = '';
                imageInput.required = true;
                videoInput.required = true;
                imageLabel.textContent = 'Cover Image:';
            }
        }

        mediaTypeInputs.forEach(input => {
            input.addEventListener('change', updateVisibility);
        });
        updateVisibility();
    });
})();