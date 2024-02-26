function getDeleteSpan() {
	let deleteSpan = document.createElement('span');
	deleteSpan.setAttribute('class', 'deleteSpan');
	deleteSpan.textContent = 'x';
	return deleteSpan;
}

function addCategoryToMulti(e) {
	console.log('addCategoryToMulti' + e.target.value);
	//Recupero il multiBox, ovvero l'elemento che contiene graficamente le categorie
	const box = document.getElementById("multiBox");

	//Recupero categorie_movimento, ovvero l'elemento select che contiene le options selezionate
	// ossia quelle che si trovano in ogni momento nel multiBox
	const input = document.getElementById("categorie_movimento");

	//Recupero la sorgente dell'evento, ovvero il div che contiene la categoria da aggiungere
	// nel multiBox e in categorie_movimento e 
	//creo il nuovo elemento da inserire nel multiBox
	let dx = e.target.cloneNode(true);
	dx.appendChild(getDeleteSpan());
	dx.addEventListener('click', removeCategoryFromMulti);

	//Creo il nuovo elemento option da inserire nel select
	let ix = document.createElement('option');
	ix.setAttribute('value', e.target.getAttribute('id'));
	ix.setAttribute('id',e.target.getAttribute('id')+'_opt');

	//Aggiungo la nuova categoria al multiBox
	box.appendChild(dx);
	//Aggiungo la nuova categoria al categorie_movimento
	input.appendChild(ix);
	//Disabilito il result clickato per non permettere doppioni
	// TODO rimuovere eventHandler? 
	e.target.setAttribute('disabled', true);
	e.target.removeAttribute('onclick');
}

function removeCategoryFromMulti(e) {
	//Recupero il multiDiv, ovvero l'elemento che contiene graficamente le categorie
	const div = document.getElementById("multiBox");

	//Recupero il multiInput, ovvero l'elemento select che contiene le options selezionate
	// ossia quelle che si trovano in ogni momento nel multiDiv
	const input = document.getElementById("categorie_movimento");

	//Recupero la sorgente dell'evento, ovvero il div che contiene la categoria da aggiungere
	// nel multiDiv e nel multiInput
	const category = e.target;

	//Rimuovo la categoria dal multiDiv
	div.removeChild(div.getElementById(category.id));
	//Rimuovo l'option corrispondente dalla select
	input.removeChild(input.getElementById(category.id));
	//TODO Riattivare event sulla dropdown se esiste id
}