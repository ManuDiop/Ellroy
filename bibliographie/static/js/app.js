document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM chargé correctement !");
    
    document.querySelectorAll('.delete-comment').forEach(button => {
        button.addEventListener('click', function(event) {
            if (!confirm('Voulez-vous vraiment supprimer ce commentaire ?')) {
                event.preventDefault();
            }
        });
    });
});
