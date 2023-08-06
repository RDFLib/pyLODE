let nodes = document.getElementsByClassName("hierarchy-node");

for (let node of nodes) {
  node.addEventListener("click", function () {
    node.classList.toggle("hierarchy-node-active");
    this.parentElement
      .querySelector(".nested-hierarchy-list")
      .classList.toggle("nested-hierarchy-node-active");
  });
}
