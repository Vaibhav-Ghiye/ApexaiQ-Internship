
## What is JavaScript?

- **JavaScript** is a versatile scripting and programming language primarily used to add interactivity, dynamic content, and advanced features to web pages.

- It enables actions like form validation, animations, and responding to user events, making websites more engaging and functional.

## Where Does JavaScript Run?

JavaScript runs mainly in two places:
- **Client-side (Browser):** Executes in web browsers—this is its most common use, allowing websites to respond instantly to user actions without needing to reload the page.
- **Server-side (Node.js):** Runs on servers using platforms like Node.js, enabling backend web development, database operations, and building APIs.

## Basic Web Development Analogy

Think of web development as building a digital house:
- **HTML** is the structure and framework—the walls, windows, and doors that hold everything together.
- **CSS** is the design and paint—the styles and colors that make it look attractive.
- **JavaScript** is the electricity and appliances—it brings the house to life with lights, movement, and interaction, letting users "live" in the house and shape their experience.
JavaScript is the essential technology that turns static web pages into interactive, modern web applications.




***
***

## JavaScript Basics

Here is a detailed overview of variables, datatypes, and operators in JavaScript with explanations and examples:

***

### Variables

Variables in JavaScript are containers for storing data values. They can be declared using three keywords: `var`, `let`, and `const`.[2][5]

- **var**: Function-scoped and can be redeclared or reassigned.
    ```js
    var a = 10;
    a = 20; // allowed
    var a = 30; // allowed
    ```
- **let**: Block-scoped and can be reassigned but not redeclared within the same scope.
    ```js
    let b = 15;
    b = 25; // allowed
    // let b = 35; // not allowed in same scope
    ```
- **const**: Block-scoped and cannot be reassigned after its initial assignment.
    ```js
    const PI = 3.14;
    // PI = 3.1415; // Error: reassignment not allowed
    ```

Variables can be declared without an initial value (default value is `undefined`):
```js
let name;
console.log(name); // undefined
```
Multiple variables can be declared in one line:
```js
let x = 5, y = 10, z = 15;
```

***

## Data Types

JavaScript is dynamically typed, meaning variables do not need a declared type; the type depends on the value assigned.[1][7]

Main data types:
- **String**: Sequence of characters.  
  Example: `let message = "Hello";`
  
- **Number**: Numeric value, integers or floating-point.
  Example: `let age = 25;`
- **Boolean**: True or false values.
  Example: `let isValid = true;`
- **Undefined**: Variable declared but not assigned a value.
  Example: `let value; // value is undefined`
- **Null**: Intentional absence of value.
  Example: `let empty = null;`
- **Object**: Collection of properties and methods.
  Example: `let person = { name: "Alex", age: 22 };`
- **Array**: Ordered list of values (a type of object).
  Example: `let numbers = [1, 2, 3];`
- **Symbol**: Unique, immutable value.
  Example: `let id = Symbol("id");`
- **BigInt**: For very large integers.
  Example: `let bigNum = 123456789012345678901234567890n;`

Use the `typeof` operator to check a variable’s type:
```js
console.log(typeof age); // "number"
console.log(typeof message); // "string"
console.log(typeof person); // "object"
```

***

## Operators

Operators perform operations on values and variables:[7][1]
- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `%` (modulus), `++`, `--`
  ```js
  let sum = 10 + 5; // 15
  let diff = 10 - 5; // 5
  let prod = 10 * 5; // 50
  let quotient = 10 / 5; // 2
  let remainder = 10 % 3; // 1
  ```
- **Assignment Operators:** `=`, `+=`, `-=`, `*=`, `/=`
  ```js
  let x = 10;
  x += 5; // x = 15
  ```
- **Comparison Operators:** `==`, `===`, `!=`, `!==`, `>`, `<`, `>=`, `<=`
  ```js
  let a = 5, b = "5";
  console.log(a == b); // true (loose equality)
  console.log(a === b); // false (strict equality)
  ```
- **Logical Operators:** `&&` (and), `||` (or), `!` (not)
  ```js
  let isAdult = age > 18 && age < 65; // true if age is between 19 and 64
  ```
- **String Operators:** `+` (concatenation)
  ```js
  let greet = "Hello, " + name;
  ```

***


| Concept        | Explanation                                                                            | Example                                     |
|----------------|----------------------------------------------------------------------------------------|---------------------------------------------|
| **Variables**  | Storage containers for data; declared with `var`, `let`, or `const`.                   | `let age = 25;`                             |
| **Data Types** | Main types: number, string, boolean, null, undefined, object, array.                   | `let name = "ApexAIQ";`                     |
| **Operators**  | Arithmetic (`+`, `-`, `*`, `/`), comparison (`==`, `===`, `<`, `>`), logical (`&&`, `||`). | `let sum = 2 + 3;`                          |
| **Functions**  | Reusable blocks of code that perform specific tasks.                                   | `function greet() { console.log("Hi!"); }`  |
| **Objects**    | Group related data and functions into a single entity.                                 | `let user = {name: "Alex", age: 25};`       |
| **Arrays**     | Store multiple values in a single variable.                                            | `let colors = ["red", "blue", "green"];`    |

***

## Control Flow in JavaScript

Control flow statements determine how code executes:

| Statement              | Explanation                                                         | Example                                 |
|------------------------|---------------------------------------------------------------------|-----------------------------------------|
| **if / else**          | Conditional execution based on a boolean expression.                | `if (age > 18) { console.log("Adult"); } else { console.log("Minor"); }` |
| **switch**             | Selects code to run based on multiple possible values.              | `switch(day) { case 1: console.log("Mon"); break; }` |
| **for loop**           | Runs code a certain number of times.                                | `for(let i=0; i<3; i++) { console.log(i); }` |
| **while loop**         | Repeats code while condition is true.                               | `while(x < 5) { console.log(x); x++; }` |
| **do...while loop**    | Runs code at least once then continues while condition is true.     | `do { x++; } while(x < 5);`             |
| **break**              | Exits from a loop or switch statement early.                        | `for(...) { if(x===3) break; }`         |
| **continue**           | Skips current loop iteration and moves to the next.                 | `for(...) { if(x===3) continue; }`      |

***

### Example: Combining Basics & Control Flow

```javascript
let colors = ["red", "green", "blue"];
for(let i = 0; i < colors.length; i++) {
  if(colors[i] === "green") {
    console.log("Found green!");
  }
}
```

This example loops through an array and prints a message when it finds "green".

***
