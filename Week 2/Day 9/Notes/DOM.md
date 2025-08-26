

***

## What is DOM?

The **Document Object Model (DOM)** is a hierarchical, object-oriented representation of a web page. It acts as a programming interface that represents the structure, style, and content of HTML or XML documents as a tree of nodes (elements, text, attributes, etc.). This allows programming languages like JavaScript to access, modify, and interact with the web page dynamically.

Each element in the HTML page becomes a **node** in the DOM tree, with properties and methods for interacting with it programmatically.

***

## Why is DOM Important?

- **Dynamic Interaction:** DOM allows JavaScript to dynamically change the content, structure, and styles of a webpage after it has loaded without reloading the page.

- **Event Handling:** Enables responding to user actions like clicks, input, and keyboard events.

- **Web Application Foundation:** Provides the essential interface for building interactive, responsive web apps.


- **Access and Manipulation:** Provides standardized methods to create, delete, or update elements, attributes, and text nodes.

***

## DOM Manipulation Methods

### Accessing Elements

- **`getElementById(id)`**: Returns the element with the specified ID.
```js
const header = document.getElementById("main-header");
```
___

- **`getElementsByClassName(className)`**: Returns a live HTMLCollection of elements with the given class name.
```js
const items = document.getElementsByClassName("list-item");
```
___

- **`getElementsByTagName(tagName)`**: Returns a live HTMLCollection of elements with the given tag name.
```js
const paragraphs = document.getElementsByTagName("p");
```
___

- **`querySelector(selector)`**: Returns the first element that matches a CSS selector.
```js
const firstButton = document.querySelector(".btn");
```
___

- **`querySelectorAll(selector)`**: Returns a static NodeList of all elements matching the CSS selector.
```js
const allButtons = document.querySelectorAll(".btn");
```
___

### Creating and Inserting Elements

- **`createElement(tagName)`**: Creates a new element node.
```js
const newDiv = document.createElement("div");
```
___

- **`appendChild(node)`**: Adds a child node to an element.
```js
document.body.appendChild(newDiv);
```
___

- **`insertBefore(newNode, referenceNode)`**: Inserts a node before a reference node.
```js
parentNode.insertBefore(newNode, existingChild);
```
___

### Modifying Elements

- **`element.textContent`**: Sets or gets the text content of an element.
```js
header.textContent = "New Header";
```
___

- **`element.innerHTML`**: Sets or gets the HTML content inside an element.
```js
div.innerHTML = "<p>Hello World</p>";
```
___

- **`setAttribute(name, value)`**: Adds or changes an attribute of an element.
```js
button.setAttribute("disabled", "true");
```
___

- **`removeAttribute(name)`**: Removes an attribute.
```js
button.removeAttribute("disabled");
```
___

- **`classList`**: Manipulate CSS classes.
```js
element.classList.add("active");
element.classList.remove("hidden");
element.classList.toggle("visible");
```

___
### Removing Elements

- **`removeChild(childNode)`**: Removes a child node from an element.
```js
parentElement.removeChild(childElement);
```
___

- **`element.remove()`**: Removes the element itself from the DOM.
```js
element.remove();
```
___

### Event Handling

- **`addEventListener(event, handler)`**: Attaches an event listener to an element.
```js
button.addEventListener("click", () => alert("Clicked!"));
```
___

- **`removeEventListener(event, handler)`**: Removes an event listener.
```js
button.removeEventListener('click', handleClick);
```

***
