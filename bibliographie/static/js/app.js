app = {
    init: function() {
        this.smoothScroll();
        this.deleteComment();
        this.logoutTooltip();
    },

    smoothScroll : function() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    },


    deleteComment : function() {  
        document.querySelectorAll('#delete-comment').forEach(button => {
            button.addEventListener('click', function(event) {
                if (!confirm('Voulez-vous vraiment supprimer ce commentaire ?')) {
                    event.preventDefault();
                }
            });
        });
    },

    logoutTooltip: function() {
        const logoutIcon = document.getElementById('logoutIcon');

        if (logoutIcon) {
            logoutIcon.addEventListener('mouseenter', function() {
                //création de l'élément pour afficher le message
                const tooltip = document.createElement('div');
                tooltip.textContent = 'Se déconnecter';
                tooltip.classList.add('js-tooltip');
                document.body.appendChild(tooltip);

                // Position de l'élément
                const rect = logoutIcon.getBoundingClientRect();
                tooltip.style.left = `${rect.left + window.scrollX + rect.width / 2 - tooltip.offsetWidth / 2}px`;
                tooltip.style.top = `${rect.bottom + window.scrollY + 10}px`;
            });
        
            logoutIcon.addEventListener('mouseleave', function() {
                const tooltip = document.querySelector('.js-tooltip');
                if (tooltip) {
                    tooltip.remove();
                }
            });
        }
    }
};    


document.addEventListener('DOMContentLoaded', function() {
    app.init();
});

