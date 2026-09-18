// Optimized theme management for better performance
class ThemeManager {
    constructor() {
        this.userInitiatedThemeChange = false;
        this.themeObserver = null;
        this.initialized = false;
        this.currentTheme = this.getStoredTheme();
    }

    getStoredTheme() {
        if (typeof window === 'undefined') return false;
        // Only return true for dark theme if explicitly set in localStorage
        // Default to light theme when localStorage.theme doesn't exist
        return localStorage.theme === 'dark';
    }

    applyTheme(theme = null) {
        const isDark = theme !== null ? theme : this.getStoredTheme();
        const htmlElement = document.documentElement;

        // Force immediate update of the class
        if (isDark) {
            htmlElement.classList.add('dark');
        } else {
            htmlElement.classList.remove('dark');
        }

        this.currentTheme = isDark;
        return isDark;
    }

    updateThemeToggleUI(isDark, animate = false) {
        const switchThumb = document.getElementById('theme-switch-thumb');
        const lightIcon = document.getElementById('light-mode-icon');
        const darkIcon = document.getElementById('dark-mode-icon');
        const themeToggle = document.getElementById('theme-toggle');
        
        if (!switchThumb) return;

        // translateX is physical, but the thumb's resting edge is the inline
        // start — in RTL the "on" position is to the LEFT, so negate the shift.
        const isRTL = getComputedStyle(switchThumb).direction === 'rtl';
        const onShift = isRTL ? '-1.75rem' : '1.75rem';
        const targetTransform = isDark ? `translateX(${onShift})` : 'translateX(0)';
        
        if (!animate) {
            switchThumb.style.transition = 'none';
            switchThumb.style.transform = targetTransform;
            // Use requestAnimationFrame for better performance
            requestAnimationFrame(() => {
                switchThumb.style.transition = '';
            });
        } else {
            switchThumb.style.transform = targetTransform;
        }
        
        // Batch DOM updates
        if (lightIcon && darkIcon) {
            lightIcon.classList.toggle('hidden', isDark);
            darkIcon.classList.toggle('hidden', !isDark);
        }
        
        themeToggle?.setAttribute('aria-checked', isDark ? 'true' : 'false');
    }

    startThemeMonitoring() {
        if (this.themeObserver) return;
        
        // Optimized mutation observer
        this.themeObserver = new MutationObserver((mutations) => {
            if (this.userInitiatedThemeChange) return;
            
            for (const mutation of mutations) {
                if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                    const expectedTheme = this.getStoredTheme();
                    const hasClass = document.documentElement.classList.contains('dark');
                    
                    if (hasClass !== expectedTheme) {
                        this.applyTheme(expectedTheme);
                    }
                    break;
                }
            }
        });
        
        this.themeObserver.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ['class']
        });
    }

    toggleTheme() {
        this.userInitiatedThemeChange = true;

        const newTheme = !this.currentTheme;

        // Update localStorage first
        localStorage.theme = newTheme ? 'dark' : 'light';

        // Apply theme immediately
        this.applyTheme(newTheme);

        // Force immediate repaint
        document.documentElement.offsetHeight;

        // Update UI after theme is applied
        this.updateThemeToggleUI(newTheme, true);

        // Reset flag after animation
        setTimeout(() => {
            this.userInitiatedThemeChange = false;
        }, 100);
    }

    initializeThemeToggle() {
        const themeToggle = document.getElementById('theme-toggle');
        
        if (!themeToggle || themeToggle.hasAttribute('data-initialized')) return;
        
        themeToggle.setAttribute('data-initialized', 'true');
        
        // Use event delegation for better performance
        themeToggle.addEventListener('click', (e) => {
            e.preventDefault();
            this.toggleTheme();
        });

        themeToggle.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.toggleTheme();
            }
        });
    }

    initialize() {
        if (this.initialized) return;
        
        const isDark = this.applyTheme();
        this.updateThemeToggleUI(isDark, false);
        this.initializeThemeToggle();
        this.startThemeMonitoring();
        
        this.initialized = true;
    }
}

// Export for use in other scripts
window.ThemeManager = ThemeManager;