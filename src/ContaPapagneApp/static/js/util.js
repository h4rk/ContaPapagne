function switchTipoMovimento() {
	// Recupera il valore dello switch per la tipologia di movimento
	// true = entrata
	// false = uscita
	let type = document.getElementById("tipologia_movimento");
	if (type.checked) {
		//applicare stile entrata al form
		document.getElementById('risarcimento_movimento').removeAttribute('disabled');
	} else {
		//applicare stile uscita al form
		document.getElementById('risarcimento_movimento').setAttribute('disabled', '');
	}
}

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
		return new bootstrap.Tooltip(tooltipTriggerEl);
	})

function toggleTooltipVisibility() {
	var tooltipContainer = document.getElementById("tooltip-container");

	if (tooltipContainer.classList.contains("hide")) {
		tooltipContainer.classList.remove("hide");
	} else {
		tooltipContainer.classList.add("hide");
	}
}

function boldTipologia() {
	var uscita = document.getElementById("uscita");
	var entrata = document.getElementById("entrata");
	var checkbox = document.getElementById("tipologia_movimento");

	if (checkbox.checked) {
		checkbox.classList.remove("highlight-checkbox")
		entrata.classList.add("highlight");
		entrata.classList.remove("hide");
		uscita.classList.remove("highlight");
		uscita.classList.add("hide");

	} else {
		checkbox.classList.add("highlight-checkbox")
		uscita.classList.add("highlight");
		uscita.classList.remove("hide");
		entrata.classList.remove("highlight");
		entrata.classList.add("hide");
	}
}

function cleanCategorieAndDropdown() {
	document.getElementById('multiDropdown').textContent='';
	document.getElementById('multiBox').textContent='';
	document.getElementById('multiRicerca').value='';
	document.getElementById('categorie_movimento').textContent='';
}

function formTypeSwitchWrapper(e) {
	switchTipoMovimento();
	toggleTooltipVisibility();
	boldTipologia();
	//cleanCategorieAndDropdown();
}