document.getElementById('profile').addEventListener('change', function () {
    var fileInput = document.getElementById('profile');
    var fileDisplay = document.getElementById('file');
    var imagePreview = document.getElementById('imagePreview');

    if (fileInput.files.length > 0) {
        var fileNames = Array.from(fileInput.files).map(function (file) {
            return file.name;
        }).join(', ');

        fileDisplay.value = fileNames;
        imagePreview.style.display = 'block';
    } else {
        fileDisplay.value = '';
        imagePreview.style.display = 'none';
    }
});