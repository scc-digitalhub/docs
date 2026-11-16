(() => {
    function openAnchoredDetails() {
        const id = decodeURIComponent(window.location.hash.slice(1));
        if (!id) return;

        const target = document.getElementById(id);
        if (!target) return;

        const containingDetails = target.closest("details");
        const followingDetails = target.closest("p")?.nextElementSibling;
        const details = containingDetails ?? followingDetails;

        if (details instanceof HTMLDetailsElement) {
            details.open = true;
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", openAnchoredDetails, { once: true });
    } else {
        openAnchoredDetails();
    }

    window.addEventListener("hashchange", openAnchoredDetails);
})();
