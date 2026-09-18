// Main initialization script - optimized for performance
(function() {
    'use strict';
    
    // Immediate theme application to prevent FOUC
    function applyImmediateTheme() {
        const isDark = localStorage.theme === 'dark' || 
            (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);
        
        document.documentElement.classList.toggle('dark', isDark);
        return isDark;
    }

    // Initialize all components efficiently
    function initializeApp() {
        // Apply theme first
        applyImmediateTheme();

        // Initialize performance optimizations - only create once
        if (window.PerformanceOptimizer && !window.appPerfOptimizer) {
            const perfOptimizer = new window.PerformanceOptimizer();
            perfOptimizer.initialize();
            window.appPerfOptimizer = perfOptimizer;
        }

        // Initialize theme manager - only create once
        if (window.ThemeManager && !window.appThemeManager) {
            const themeManager = new window.ThemeManager();
            themeManager.initialize();
            window.appThemeManager = themeManager; // Store for global access
        }

        // Initialize navigation - only create once
        if (window.NavigationManager && !window.appNavManager) {
            const navManager = new window.NavigationManager();
            navManager.initialize();
            window.appNavManager = navManager; // Store for global access
        }
    }

    // Handle Astro ClientRouter events
    function setupAstroEventListeners() {
        // Re-apply theme on navigation
        document.addEventListener('astro:before-preparation', applyImmediateTheme);
        document.addEventListener('astro:before-swap', applyImmediateTheme);
        document.addEventListener('astro:after-swap', applyImmediateTheme);
        
        // Reinitialize components after navigation
        document.addEventListener('astro:page-load', () => {
            if (window.appThemeManager) {
                window.appThemeManager.initialize();
            }
            if (window.appNavManager) {
                // Force navigation update on page change
                window.appNavManager.updateActiveNavigation();
            }
        });
    }

    // System theme change listener
    function setupSystemThemeListener() {
        if (window.systemThemeListenerAdded) return;
        
        window.systemThemeListenerAdded = true;
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        mediaQuery.addEventListener('change', () => {
            if (!('theme' in localStorage) && window.appThemeManager) {
                window.appThemeManager.initialize();
            }
        });
    }

    // Initialize everything
    function init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initializeApp);
        } else {
            initializeApp();
        }
        
        setupAstroEventListeners();
        setupSystemThemeListener();
    }

    // Start initialization
    init();
})();