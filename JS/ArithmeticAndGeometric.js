const getFirstElementValu = () => {
	return parseFloat(document.querySelector("#first-element").value);
};

const getSecondElementValu = () => {
	return parseFloat(document.querySelector("#second-element").value);
};

const getNumberOfElements = () => {
	return parseInt(document.querySelector("#number-elements").value);
};

const getArithmetic = () => {
	return document.querySelector("#arithmetic").value;
};

const getGeometric = () => {
	return document.querySelector("#geometric").value;
};
//------------------------------------------------------------------------
//Tu robie listy
//------------------------------------------------------------------------

const generateAnArithmeticSequence = () => {
	const lst = [];
	let element = getFirstElementValu();
	let howMuchItChanges = getSecondElementValu() - element;
	for (let i = 0; i < getNumberOfElements(); i++) {
		lst.push(element);
		element += howMuchItChanges;
	}
	return lst;
};

const generateAnGeometricSequence = () => {
	const lst = [];
	let element = getFirstElementValu();
	let howMuchItChanges = getSecondElementValu() / element;
	for (let i = 0; i < getNumberOfElements(); i++) {
		lst.push(element);
		element *= howMuchItChanges;
	}
	return lst;
};

//------------------------------------------------------------------------
// Tu generuje piekne div na podstawie otrzymanej listy
//------------------------------------------------------------------------
const cleanNewDiv = () => {
	let allNewDivs = document.querySelectorAll(".new-div");
	allNewDivs.forEach((element) => element.remove());
};

const generateDivs = () => {
	cleanNewDiv();

	const isArithmeticSelected = document.querySelector("#arithmetic").checked;
	const isGeometricSelected = document.querySelector("#geometric").checked;

	if (isArithmeticSelected) {
		lst = generateAnArithmeticSequence();
	} else if (isGeometricSelected) {
		lst = generateAnGeometricSequence();
	}

	const elementsDiv = document.querySelector("#elements");
	lst.forEach((element) => {
		let newDiv = document.createElement("div");
		newDiv.className = "new-div";
		newDiv.textContent = element;
		elementsDiv.appendChild(newDiv);
	});
};

calculate.addEventListener("click", generateDivs);
//------------------------------------------------------------------------
