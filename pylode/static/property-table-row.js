function toggleHiddenElements(elementsList) {
    for (const el of elementsList) {
        el.classList.toggle("hidden");
    }
}

const allSecondaryRows = document.getElementsByClassName(
    "property-row-secondary"
);
toggleHiddenElements(allSecondaryRows);

const propertyButtons = document.getElementsByClassName(
    "property-row-button"
);

const BTN_CIRCLE_RIGHT = "fa-arrow-circle-right";
const BTN_CIRCLE_DOWN = "fa-arrow-circle-down";

for (const btn of propertyButtons) {
    btn.addEventListener("click", () => {
        // Toggle button icon
        const buttonIcon = btn.firstElementChild;
        if (buttonIcon.classList.contains(BTN_CIRCLE_RIGHT)) {
            buttonIcon.classList.remove(BTN_CIRCLE_RIGHT);
            buttonIcon.classList.add(BTN_CIRCLE_DOWN);
        } else {
            buttonIcon.classList.remove(BTN_CIRCLE_DOWN);
            buttonIcon.classList.add(BTN_CIRCLE_RIGHT);
        }

        const parentRow = btn.parentElement.parentElement;
        const secondaryRows = [];

        // Find secondary rows for current property
        let row = parentRow;
        while (row.nextElementSibling) {
            row = row.nextElementSibling;

            if (row.classList.contains("property-row-secondary")) {
                secondaryRows.push(row);
            } else {
                break;
            }
        }

        toggleHiddenElements(secondaryRows);
    });
}