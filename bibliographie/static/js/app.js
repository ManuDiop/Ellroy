app = {
    init: function() {
        this.smoothScroll();
        this.deleteComment();
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

}

document.addEventListener('DOMContentLoaded', function() {
    app.init();
});

