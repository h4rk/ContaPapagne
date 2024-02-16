/**
 * Option object for multiselect
 */
class Option {
    #id
    #value
    #selected
	#color
    #selectId

    /**
     * If the selector is invalid, don't create the object.
     * If the object alredy exist in the DOM, make it selected
     * Otherwise, create a new object
     * @param {number} id - id of the option element
     * @param {string} value - the text content ot the option element
     * @param {string} color - Hex value for the color for the specific category/user combination
     * @param {string} selectId - CSS selector got the select obj in the DOM
     * @throws {InternalError} - Argument selectId must be valid anc existing css identifier
     */
    constructor(id, value, color, selectId) {
        if(document.getElementById(selectId) === null) {
            throw new Error("Invalid selector: " + selectId);
        } else if(document.getElementById(selectId).querySelector('#o'+id)!==null) {
            let x = document.getElementById(selectId).querySelector('#o'+id);
            this.#id = id;
            this.#value = value;
			this.#color = color;
            this.#selectId = selectId;
            this.#selected = true;
        }
        else {
            this.#id = id;
            this.#value = value;
			this.#color = color;
            this.#selectId = selectId;
            this.#selected = false;
        }
    }

    /**
     * Getter for the selected attribute
    * @returns {boolean} True if option is selected otherwise false 
     */
    isSelected() {
        return this.#selected;
    }

    /**
     * Set selected to true and append option to the linked select element on the DOM
     */
    select() {
        if(!this.#selected) {
            this.#selected = true;
            this.#addToOption(this.#selectId);
        }
    }

    /**
     * Setter for the selected attribute
     * @param {boolean} selected - the boolean value to assign
     */
    deselect() {
        if(this.#selected) {
            this.#selected = false;
            this.#removeFromOption();
        }
    }

    /**
     * If not alredy added, adds the element to the options in the DOM and sets selected to true
     */
    #addToOption(){
        document.getElementById(this.#selectId).appendChild(this.#renderOption());
    }

    /**
     * If present, removes the element from the options in the DOM and sets selected to false
     */
    #removeFromOption(){
        document.getElementById(this.#selectId).removeChild(
            document.getElementById(this.#selectId).querySelector('#'+this.#id));
    }

    /**
     * Getter for the id attribute
     * @returns {number} The value of id
     */
    get id() {
        return this.#id;
    }

    /**
     * Getter for the value attribute
     * @returns {string} The value of value
     */
    get value() {
        return this.#value;
    }

    /**
     * render the Option
     * @returns {HTMLOptionElement}
     */
    #renderOption() {
        let t = document.createElement('option');
        t.setAttribute('id', this.#id);
        t.setAttribute('value', this.#id);
        t.setAttribute('selected', 'selected');
        t.innerText = this.#value;
        return t;
    }

    /**
     * render the div version of the option with classes for styling
     * @returns {HTMLDivElement}
     */
    renderDiv(){
        let t = document.createElement('div');
        t.setAttribute('id', this.#id);
        t.setAttribute('class', 'category');
		t.setAttribute('style', 'background-color: ' + this.#color);
		let p = document.createElement('span');
		p.innerText = this.#value;
		let m = document.createElement('span');
		m.innerText = 'X';
		//m.setAttribute('onClick', )
		t.appendChild(document.createElement('span'))
		t.appendChild(p);
		t.appendChild(m);
        return t;
    }
}

/**
 * Class responsible for handling the Options
 * @param {[]} options - A list of options
 * @param {string} - The CSS selector for the related select DOM element
 */
class Select {
	#optionMap = new Map();
	#selectId;
	constructor(options, selectId){
		options.forEach(x => {
			console.log(x);
			this.#optionMap.set(x.id_categoria, new Option(x.id_categoria, x.nome, x.colore, selectId));
		});
		console.log(this.#optionMap);
		this.#selectId = selectId;
	}

	/**
	 * 
	 * @param {Event} e - The source event
	 */
	handleEvent(e) {
		switch(e.type) {
			case "click":
				this.#handleUnselect(e);
			default:
				console.log('Unhandled event type: ' + e.type);
		}
	}

	/**
	 * 
	 * @param {Event} e - The source event
	 */
	#handleUnselect(e){
		console.log(this.#optionMap.get(e.target.id));
	}

	render(){
		const x = document.createElement('div');
		this.#optionMap.forEach((v, k) => {
			x.appendChild(v.renderDiv());
			document.getElementById(this.#selectId).appendChild(v.render());
		});
		x.setAttribute('id', 'wrapper');
		document.getElementById(this.#selectId).appendChild()
		return x;
	}
}

// TEST
function test() {
	const options = [{id_categoria: 1, nome: 'Cat1', colore: '#ffff11'}, {id_categoria: 2, nome: 'Cat2', colore: '#ffff22'}];
	const select = new Select(options, 'test-select');
	document.getElementById('container').appendChild(select.render());
}