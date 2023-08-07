# Vulnerable API Python Application

This project is an intentionally vulnerable API-based Python application that uses Flask, Jinja, and SQLite3. It has been deliberately designed with multiple vulnerabilities, including XSS (Cross-Site Scripting), SQLi (SQL Injection), HHI (HTTP Header Injection), LFI (Local File Inclusion), RFI (Remote File Inclusion), and SSTI (Server-Side Template Injection). The purpose of this project is to provide a playground for educational purposes and to test and understand automated API scanners and security testing tools.

**Disclaimer**: This project should only be used in a controlled environment and for educational purposes. Do not deploy it in a production environment or expose it to the public as it can be used to exploit and damage systems if not handled responsibly.

## Setup Instructions

```bash
git clone https://github.com/yourusername/vulnerable-api.git
cd vulnerable-api
```

### Install the required Python packages:

```bash
pip install -r req.txt
```

### Run the application:

```bash   
python app.py

Access the application in your web browser by navigating to http://localhost:8000.
```

## Vulnerabilities

The application contains the following vulnerabilities:

1. Cross-Site Scripting (XSS)

The application is susceptible to Cross-Site Scripting attacks. These vulnerabilities occur when unvalidated user inputs are rendered directly in the HTML page, allowing malicious scripts to be executed in the context of the website.

2. SQL Injection (SQLi)

The application is vulnerable to SQL Injection attacks. SQLi occurs when user-supplied data is not properly sanitized or validated, allowing an attacker to execute arbitrary SQL commands on the database.

3. HOST Header Injection (HHI)

The application is vulnerable to HOST Header Injection attacks. This vulnerability allows an attacker to inject malicious HOST headers, potentially leading to various security issues like cache poisoning or cross-site scripting.

4. Local File Inclusion (LFI)

The application is susceptible to Local File Inclusion attacks. This vulnerability allows an attacker to include and execute local files on the server, potentially exposing sensitive information or executing arbitrary code.

5. Remote File Inclusion (RFI)

The application is vulnerable to Remote File Inclusion attacks. RFI occurs when user-supplied input is used to include remote files from external servers, leading to potential code execution and unauthorized access.

6. Server-Side Template Injection (SSTI)

The application is prone to Server-Side Template Injection attacks. SSTI occurs when user input is used directly in server-side templates, potentially leading to code execution on the server.

## Contributing

If you would like to contribute to this project by adding more vulnerabilities, improving existing ones, or enhancing the overall codebase, you are welcome to submit a pull request. Please follow the guidelines and ensure that the vulnerabilities added are safe and for educational purposes only.

## Disclaimer

This project is for educational purposes only. Do not use it for any malicious intent. The authors and contributors of this project are not responsible for any misuse or damage caused by this software.

Use this project responsibly and only in controlled environments. Do not deploy it in a production environment or expose it to the public. Stay ethical and abide by the law.
License

This project is licensed under the MIT License.

This README provides an overview of the vulnerable API Python application. Remember that the primary goal of this project is educational, and users should exercise caution when running and testing it. Make sure to use this responsibly and only in environments you have permission to test and evaluate. Happy learning and happy testing!