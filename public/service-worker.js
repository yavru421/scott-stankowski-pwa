self.addEventListener('install', (event) => {
    console.log('Service Worker installing.');
    // Perform install steps
    event.waitUntil(
        caches.open('realtor-pwa-v1').then((cache) => {
            console.log('Opened cache');
            return cache.addAll([
                '/',
                '/src/index.html',
                '/src/styles/style.css',
                '/src/main.js',
                '/public/manifest.json',
            ]);
        })
    );
});

self.addEventListener('fetch', (event) => {
    console.log('Service Worker fetching.', event.request.url);
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
