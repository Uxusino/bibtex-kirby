// Get elements
const modal = document.getElementById("modal");
const openModalButtons = document.querySelectorAll(".bibtex-title");
const closeModalButton = document.querySelector(".close");
const modalBody = document.getElementById("modal-body")

// Each bibtex title can open modal
openModalButtons.forEach(button => {
    button.addEventListener("click", () => {
        const data = JSON.parse(button.getAttribute("data-bibtex"));

        modalBody.innerHTML = "";

        const orderedKeys = ['title', 'author'];

        // Puts title and author first
        orderedKeys.forEach(k => {
            if (data[k]) {
                const paragraph = document.createElement("p");
                paragraph.textContent = `${k}: ${data[k]}`;
                modalBody.appendChild(paragraph);
            }
        });

        Object.entries(data).forEach(([k, v]) => {
            if (!orderedKeys.includes(k)) {
                const paragraph = document.createElement("p");
                paragraph.textContent = `${k}: ${v}`;
                modalBody.appendChild(paragraph);
            }
        });

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