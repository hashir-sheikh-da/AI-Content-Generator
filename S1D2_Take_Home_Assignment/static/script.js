document.addEventListener('DOMContentLoaded', function () {
    // Get the mode switch checkbox element
    const modeSwitch = document.getElementById('mode-switch');

    // Check localStorage for theme preference and apply it
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode'); // Apply dark mode class
        modeSwitch.checked = true; // Check the switch
    }

    // Add an event listener for changes to the mode switch
    modeSwitch.addEventListener('change', function () {
        if (this.checked) {
            // If the switch is checked, enable dark mode
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark'); // Save preference to localStorage
        } else {
            // If the switch is unchecked, disable dark mode
            document.body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light'); // Save preference to localStorage
        }
    });
});
