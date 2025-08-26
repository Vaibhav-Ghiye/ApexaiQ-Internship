
***

## What is a Function?

A **function** is a reusable block of code designed to perform a particular task. Functions take inputs (parameters), process them, and can return a result. They help organize code and avoid repetition.

***

## Key Concepts Related to Functions

### Parameters & Arguments
- **Parameters** are named placeholders declared in the function definition.
- **Arguments** are the actual values passed when calling the function.
```js
function greet(name) { // 'name' is a parameter
  console.log("Hello " + name);
}
greet("Alex"); // "Alex" is an argument
```

### Return Statement
- The `return` keyword outputs a value from the function and ends its execution.
```js
function square(num) {
  return num * num;
}
console.log(square(4)); // 16
```
If no `return` is specified, the function returns `undefined`.

### Scope
- Functions create a **local scope** for variables declared inside them.
- Variables inside a function are not accessible outside.
- Functions can access variables from outer (parent) scopes but not vice versa.

```js
let globalVar = 10;

function testScope() {
  let localVar = 20;
  console.log(globalVar); // 10 (accessible)
}

console.log(localVar); // Error: localVar is not defined
```

### Function Hoisting
- Function declarations are hoisted, meaning they can be called before they are defined.
- Function expressions and arrow functions are not hoisted.

***

## Types of Functions with Examples

### 1. Function Declaration 
Defined with the `function` keyword, can be called before declaration (hoisted).
```js
function add(a, b) {
  return a + b;
}
console.log(add(2, 3)); // 5
```

### 2. Function Expression
A function assigned to a variable. Not hoisted.
```js
const multiply = function(a, b) {
  return a * b;
}
console.log(multiply(2, 3)); // 6
```

### 3. Arrow Function 
Shorter syntax, does not have its own `this`.
```js
const divide = (a, b) => a / b;
console.log(divide(6, 2)); // 3
```
With multiple statements:
```js
const greet = name => {
  console.log("Hello " + name);
}
```

### 4. Anonymous Function
Function without a name, often used as function expressions or callbacks.
```js
setTimeout(function() {
  console.log("Executed after 1 second");
}, 1000);
```

### 5. Immediately Invoked Function Expression (IIFE)
A function that runs immediately after it’s defined.
```js
(function() {
  console.log("IIFE runs instantly");
})();
```

### 6. Higher-Order Function
Takes other functions as arguments or returns them.
```js
function operation(a, b, func) {
  return func(a, b);
}
function subtract(x, y) {
  return x - y;
}
console.log(operation(5, 3, subtract)); // 2
```

### 7. Recursive Function
Calls itself to solve smaller instances of a problem.
```js
function factorial(n) {
  if (n === 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(5)); // 120
```

***
