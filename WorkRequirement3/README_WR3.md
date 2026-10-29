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
The result in the terminal should display: `Hello from:"Your hostname"! The IP address is "hostname address"`.<br>

# Work Requirement 3 Reflection
The script in Work Requirement 3 is kept short and simple. The script allows the user to enter a hostname as input. The script is also organized into a function to keep the code readable.

#### key takeaways from Module 5 (TCP/IP, the socket API, browsers, HTTP, web servers)
For me, the key takeaway from Module 5 was gaining a better understanding of server side web development as a whole. I think that the module explained HTTP, TCP/IP, Web Server, Socket, and browsers in a way that helped me understand their roles, how they communicate, and how everything works together. For example, I learned how the socket API could resolve a hostname to an IP address with Python. I think this can be useful when testing network connection, or other network related issues. I also appreciated the  explanation of the HTTP request/response cycle, how HTTP uses URLs to locate resources, and how clients use  HTTP methods to communicate with  servers. These topics were not covered in depth in my prior education and courses. Therefore, I appreciate this new knowledge which will be valuable for my future career, no matter the path I choose within information technology.

#### A challenge or surprise in Module 5
In Module 5, I did not find the topics particularly challenging. However, I was surprised by the section Generating HTML Programmatically or with Templates. I was not familiar with these approaches to generating HTML with Python. The Jinja2 templating language for Python had a very user friendly syntax and the structure was easy to follow. 

#### One topic from the module I want to explore
The one topic from Module 5 that I want to explore further is HTTP. I did find many of the sections in this topic interesting, but I was most curious about the header metadata and statelessness in HTTP. I do want to explore more about authorization, authentication, and cookies in HTTP headers as I have minimal experience with these concepts. I found statelessness interesting as each HTTP request from the client is independent, and the server does not remember the previous interaction. I think these sections would further enhance my skills and understanding.