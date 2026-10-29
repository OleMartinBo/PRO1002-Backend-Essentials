# Work Requirement 3 Intro to Networking: Simple Socket Task & Short Reflection
For this task, you'll get a small taste of how TCP/IP and the client-server model work in practice. You'll create a tiny Python script using the socket module and write a short reflection on key ideas from Module 5.<br>

Submission deadline: 30.10.2026

## Objectives
1. Use the Python socket API in a minimal practical example.
2. Reflect on what you learned about networking fundamentals.

## Project Overview
* Write a small Python script that resolves a hostname.
* Write a short reflection (~100 words) summarizing your main takeaways.
* Create a small Python script that performs the following:
  * use the socket module to resolve a hostname into an IP address'
  * print a short greeting together with the resolved IP<br>
<br>

## How to run and use main.py
1. Locate the folder WorkRequirement3. 
2. Open the file `main.py`.
3. Click Run Python File in the right top corner (VS Code).<br>
<br>
ALT: Use the commands below in the terminal:

```
CD WorkRequirement3
```
```
python main.py
```
In the terminal you will be asked to enter a hostname, `Enter a hostname: `.<br>
Enter your preferred hostname, for example: `vg.no`.<br>
The result in the terminal should display: `Hello from:"Your hostname"! The IP address is "host address"`.<br>

# Work Requirement 3 Reflection
The script in  Work Requirement 3 is kept short and simple. The script allows a user to choose an external domain through the user input. The script is wrapped inside a function to keep the code organized and readable.

#### key takeaways from Module 5 (TCP/IP, the socket API, browsers, HTTP, web servers)
For me, the key takeaway from Module 5 was gaining a better understanding of server side web development as a whole. I think that the module explained HTTP, TCP/IP, Web Server, Socket, and browsers in a manner that helped me understand their roles, how they communication, and how everything works together. For example, I learned how the socket API could resolve a hostname to an IP address with python. I think this can be useful when testing commutation, connection, or other network related factors. I also appreciated the  explanation of HTTPs request/response cycle, how HTTP uses URLs to locate resources, and the HTTP methods clients use to communicate with  servers. These details and information were not covered in depth in my prior education and courses. Therefore, I appreciate the new knowledge which is valuable for my future career, no matter the path i choose within information technology.

#### A challenge or surprise in Module 5
For module 5, i did not find the topics particularly challenging. However, I was more so surprised by the section Generating HTML Programmatically and with Templates. I was not familiar with these options for generating HTML with python. The Jinja2 templating language for Python had a very user friendly syntax and the structure was easy to follow. 

#### One topic from the module I want to explore
The one topic form  Module 5 I further want to explore is HTTP. I did find many of the sections in this topic interesting, but were most curios about the header Metadata and Statelessness in HTTP. I do want to explore more about authorization, authentication, and cookies in header as i have minimal experience with these concepts. Statelessness I found interesting as each request form the client is independent where the server doest remember the interaction from before. I think these sections would further enhance my skills and understanding.