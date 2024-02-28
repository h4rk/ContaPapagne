function getDeleteSpan() {
	let deleteSpan = document.createElement('span');
	deleteSpan.setAttribute('class', 'deleteSpan');
	deleteSpan.textContent = 'x';
	return deleteSpan;
}

function addCategoryToMulti(e) {
	//Recupero il multiBox, ovvero l'elemento che contiene graficamente le categorie
	const box = document.getElementById("multiBox");

	//Recupero categorie_movimento, ovvero l'elemento select che contiene le options selezionate
	// ossia quelle che si trovano in ogni momento nel multiBox
	const input = document.getElementById("categorie_movimento");

	//Recupero la sorgente dell'evento, ovvero il div che contiene la categoria da aggiungere
	// nel multiBox e in categorie_movimento. Creo un clone, rimuovo l'attributo onclick
	// e aggiungo un eventListener per il click di rimozione
	let dx = e.target.cloneNode(true);
	//dx.appendChild(getDeleteSpan()); //TODO Ragionare uslla X per rimuovere
	dx.removeAttribute('onclick');
	dx.id = dx.id+'_box'
	dx.addEventListener('click', removeCategoryFromMulti);

	//Creo il nuovo elemento option da inserire nel select
	let ix = document.createElement('option');
	ix.setAttribute('value', e.target.getAttribute('id'));
	ix.setAttribute('id',e.target.getAttribute('id')+'_opt');
	ix.setAttribute('selected', 'selected');

	//Aggiungo la nuova categoria al multiBox
	box.appendChild(dx);
	//Aggiungo la nuova categoria al categorie_movimento
	input.appendChild(ix);
	//Disabilito il result clickato per non permettere doppioni
	e.target.classList.add('hidden');
}

function removeCategoryFromMulti(e) {
	//Recupero il multiBox, ovvero l'elemento che contiene graficamente le categorie
	const box = document.getElementById("multiBox");

	//Recupero il multiInput, ovvero l'elemento select che contiene le options selezionate
	// ossia quelle che si trovano in ogni momento nel multiDiv
	const input = document.getElementById("categorie_movimento");

	//Riporto visibile l'elemento nella dropdown
	let tempId = e.target.id.replace('_box', '');
	let dd = document.getElementById(tempId);
	if (dd !== null) {
		dd.classList.remove('hidden');
	}
	//Rimuovo l'option corrispondente dalla select
	input.removeChild(document.getElementById(tempId+'_opt'));
	
	//Rimuovo la categoria dal multiBox
	box.removeChild(document.getElementById(e.target.getAttribute('id')));
}

window.addEventListener("load", function() {
	document.body.addEventListener("htmx:afterSettle", function(afterSwapEvent) {
		if(afterSwapEvent.target.id=='multiDropdown') {
			console.log('Check alredy selected:');

			let listSel = document.getElementById('multiBox').children;
			let listRes = document.getElementById('multiDropdown').children;

			for(let sel of listSel) {
				for(let res of listRes) {
					if(sel.id.replace('_box', '') == res.id) {
						//res.classList.add('hidden');
						document.getElementById(res.id).classList.add('hidden');
						console.log('Adding hidden to ' + res.id);
					}
				}
			}
		}
	});
	document.body.addEventListener('htmx:configRequest', function(configRequestEvent) {
		if(configRequestEvent.target.id=='multiRicerca') {
			configRequestEvent.detail.parameters['tipo_movimento'] = document.getElementById('tipologia_movimento').checked;
		}
	});
})
