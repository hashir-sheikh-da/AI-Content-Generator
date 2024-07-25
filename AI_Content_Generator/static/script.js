document.addEventListener('DOMContentLoaded', function () {
    const modeSwitch = document.getElementById('mode-switch');

    // Check localStorage for theme preference and apply it
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
        modeSwitch.checked = true;
    }

    modeSwitch.addEventListener('change', function () {
        if (this.checked) {
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
        } else {
            document.body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
        }
    });
});