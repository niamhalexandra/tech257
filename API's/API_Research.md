## API's

### what are API's?
* API stands for "Application Programming Interface"
* It's a set of rules and tools that allow different software programmes to talk to each other and share info.
* They serve as an interface between different software applications, defining methods and endpoints that applications can use to interact with each other
* They enable applications to communicate with each other
* Define data formats used for communication between applications (most commonly JSON)
* Used for authentication so only authorised users or apps can access certain resources or perform actions. 

### How are they used?
* API's are used by developers to add features and data to their apps without building everything from scratch
* Often used when building an app that may need users to log in, they could, for instance, then do that via their google or facebook log in's to handle authentication.

### Why are they so popular?
* They enable seamless communication and data exchange between different software components, making it easier to build complex applications.

![Your paragraph text.png](..%2F..%2F..%2F..%2F..%2FDownloads%2FYour%20paragraph%20text.png)

## What is REST API?

_"Representational State Transfer Application"*_
* A specific type of API that is 'RESTful'.

## What makes an API RESTful
* REST is an architectural style for designing networked apps, particularly web services, they use HTTP methods (detailed below) to perform operations on resources which are typically represented as URLS's (Uniform Resource Locators)

## What are the REST Guidelines?
1. Each Request is Complete: When you talk to a server, you tell it everything it needs to know in one go. You don't have to remind it about past conversations. 
2. Use Standard Tools: Everyone follows the same rules when talking to each other. We all know how to ask for things (GET), add new stuff (POST), change things (PUT), or get rid of them (DELETE). 
3. Everything has a Name: Imagine everything is like a toy in a big box. Each toy has its own name (like a URL), so you can ask for the one you want. 
4. Different Ways to Look at Things: You can ask for information in different ways, like asking for a story in English or Spanish. You pick the one you like. 
5. Servers Don't Remember: Once the server gives you what you want, it forgets about you. It doesn't keep track of your requests. 
6. Remembering Old Answers: Sometimes, it's okay to keep an old answer around so you don't have to ask again. But you have to follow the rules about when you can do that. 
7. Adding More Layers: You can put things in between you and the server, like a mailbox or a friend. They help make things faster or keep them organized. 
8. We're All Connected: There's you (the client) and the server (the one with the information). We keep things separate so we can make changes or grow without messing up each other's stuff.

## What is HTTP?
_"Hypertext Transfer Protocol"_
* It's like a language that computers use to talk to each other over the internet

### What is it used for?
* A set of rules that define how information is sent and received between web servers and web browsers. 
* Like the way your browser asks for web pages and the server sends them back. It's the foundation of how we access and interact with websites on the internet.

### What is HTTPS?
_"Hypertext Transfer Protocol Secure"_
* A safer version of HTTP, it encrypts the data being sent between browser and server making it harder to be tampered with, protects your privacy and ensures secure online interactions

### Explaination of HTTP Request Structure in diagram:



### Explaination of HTTP Response Structure in a diagram:

### What are 5 HTTP verbs and what do they do?

* GET: Asking for something. It's like saying "Give me this web page or piece of information."
* POST: Adding something new. It's like submitting a form or adding a new entry to a list. 
* PUT: Updating something. It's like saying "Replace this with that" or "Update this information."
* PATCH: Partially updating something. It's like making small changes to existing data without replacing it entirely. 
* DELETE: Removing something. It's like saying "Get rid of this" or "Delete this entry from the list."

## What is Statelessness?
* Each request to a server is independent and doesn't rely on any previous requests. In other words, the server doesn't remember any information about previous interactions/requests.

### Stateless Request (GET) vs Stateful Request (POST)

1. Stateless Request (GET): Imagine you visit a website to read an article. You send a GET request to the server asking for the article. The server sends back the article, but it doesn't remember who you are or what article you read before.
You visit the same website again and request another article. The server treats this as a completely new request and sends back the requested article without any knowledge of your previous visit.
2. Stateful Request (POST): Now, let's say you're submitting a form on a website (e.g., signing up for an account). You fill out the form and click "Submit." The data you entered (e.g., username, password) is sent to the server in a POST request.
The server receives the POST request, processes the form data, and creates a new user account in its database. It remembers this information for future requests, such as when you log in again later.

## What is caching?
* Caching is like storing a copy of something you use often so you can access it faster later. storing copies of web pages, images, or other data on your device or a server closer to you, so they load quickly the next time you visit a website or use an app. It helps speed up your internet experience by reducing the time it takes to fetch data from the original source. 


