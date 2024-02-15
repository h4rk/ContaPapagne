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