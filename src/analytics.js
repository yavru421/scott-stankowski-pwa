// Simple analytics helper for PWA

const Analytics = {
    // Track page views
    pageView: function(pagePath) {
        if (navigator.onLine && window.gtag) {
            gtag('event', 'page_view', {
                page_path: pagePath
            });
        } else {
            this.saveOfflineEvent('page_view', { page_path: pagePath });
        }
    },
    
    // Track events
    event: function(eventName, params = {}) {
        if (navigator.onLine && window.gtag) {
            gtag('event', eventName, params);
        } else {
            this.saveOfflineEvent(eventName, params);
        }
    },
    
    // Save events for later when offline
    saveOfflineEvent: function(name, params) {
        let events = [];
        if (window.localStorage.getItem('offlineAnalytics')) {
            events = JSON.parse(window.localStorage.getItem('offlineAnalytics'));
        }
        events.push({name, params, timestamp: new Date().toISOString()});
        window.localStorage.setItem('offlineAnalytics', JSON.stringify(events));
    }
};

// Export for use in other files
export default Analytics;
