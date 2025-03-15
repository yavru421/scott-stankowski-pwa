let deferredPrompt;
const installButton = document.getElementById('install-button');

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    installButton.style.display = 'block';
});

installButton.addEventListener('click', () => {
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
            console.log('User accepted the install prompt');
            installButton.style.display = 'none';
        }
        deferredPrompt = null;
    });
});

window.addEventListener('appinstalled', () => {
    installButton.style.display = 'none';
    deferredPrompt = null;
});
