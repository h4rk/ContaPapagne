/**
 * Option object for multiselect
 */
export class Option {
    #id
    #value
    #selected
    #selectId

    /**
     * If the selector is invalid, don't create the object.
     * If the object alredy exist in the DOM, make it selected
     * Otherwise, create a new object
     * @param {number} id - id of the option element
     * @param {string} value - the text content ot the option element
     * @param {string} selectId - CSS selector got the select obj in the DOM
     * @throws {InternalError} - Argument selectId must be valid anc existing css identifier
     */
    constructor(id, value, selectId) {
        if(document.getElementById(selectId) === null) {
            throw InternalError("Invalid selector: " + selectId);
        } else if(document.getElementById(selectId).querySelector('#'+id)===null) {
            let x = document.getElementById(selectId).querySelector('#'+id);
            this.#id = id;
            this.#value = value;
            this.#selectId = selectId;
            this.#selected = true;
        }
        else {
            this.#id = id;
            this.#value = value;
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
     * @returns HTMLOptionElement
     */
    #renderOption() {
        let t = document.createElement('option');
        t.setAttribute('id', this.#id);
        t.setAttribute('selected', 'selected');
        t.innerText = this.#value;
    }

    renderDiv(){
        // TODO
    }
}