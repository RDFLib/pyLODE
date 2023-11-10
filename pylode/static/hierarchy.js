let nodes = document.getElementsByClassName("hierarchy-node");

// Register event listener
for (let node of nodes) {
    node.addEventListener("click", function () {
        node.classList.toggle("hierarchy-node-active");
        this.parentElement
            .querySelector(".nested-hierarchy-list")
            .classList.toggle("nested-hierarchy-node-active");
    });
}

function getNestedElements(element, depth, currentDepth = 0) {
    if (currentDepth > depth) {
        return [];
    }

    const childElements = Array.from(element.children);

    if (currentDepth === depth) {
        return childElements;
    }

    const nestedElements = childElements.flatMap(child =>
        getNestedElements(child, depth, currentDepth + 1)
    );

    return childElements.concat(nestedElements);
}

//
// On load, expand first 3 levels
//
const profilesHierarchy = document.getElementById("profiles-hierarchy");
// Note: depth is not the depth of the hierarchy, rather it's the depth of the DOM tree from the root element.
const initialNodes = getNestedElements(profilesHierarchy, 4);

for (let node of initialNodes) {
    if (node.classList.contains("hierarchy-node")) {
        node.dispatchEvent(new Event("click"))
    }
}