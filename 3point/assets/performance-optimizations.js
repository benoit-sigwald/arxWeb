// Performance optimizations to minimize layout thrashing
class PerformanceOptimizer {
    constructor() {
        this.resizeTimer = null;
        this.isMobile = window.innerWidth <= 768;
    }

    suppressConsoleErrors() {
        const originalError = console.error;
        console.error = (...args) => {
            const message = args.join(' ');
            
            // Filter extension-related errors
            if (message.includes('Extension context') ||
                message.includes('chrome-extension') ||
                message.includes('moz-extension') ||
                message.includes('safari-extension') ||
                message.includes('edge-extension') ||
                message.includes('runtime.lastError')) {
                return;
            }
            
            originalError.apply(console, args);
        };
    }

    optimizeMobilePerformance() {
        if (!('ontouchstart' in window)) return;
        
        // Prevent 300ms click delay and optimize touch handling
        document.body.style.touchAction = 'manipulation';
        
        // Optimize viewport for mobile
        let viewport = document.querySelector('meta[name="viewport"]');
        if (!viewport) {
            viewport = document.createElement('meta');
            viewport.name = 'viewport';
            document.head.appendChild(viewport);
        }
        viewport.content = 'width=device-width, initial-scale=1, viewport-fit=cover';
    }

    optimizeImagesForMobile() {
        if (!this.isMobile) return;
        
        // Use requestAnimationFrame for better performance
        requestAnimationFrame(() => {
            const images = document.querySelectorAll('img[data-mobile-optimized]');
            images.forEach(img => {
                img.style.willChange = 'transform';
            });
        });
    }

    handleResize() {
        clearTimeout(this.resizeTimer);
        this.resizeTimer = setTimeout(() => {
            this.isMobile = window.innerWidth <= 768;
            this.optimizeImagesForMobile();
        }, 250);
    }

    initialize() {
        this.suppressConsoleErrors();
        this.optimizeMobilePerformance();
        this.optimizeImagesForMobile();
        
        // Add resize listener with throttling
        window.addEventListener('resize', () => this.handleResize(), { passive: true });
    }
}

// Export for global use
window.PerformanceOptimizer = PerformanceOptimizer;