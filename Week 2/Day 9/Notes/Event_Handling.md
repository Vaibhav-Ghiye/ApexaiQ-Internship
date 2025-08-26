***

## What is an Event?

- An **event** is an action or occurrence that happens in the browser, which the browser can detect and respond to. 

- Events are typically triggered by user interactions such as clicking, typing, or moving the mouse, but can also be system-generated, such as when a page loads or when an animation completes.

***

## What is Event Handling?

**Event handling** is the process by which JavaScript listens for and responds to events. Developers write *event handlers* (functions) that execute when specific events occur. This makes web pages interactive and responsive.

- **Event Listener:** A function attached to an element that waits for a particular event.
- **Event Object:** An object passed to event handlers that contains details about the event, such as the element that triggered it and the type of event.

Example:
```js
const btn = document.getElementById('myButton');
btn.addEventListener('click', function(event) {
  alert('Button clicked!');
  console.log('Event type:', event.type);
});
```

***

## Common Types of Events in JavaScript

### 1. Mouse Events
Triggered by mouse actions.
- **click:** When the mouse button is clicked.
- **dblclick:** Double-click.
- **mouseover:** Mouse pointer moves over an element.
- **mouseout:** Mouse pointer leaves the element.
- **mousemove:** Mouse moves within an element.

Example:
```js
element.addEventListener('click', () => console.log('Clicked!'));
```
___ 
### 2. Keyboard Events
Triggered by keyboard actions.
- **keydown:** When a key is pressed down.
- **keypress:** When a key is pressed and produces a character.
- **keyup:** When a key is released.

Example:
```js
document.addEventListener('keydown', event => console.log(`Key pressed: ${event.key}`));
```
___ 

### 3. Form Events
Triggered by form actions.
- **submit:** When a form is submitted.
- **change:** When an input value changes.
- **focus:** When an element gains focus.
- **blur:** When an element loses focus.

Example:
```js
form.addEventListener('submit', event => {
    event.preventDefault(); // Prevent form submission
  console.log('Form submitted!');
});
```

___

### 4. Window Events
Occur on the browser window.
- **load:** When the page has fully loaded.
- **resize:** When the window is resized.
- **scroll:** When the page is scrolled.
- **unload:** When the user leaves the page.

Example:
```js
window.addEventListener('resize', () => console.log('Window resized'));
```
***
