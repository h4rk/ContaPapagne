function getDeleteSpan() {
	let deleteSpan = document.createElement('span');
	deleteSpan.setAttribute('class', 'deleteSpan');
	deleteSpan.text('x');
	return deleteSpan;
}

function addCategoryToMulti(e) {
	console.log('addCategoryToMulti' + JSON.stringify(e.target));
	//Recupero il multiDiv, ovvero l'elemento che contiene graficamente le categorie
	const div = document.getElementById("multiDiv");

	//Recupero il multiInput, ovvero l'elemento select che contiene le options selezionate
	// ossia quelle che si trovano in ogni momento nel multiDiv
	const input = document.getElementById("multiInput");

	//Recupero la sorgente dell'evento, ovvero il div che contiene la categoria da aggiungere
	// nel multiDiv e nel multiInput
	const catDiv = e.target;

	//Creo il nuovo elemento da inserire nel multiDiv
	let dx = catDiv;
	dx.appendChild(getDeleteSpan());

	//Creo il nuovo elemento option da inserire nel select
	let ix = document.createElement('option');
	ix.text=catDiv.querySelector('span').text;
	ix.setAttribute('id',catDiv.getAttribute('id'));

	//Aggiungo la nuova categoria al multiDiv
	div.appendChild(dx);
	//Aggiungo la nuova categoria al multiInput
	input.appendChild(ix);
}

function removeCategoryFromMulti(e) {
	//Recupero il multiDiv, ovvero l'elemento che contiene graficamente le categorie
	const div = document.getElementById("multiDiv");

	//Recupero il multiInput, ovvero l'elemento select che contiene le options selezionate
	// ossia quelle che si trovano in ogni momento nel multiDiv
	const input = document.getElementById("multiInput");

	//Recupero la sorgente dell'evento, ovvero il div che contiene la categoria da aggiungere
	// nel multiDiv e nel multiInput
	const category = e.target.value;

	//Rimuovo la categoria dal multiDiv
	div.removeChild(div.getElementById(category.id));
	//Rimuovo l'option corrispondente dalla select
	input.removeChild(input.getElementById(category.id));
}