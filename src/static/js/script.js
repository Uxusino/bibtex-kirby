// Get elements
const modal = document.getElementById("modal");
const openModalButtons = document.querySelectorAll(".bibtex-title");
const closeModalButton = document.querySelector(".close");
const modalBody = document.getElementById("modal-body");
const leftBlock = document.getElementById("left-block");
const rightBlock = document.getElementById("right-block");
const modalId = document.getElementById("modal-bibtex-id");

const copyButtons = document.querySelectorAll(".copy-btn");
const copyAllButton = document.getElementById("fetch-btn");

const fields = {
  "article": ["title", "author", "journal", "year", "volume", "number",
    "pages", "doi", "url"
  ],
  "book": ["title", "author", "publisher", "year", "editor", "volume",
    "series", "number", "address", "edition", "month", "note", "isbn"
  ],
  "inproceedings": ["title", "author", "booktitle", "year", "editor",
    "volume", "number", "series", "pages", "address", "month",
    "organization", "publisher", "note", "doi"
  ],
  "misc": ["title", "author", "howpublished", "year", "note", "key", "url"]
};

const requiredFields = ["title", "author", "journal", "year", "publisher",
  "booktitle", "howpublished"
];

async function fetchReferences() {
  try {
    const response = await fetch('/get_all');
    const data = await response.text();
    return data;
  } catch (error) {
    console.error('Error while fetching references:', error);
  }
}

function addModalFields(key, value) {
  const name = document.createElement("label");
  const content = document.createElement("input");

  name.textContent = `${key}`;

  content.value = `${value}`;
  content.name = `${key}`;
  content.className = "modal-input-content";
  if (requiredFields.includes(key)) {
    content.required = true;
  }

  leftBlock.appendChild(name);
  rightBlock.appendChild(content);
}

// Each bibtex title can open modal
openModalButtons.forEach(button => {
    button.addEventListener("click", () => {
        const data = JSON.parse(button.getAttribute("data-bibtex"));
        const id = button.getAttribute("data-id");
        const type = button.getAttribute("data-type");

        leftBlock.innerHTML = "";
        rightBlock.innerHTML = "";

        const keys = fields[type];

        keys.forEach(k => {
            if (data[k]) {
              addModalFields(k, data[k]);
            }
            else {
              addModalFields(k, "");
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

// event for copy button
copyButtons.forEach(button => {
  button.addEventListener("click", function() {
    const textToCopy = button.getAttribute('data-bibtex');

    navigator.clipboard.writeText(textToCopy)
      .then(() => {
        alert(".bib copied to clipboard");
      })
      .catch(err => {
        console.error("Error while copying .bib: ", err);
      });
  });
});

copyAllButton.addEventListener("click", async function() {
  const data = await fetchReferences();
  navigator.clipboard.writeText(data)
    .then(() => {
      alert("Bibliography copied to clipboard");
    })
    .catch(err => {
      console.error("Error while copying bibliography: ", err)
    });
});
// Listener for sorting by tags
document.addEventListener("DOMContentLoaded", function() {
  const filterTags = document.querySelectorAll("#filter-tags .tag");
  const bibtexItems = document.querySelectorAll(".bibtex-item");
  console.log(filterTags);
  // Array for storing tags
  let selectedTags = [];
  // Function for filtering references
  function filterBibtexItems() {
    bibtexItems.forEach(item => {
      const itemTags = item.getAttribute("data-tags") ? item.getAttribute("data-tags").split(",") : [];
      
      const trimmedTags = itemTags.map(tag => tag.trim());
      const matches = selectedTags.every(tag => trimmedTags.includes(tag));
      console.log("Item Tags:", trimmedTags, "Selected Tags:", selectedTags, "Matches:", matches);
      // Show or hide by tags
      if (matches) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });
  }
  filterTags.forEach(tag => {
    tag.addEventListener("click", function() {
      const tagText = this.getAttribute("data-tag").trim();
      console.log("Obtained tag:", tagText);
      // Select or deselect tag
      if (selectedTags.includes(tagText)) {
        selectedTags = selectedTags.filter(t => t !== tagText);
        this.classList.remove("selected");
      } else {
        selectedTags.push(tagText);
        this.classList.add("selected");
      }
      filterBibtexItems();
      // If no tag is selected, show everything
      if (selectedTags.length == 0) {
        bibtexItems.forEach(item => {
          item.style.display = "block";
        });
      }
    });
  });
});