// Get elements
const modal = document.getElementById("modal");
const openModalButtons = document.querySelectorAll(".bibtex-title");
const closeModalButton = document.querySelector(".close");
const modalBody = document.getElementById("modal-body");
const leftBlock = document.getElementById("left-block");
const rightBlock = document.getElementById("right-block");
const modalId = document.getElementById("modal-bibtex-id");

function addModalFields(key, jsondata) {
  const name = document.createElement("label");
  const content = document.createElement("input");

  name.textContent = `${key}`;

  content.value = `${jsondata[key]}`;
  content.name = `${key}`
  content.className = "modal-input-content";

  leftBlock.appendChild(name);
  rightBlock.appendChild(content);
}

// Each bibtex title can open modal
openModalButtons.forEach(button => {
    button.addEventListener("click", () => {
        const data = JSON.parse(button.getAttribute("data-bibtex"));
        const id = button.getAttribute("data-id");

        leftBlock.innerHTML = "";
        rightBlock.innerHTML = "";

        const orderedKeys = ['title', 'author'];

        // Puts title and author first
        orderedKeys.forEach(k => {
            if (data[k]) {
                addModalFields(k, data);
            }
        });

        Object.entries(data).forEach(([k, v]) => {
            if (!orderedKeys.includes(k)) {
                addModalFields(k, data);
            }
        });

        modalId.value = id;
        modal.style.display = "block";
    })
});

// Close modal by clicking "x"
closeModalButton.addEventListener("click", () => {
  modal.style.display = "none";
});

// Close modal by clicking outside the window
window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});