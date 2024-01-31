//Funzione di callback da passare come parametro all'event listener dello switch
// per passare da form entrate a form uscite
switchForm = function switchForm() {
	var formContainer = document.getElementById('form-container');
	var formTitle = document.getElementById('form-title');
	var submitBtn = document.getElementById('submit-btn');

	if(this.checked) {
		formContainer.className = 'form-container income-form';
		formTitle.innerText = 'Income Form';
		submitBtn.className = 'submit-btn income-btn';
		submitBtn.innerText = 'Add Income';
	} else {
		formContainer.className = 'form-container expenses-form';
		formTitle.innerText = 'Expenses Form';
		submitBtn.className = 'submit-btn expenses-btn';
		submitBtn.innerText = 'Add Expense';
	}
}