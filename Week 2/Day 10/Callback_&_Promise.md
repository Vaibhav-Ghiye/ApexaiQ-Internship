# Callback

- A **callback** in JavaScript is a function passed as an argument to another function, which then executes the callback after completing its own operations. 

- Callbacks are used to ensure that a certain code runs only after a particular task is finished, especially useful for dealing with asynchronous operations like server responses, timers, or events.

***

## Why Use Callbacks?

- **Sequencing Tasks:** Callbacks help control the order of execution, especially when dealing with code that doesn’t finish instantly.

- **Asynchronous Programming:** They allow code to run without blocking the main execution thread, enabling smooth user experiences and efficient programs.
- **Custom Handling:** Developers can define what happens next after an operation by passing different callback functions.

***

## Example

```js
function greet(name, callback) {
  console.log("Hello, " + name);
  callback();
}
function sayBye() {
  console.log("Goodbye!");
}
greet("Alex", sayBye);

// Output:
// Hello, Alex
// Goodbye!
```



***

## Advantages

- Allows **non-blocking** (asynchronous) code execution.
- Enables flexible, reusable, and modular code design.
- Makes it easy to define custom steps after tasks complete (success, error, etc.).

***

## Disadvantages

- **Callback Hell:** Deeply nested callbacks (many inside each other) can make code hard to read and maintain.

- **Error Handling:** Handling errors across callbacks can be complicated and messy.
- **Debugging Difficulty:** Tracing bugs and following program flow is tougher in complex callback chains.

***
***
# Promise

- A **Promise** in JavaScript is an object that represents the eventual result of an asynchronous operation. 

- It lets you write cleaner, more manageable asynchronous code by providing a way to handle success or failure without deep nesting of callbacks.

***

## Promise States

1. **Pending**: The initial state, where the operation has neither completed nor failed yet.
2. **Fulfilled (Resolved)**: The operation completed successfully, and the promise has a result.
3. **Rejected**: The operation failed, and the promise has an error as its result.

***

## Why Use Promises?

- Promises help avoid "callback hell" by flattening nested asynchronous code and making it easier to read and maintain.
- They allow chaining, so multiple async operations can be handled in sequence.
- Error handling becomes simpler with `.catch()`.

***

## Example

```js
let promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    let success = true;
    if (success) {
      resolve("Operation successful!");
    } else {
      reject("Something went wrong.");
    }
  }, 1000);
});

promise
  .then(result => console.log(result))     // Handles fulfilled state
  .catch(error => console.error(error));   // Handles rejected state
```
**Output after 1 second:**  
`Operation successful!` if `success` is true; otherwise logs the error.

***
