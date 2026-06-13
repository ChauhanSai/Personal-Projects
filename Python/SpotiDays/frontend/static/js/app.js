document.addEventListener('DOMContentLoaded', () => {
    // Scroll behavior for Landing -> Features (index.html)
    const discoBall = document.getElementById('main-disco-ball');
    if (discoBall) {
        window.addEventListener('scroll', () => {
            const scrollPos = window.scrollY;
            const windowHeight = window.innerHeight;
            
            // If scrolled more than 30% of window height, shift the ball
            if (scrollPos > windowHeight * 0.3) {
                discoBall.classList.add('disco-ball-shifted');
            } else {
                discoBall.classList.remove('disco-ball-shifted');
            }
        });
    }

    // Curate Page interactions (curate.html)
    const dateCards = document.querySelectorAll('.date-card');
    dateCards.forEach(card => {
        card.addEventListener('click', () => {
            // Toggle expanded state on the parent group
            const group = card.closest('.date-group');
            if (group) {
                group.classList.toggle('expanded');
            } else {
                card.classList.toggle('expanded');
            }
        });
    });

    const trackAdds = document.querySelectorAll('.track-add');
    trackAdds.forEach(addBtn => {
        addBtn.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent expanding date card
            const trackItem = addBtn.closest('.track-item');
            trackItem.classList.toggle('selected');
            
            if (trackItem.classList.contains('selected')) {
                addBtn.innerHTML = '✓';
                // Trigger sidebar automatically on first selection just to demo
                document.getElementById('spotted-sidebar').classList.add('open');
            } else {
                addBtn.innerHTML = '+';
            }
        });
    });

    const closeSidebarBtn = document.getElementById('close-sidebar');
    if (closeSidebarBtn) {
        closeSidebarBtn.addEventListener('click', () => {
            document.getElementById('spotted-sidebar').classList.remove('open');
        });
    }

    const openSidebarBtn = document.getElementById('nav-spotted');
    if (openSidebarBtn) {
        openSidebarBtn.addEventListener('click', (e) => {
            e.preventDefault();
            document.getElementById('spotted-sidebar').classList.add('open');
        });
    }
});
