MRKNIGHT-NIDU

Overview
MRKNIGHT-NIDU is a Python-based tool designed to extract and check the status of URLs from specified domains. This tool is essential for web administrators, security professionals, and anyone needing to monitor the health of web assets and ensure the accessibility of links.


Key Features
URL Extraction: Extracts URLs from a given domain based on specified keywords.
Status Checking: Verifies the HTTP status of each extracted URL to identify issues like broken links or server errors.
Customizable Keywords: Allows modification of keywords for more targeted URL extraction.
Result Export: Saves results to a file for easy analysis and record-keeping.
Installation
To use this tool, ensure you have Python installed on your system. The script requires the requests and beautifulsoup4 libraries, which can be installed via pip.

bash
Copy code
pip install requests beautifulsoup4
Usage
Run the script from the command line with the following options:

bash
Copy code
python script.py [-d DOMAIN] [-o OUTPUT] [-f FILE]
-d DOMAIN : The domain name to extract URLs from and check.
-o OUTPUT : The file to save the results of the URL status checks.
-f FILE : The file containing URLs to check.
Examples
Extract and check URLs from a domain:

bash
Copy code
python script.py -d https://example.com -o results.txt
This command extracts URLs from https://example.com, checks their statuses, and saves the results to results.txt.

Check URLs from a file:

bash
Copy code
python script.py -f urls.txt -o status_results.txt
This command reads URLs from urls.txt, checks their statuses, and saves the results to status_results.txt.

Customization
You can customize the keywords used for URL extraction by modifying the script. The default keywords are page= and php?id=.

License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

Contact
For questions or support,create an issue on the GitHub repository.

