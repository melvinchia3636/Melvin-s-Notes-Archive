# Express JS Complete Guide

## What is an API?

Simply put, API stands for **Application Programming Interface**, is a kind of medium that allows the interaction between client and server side for transfering data back and forth, updating/deleting/adding data in the database, etc.

![What is an API and How Does It Work?](https://www.cleveroad.com/images/article-previews/40ca78a7a9db7adfb6bb861fc6b8910ae2ef4bb79f5508007d166f01df5c1038.png)

## What is ExpressJS

Express JS is basically a framework that allows you to create your very own **REST API** in Javascript (NodeJS).

> **What in the world is REST API?**
>
> **REST (Representational State Transfer) API** stands for is a kind of API that has multiple endpoints/routes and each of them serves different purpose.

## Setting up an ExpressJS project

### Prerequiries

- A computer
- A functional brain ;-;
- Decent JavaScript and NodeJS fundamental
- NodeJS
- A node package manager like NPM or Yarn
- A code editor (preferably VSCode)
- A browser (Firefox is strongly recommended cuz it lets you see JSON data in a better way)

### Installing ExpressJS

First, create a new folder that will serve the purpose of containing all the source code of your project. Then, open the project folder in your code editor.

![image-20221002201358616](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221002201358616.png)

Then, open your terminal.

> In VSCode, you can quickly pull up your terminal by using the `Ctrl + ` `  hotkey.

![image-20221002201534841](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221002201534841.png)

Type in `npm init -y` or `yarn init -y` to initialize a node project. A `package.json` file will automatically be generated in your project folder.

![image-20221002201655653](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221002201655653.png)

Create a file in your project called `index.js`. This will be the file where we write all the code of our API.

![image-20221002201800682](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221002201800682.png)

Next, we'll install our dependency, which in this case, is called `express`. To add a dependency to our Node project, we type `npm install <package_name>` or `yarn add <package_name>`. So in order to add `express` to our project, we just replace the `<package_name>` with `express`.

![image-20221002202246241](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221002202246241.png)

After this command has successfully been executed, you'll notice a new folder called `node_modules` is created. This folder contains all the code of our installed dependencies and the dependencies of these dependencies.

![image-20221002202333412](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221002202333412.png)

Theoredically speaking, we've now successfully initialized a brand new ExpressJS project. You can now start writing some code. But before that, we're going to install some utility tools which will make our job a lot easier.

Unlike frontend frameworks like React which typically shipped with a **hot reloader** that will automatically update the browser whenever our code changes, vanilla ExpressJS project doesn't do that. Thus, we'll install a package called `nodemon` as our dev dependency. This package allows the server to restart whenever we make changes to our source code.

Type in `npm install nodemon --save-dev` or `yarn add nodemon --dev` in your terminal.

![image-20221002202957915](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221002202957915.png)

Now we've successfully intialized the project, and we're ready to start writing some code.

## Get the API up and running

Head to your `index.js`, and the first thing to do is importing the `express` module.

```js
const express = require("express");
```

You'll notice that we're not using the normal `import` method that we usually use in our React project. The reason is that our React project is a `module ` but our `index.js` is just a `commonjs`, so we must use the `require` method to import modules to our project.

Next, we need to initalize our express server instance and store it inside a variable which will be used later to bind all of our routes, middleware, etc.

```js
const app = express();
```

Before firing up the API server in our local machine, we must bind the Express app to a port so that it can start listening for requests. We can achieve this by calling the `listen` method on the `app` variable which contains our ExpressJS server instance.

```js
app.listen(3000, () => {
  console.log("Server is listening on port 3000")
})
```

The first argument is the port that we'll be using to access our API, which in this case is `3000`, but you can use other port as well, just make sure that it is not used by other services, or an error will be thrown when you start the server.

The second argument is an arrow function. This function will be called after the app instance is successfully being bound to the port that we specified in the first argument being passed into the `listen` method. In our case, a message will be output to the console telling us that the server is now listening for requests on port 3000.

Now, it's finally time to head to our terminal and fire up our API server. To start our server during development (you're changing the source code constantly), we can use the Nodemon package which was installed just now. In your terminal, type in `npx nodemon index.js` or `yarn nodemon index.js` to start the development server.

![image-20221003162159379](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221003162159379.png)

> **Small tips for lazy people**
>
> If you're lazy typing `yarn nodemon index.js` everytime you start your server, consider making an alias in your `package.json`. To do that, head to your `package.json` and add the following code in your `script` object:
>
> ```json
> {
>   ...
>   "scripts": {
>     ...
>     "dev": "nodemon index.js",
>     "start": "node index.js"
>     ...
>   },
>   ...
> }
> ```
>
> Now, whenever you wanna start a development server, you can simply type `npm dev` or `yarn dev` and the required command for starting the server will automatically be executed.

It's time to try out our API for the first time. Open your preferred browser, type in `http://localhost:3000` in the url input box and hit enter. If everything was set up correctly, you should see something like this:

![image-20221003163152356](/Users/melvinchia/Library/Application Support/typora-user-images/image-20221003163152356.png)

Why is it showing `Cannot GET /`? We'll talk about it in the next chapter.

## Hello world in ExpressJS

Every programmer knows that regardless what language or framework you're learning, the first thing to do must be getting the `Hello world` string output to your screen. So, how can we do this in ExpressJS?

An important concept of REST API to be kept in mind is that a REST API consists of multiple endpoints (aka routes) which can be used to access different resources or perform different operations. Below are the code for setting up our first route in our API.

```js
app.get("/", (req, res) => {
  res.send("Hello world!");
})
```

This means, when user access our API through the base URL (`/`) using `GET` method,  we want the server to return a `Hello world!` string back to the user. Now, when you access `http://localhost:3000` in your browser, you'll see `Hello world!` being shown on your screen.

<img src="/Users/melvinchia/Library/Application Support/typora-user-images/image-20221003164704059.png" alt="image-20221003164704059" style="zoom:50%;" />

### HTTP Request Methods

We've mentioned `GET` method just now, but what is that?

`GET` is one of the HTTP request methods, which is a set of **request methods** to indicate the desired action to be performed for a given resource. Below are a list of all the valid HTTP request methods.

| Method    | Descriptions                                                 |
| --------- | ------------------------------------------------------------ |
| `GET`     | Requests a representation of the specified resource. Requests using `GET` should only retrieve data. |
| `HEAD`    | Asks for a response identical to a `GET` request, but without the response body. |
| `POST`    | Submits an entity to the specified resource, often causing a change in state or side effects on the server. |
| `PUT`     | Create new resource replaces current representations of the target resource in the serevr with the request payload. |
| `DELETE`  | Deletes the specified resource.                              |
| `CONNECT` | Establishes a tunnel to the server identified by the target resource. |
| `OPTIONS` | Describes the communication options for the target resource. |
| `TRACE`   | Performs a message loop-back test along the path to the target resource. |
| `PATCH`   | Applies partial modifications to a resource.                 |

For more detailed explanation, you may refer to https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods.

Note that despite having these much request methods, we will only use some of them, like for example `GET` and `POST` are two of the most used method in REST APIs.



## Different kind of resources

### Raw Text or HTML

You can send raw text or HTML represented in strings back to client using `res.send` method.

```js
res.send("<h1>MRGA YYDS</h1>")
```

### JSON

Most of the case when users are requesting data from your server, those data are being represented in JSON format. There are two ways of sending JSON data back to users.

#### `res.send([body])`

`res.send` is a general method for sending any kind of data, the `[body]` parameter can be a `String`, an object, `Boolean`, or an `Array`.

When the parameter is a `String`, the method sets the `Content-Type` to “text/html”:

```javascript
res.send('<p>MRGA YYDS</p>')
```

When the parameter is an `Array` or `Object`, Express responds with the JSON representation:

```javascript
res.send({ name: 'MRGA' })
res.send([1, 2, 3])
```

#### `res.json([body])`

`res.json` is quite self-explanatory, it can only be used to send JSON response.

```js
res.json({
  "name": "MRGA",
  "members": 10,
  "is_active": true
});
```

### Files

If your data is being stored in a file, or if you want to send multimedia documents like images or videos, you can send the file back to the client using the `sendFile` method, passing the absolute path of the file you want to send into the method.

```js
const path = require("path");

app.get("/data", (req, res) => {
  const targetFile = path.join(__dirname, "image.png");
  res.sendFile(targetFile)
})
```

## Routing in ExpressJS

Routing refers to defining where and how your client should access your resources through the API. Simply put, you define the path and behaviour or each and every endpoints of your API.

Generally, you define your route with the following structure:

```js
app.METHOD(PATH, HANDLER)
```

- `app`: the server instance
- `METHOD`: a HTTP request method, in lowercase
- `PATH`: a path with is used by client to request for specific resource
- `HANDLER`: a function that will be called when client request the path

For example:

```js
app.get("/data", (req, res) => {
  res.send("Put some data here")
})
```

This defines that client should be able to request a string `"Put some data here"` through the url `http://DOMAIN:PORT/data` using HTTP GET request.

Keep in mind that if you request the same route with any HTTP request method that you didn't define in your code, the request will result in 404 NOT FOUND.

If you want to allow a specific route to accept all HTTP request methods, you can write your route like this:

```js
app.all("/data", (req, res) => {
  res.send("Put some data here")
})
```

### Route paths

There are multiple ways to define route paths, the part in your URL after your domain and port. You can write your path in strings, string patterns, or regular expression. Whenever the client request path matches the string or string patterns, the corresponding handler function will be called.

#### Request to root route

Root route, defined to `/ ` on default.

```js
app.get('/', (req, res) => {
  res.send("MRGA YYDS")
})
```

URL that matches:

- `http://localhost:3000`
- `http://localhost:3000/`

#### Request to absolute route

Absolute routes with no special characters, only alphanumeric chars (A-Z, a-z, 0-9, -, _, etc.), the handler will only be called when the client matched exactly as how you defined it.

```js
app.get("/abcdef", (req, res) => {
  res.send("MRGA YYDS")
})
```

URL that matches:

- `http://localhost:3000/abcdef`

