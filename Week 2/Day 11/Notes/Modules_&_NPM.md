
---

#   Modules

### What is a Module?

* A **module** in Node.js is a **reusable block of code** (functions, objects, classes) that you can export and import in different files.
* It helps organize large applications into smaller, maintainable parts.
* Similar to libraries in other languages (like Java or Python).

---

##  Types of Modules

1. **Core Modules (Built-in)**

   * Provided by Node.js itself.
   * Example:

     * `fs` → File system operations (read/write).
     * `http` → Create server, handle requests.
     * `os` → Info about operating system.
     * `url` → URL parsing and formatting.
     * `path` → File path manipulations.

   Example:

   ```js
   const fs = require('fs');
   fs.writeFileSync('test.txt', 'Hello Node.js!');
   ```

2. **Local Modules (Custom)**

   * Created by developers for their own project.
   * Example:

     ```js
     // math.js
     function add(a, b) {
       return a + b;
     }
     module.exports = add;

     // app.js
     const add = require('./math');
     console.log(add(5, 10)); // 15
     ```

3. **Third-Party Modules**

   * Installed via **npm**.
   * Example: `express`, `mongoose`, `axios`.

   ```js
   const express = require('express');
   const app = express();
   app.get('/', (req, res) => res.send('Hello World!'));
   app.listen(3000);
   ```

---

# NPM (Node Package Manager)

### What is NPM?

* **Default package manager** for Node.js.
* It comes bundled with Node.js installation.
* Provides a huge **online registry** with over 2 million packages (libraries, frameworks, utilities).
* Used to **install, update, and manage dependencies** in your project.

---

## How NPM Works

1. **Initialize a Project**

   ```bash
   npm init -y
   ```

   * Creates `package.json` (keeps record of dependencies).

2. **Install Packages**

   ```bash
   npm install express
   ```

   * Adds `express` to `node_modules/` and updates `package.json`.

3. **Install Development Dependencies**

   ```bash
   npm install nodemon --save-dev
   ```

   * Used only for development (not production).

4. **Global Installation**

   ```bash
   npm install -g nodemon
   ```

   * Makes package available system-wide.

---

### Important Files in NPM

* **package.json** → Stores project metadata & dependencies.
* **node\_modules/** → Contains installed packages.
* **package-lock.json** → Locks exact versions of installed dependencies.

---

### Popular NPM Packages

* **Express** → Build APIs & web apps.
* **Mongoose** → MongoDB object modeling.
* **Nodemon** → Automatically restarts app when files change.
* **Dotenv** → Load environment variables from `.env` files.
* **Axios** → HTTP client for making API calls.

---

## Difference Between Module & NPM

* **Module** → A unit of reusable code (can be built-in, custom, or third-party).
* **NPM** → A tool/package manager used to install and manage those modules.

Example: `express` is a **third-party module**. You install it using **npm**.

---
