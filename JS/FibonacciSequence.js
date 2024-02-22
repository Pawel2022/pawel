const getFibonacciNumbersOFElements = () => {
	return parseInt(document.querySelector("#fibonacci-number").value);
};

const generateFibonacciSequences = document.querySelector(
	"#generateFibonacciSequences"
);

const fibonacciSequenceList = () => {
	const fibonacci = [0, 1];
	for (let i = 2; i < getFibonacciNumbersOFElements(); i++) {
		fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
        fibonacci.push(fibonacci[i]);
	}
    return fibonacci
};

const cleanNewDiv = () => {
	let allNewDivs = document.querySelectorAll(".new-div");
	allNewDivs.forEach((element) => element.remove());
};

const generateDivs = () => {
	cleanNewDiv();

	lst = fibonacciSequenceList();
	const elementsDiv = document.querySelector("#elements");
	lst.forEach((element) => {
		let newDiv = document.createElement("div");
		newDiv.className = "new-div";
		newDiv.textContent = element;
		elementsDiv.appendChild(newDiv);
	});
};

generateFibonacciSequences.addEventListener("click", generateDivs);
