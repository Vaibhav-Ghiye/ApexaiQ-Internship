# Async & Await

**Async** and **await** are modern JavaScript keywords that simplify handling asynchronous code using Promises, making it cleaner and easier to read.

***

## What Is It?

- **async** — Placed before a function declaration, it turns the function into an asynchronous function, which always returns a Promise.
- **await** — Used inside async functions; pauses the execution of the function until a Promise is resolved or rejected, acting like "wait here for the value.

***

## Why and When to Use

- Use async/await to write asynchronous code that looks and behaves more like synchronous code, avoiding deeply nested `.then()` chains (promise chaining).
- Great for scenarios where you have to perform several asynchronous operations in sequence or handle errors with `try...catch`.

***

## Example

```js
async function fetchData() {
  try {
    let response = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    let data = await response.json();
    console.log(data);
  } catch (err) {
    console.error("Error fetching data:", err);
  }
}
fetchData();
```

Here, `await` pauses the function until the fetch is complete and the result is available. This makes the code more readable and easier to debug compared to traditional promise handling with .then() and .catch().

***
***

# Closure

A **closure** in JavaScript is a function that remembers and accesses variables from its outer (enclosing) function’s scope even after the outer function has finished executing. This lets the inner function “close over” its context, retaining access to the variables it needs.

***

## Why Use Closures?

- **Data Privacy:** Variables in the outer function cannot be accessed directly from outside, but can be accessed and manipulated by the inner function. This helps create private variables in JavaScript.
5- **Stateful Functions:** Closures help maintain state across multiple invocations.
- **Callbacks & Event Handlers:** Closures are commonly used in asynchronous JavaScript and event handling to remember context or data.

***

## Example

```js
function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  }
}

let counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```
Here, the returned function is a closure. It remembers the `count` variable, and each call to `counter()` increases and returns the new value—even though `makeCounter` has already finished running.

***

### Key points

- **Lexical Scope:** Closures rely on lexical scoping, meaning they capture variables available where the function was defined, not where it’s called.[4][6]
- **Applications:** Useful for creating private data, partial function application, currying, and maintaining state (such as event listeners, timers, or factory functions).

Closures are one of JavaScript’s most powerful and foundational features, enabling data encapsulation and advanced functional patterns.


***
