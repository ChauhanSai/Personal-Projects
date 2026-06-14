document.addEventListener('DOMContentLoaded', () => {
    // Scroll behavior for Landing -> Features (index.html)
    const discoBall = document.getElementById('main-disco-ball');
    if (discoBall) {
        window.addEventListener('scroll', () => {
            const scrollPos = window.scrollY;
            const panel = document.getElementById('sonic-profiling-panel');
            let maxScroll = window.innerHeight * 0.8;
            if (panel) {
                const rect = panel.getBoundingClientRect();
                const absoluteBottom = rect.bottom + scrollPos;
                maxScroll = absoluteBottom - window.innerHeight;
                if (maxScroll <= 0) maxScroll = window.innerHeight * 0.8;
            }

            let progress = scrollPos / maxScroll;
            progress = Math.min(1, Math.max(0, progress));

            discoBall.style.setProperty('--scroll-progress', progress);
        });
    }

    // Dynamic Sparkles Logic
    const sparkleSVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 2500" width="100%" height="100%"><path fill="#ffffff" d="M 995.00,134.00 C 997.62,134.00 1003.50,133.61 1005.57,135.02 1007.72,136.49 1008.09,139.65 1008.65,142.00 1008.65,142.00 1012.87,159.00 1012.87,159.00 1012.87,159.00 1032.63,237.00 1032.63,237.00 1060.30,346.32 1095.13,465.00 1135.81,570.00 1185.94,699.38 1250.41,820.98 1347.04,922.00 1347.04,922.00 1375.00,949.09 1375.00,949.09 1375.00,949.09 1395.00,967.72 1395.00,967.72 1444.65,1011.39 1501.64,1050.68 1559.00,1083.57 1629.22,1123.83 1703.21,1158.14 1778.00,1188.99 1778.00,1188.99 1852.00,1218.58 1852.00,1218.58 1852.00,1218.58 1902.00,1238.00 1902.00,1238.00 1897.81,1241.00 1888.14,1244.17 1883.00,1246.05 1883.00,1246.05 1853.00,1257.60 1853.00,1257.60 1853.00,1257.60 1745.00,1301.43 1745.00,1301.43 1648.05,1342.79 1547.52,1393.68 1462.00,1455.42 1424.53,1482.48 1389.67,1512.33 1357.00,1545.00 1357.00,1545.00 1337.17,1565.00 1337.17,1565.00 1305.94,1599.52 1276.81,1635.99 1251.34,1675.00 1167.34,1803.66 1116.16,1949.73 1072.28,2096.00 1054.52,2155.22 1038.62,2215.03 1023.63,2275.00 1023.63,2275.00 1002.00,2364.00 1002.00,2364.00 1002.00,2364.00 1000.00,2364.00 1000.00,2364.00 1000.00,2364.00 980.37,2283.00 980.37,2283.00 966.65,2228.09 952.29,2173.33 936.42,2119.00 880.59,1927.82 809.57,1725.09 673.83,1575.00 631.69,1528.40 584.09,1486.94 533.00,1450.43 446.44,1388.56 343.79,1338.51 246.00,1296.85 246.00,1296.85 147.00,1256.81 147.00,1256.81 147.00,1256.81 119.00,1246.05 119.00,1246.05 113.22,1243.93 104.87,1241.53 100.00,1238.00 100.00,1238.00 150.00,1218.55 150.00,1218.55 150.00,1218.55 258.00,1174.57 258.00,1174.57 361.01,1130.63 472.28,1073.74 561.00,1005.35 623.20,957.41 674.40,905.84 721.53,843.00 820.29,711.30 884.49,535.27 930.42,378.00 930.42,378.00 973.88,219.00 973.88,219.00 973.88,219.00 990.65,152.00 990.65,152.00 990.65,152.00 995.00,134.00 995.00,134.00 Z"/></svg>`;

    // Remove static hardcoded sparkles
    document.querySelectorAll('.sparkle').forEach(el => el.remove());

    document.querySelectorAll('.discomorphic-panel').forEach(panel => {
        const r = Math.random();
        if (r < 0.5) {
            // 50% chance of no sparkles
        } else if (r < 0.75) {
            // 25% chance for two sparkles
            addSparkle(panel, 'left');
            addSparkle(panel, 'right');
        } else if (r < 0.875) {
            // 12.5% chance of left sparkle
            addSparkle(panel, 'left');
        } else {
            // 12.5% chance of right sparkle
            addSparkle(panel, 'right');
        }
    });

    function addSparkle(panel, side) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.style.top = (Math.random() * 80 + 10) + '%'; // 10% to 90% to keep it reasonably centered vertically
        if (side === 'left') {
            sparkle.style.left = '0';
        } else {
            sparkle.style.left = '100%';
        }
        sparkle.innerHTML = sparkleSVG;
        panel.appendChild(sparkle);
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


});
