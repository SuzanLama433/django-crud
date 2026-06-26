const deleteModal = document.getElementById("deleteModal");

if (deleteModal) {
  deleteModal.addEventListener("show.bs.modal", function (event) {
    const button = event.relatedTarget;

    document.getElementById("studentName").textContent =
      button.getAttribute("data-name");

    document.getElementById("deleteBtn").href =
      "/delete/" + button.getAttribute("data-id");
  });

  deleteModal.addEventListener("shown.bs.modal", function () {
    console.log("Modal opened!");
  });
}

// Permanent Delete

const modal = document.getElementById("permanentDeleteModal");

if (modal) {
  modal.addEventListener("show.bs.modal", function (event) {
    const button = event.relatedTarget;

    const id = button.getAttribute("data-id");
    const name = button.getAttribute("data-name");

    document.getElementById("deleteName").textContent = name;

    document.getElementById("permanentDeleteBtn").href = "/strongDelete/" + id;
  });
}

// delete all permanent
const deleteAllmodal = document.getElementById("permanentDeleteAllModal");

if (deleteAllmodal) {
  deleteAllmodal.addEventListener("show.bs.modal", function () {
    document.getElementById("permanentAllDeleteBtn").href = "/deleteAll/";
  });
}
