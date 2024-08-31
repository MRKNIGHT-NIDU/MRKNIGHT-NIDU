import requests
from bs4 import BeautifulSoup
import argparse
import re

def print_banner():
    banner = """
███╗   ███╗██████╗ ██╗  ██╗███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗   ███╗   ██╗██╗██████╗ ██╗   ██╗
████╗ ████║██╔══██╗██║ ██╔╝████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝   ████╗  ██║██║██╔══██╗██║   ██║
██╔████╔██║██████╔╝█████╔╝ ██╔██╗ ██║██║██║  ███╗███████║   ██║█████╗██╔██╗ ██║██║██║  ██║██║   ██║
██║╚██╔╝██║██╔══██╗██╔═██╗ ██║╚██╗██║██║██║   ██║██╔══██║   ██║╚════╝██║╚██╗██║██║██║  ██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║  ██╗██║ ╚████║██║╚██████╔╝██║  ██║   ██║      ██║ ╚████║██║██████╔╝╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ 
                                                                                                   
                                                                                                   
    """
    print(banner)

def extract_links(url, keywords):
    links = set()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            for keyword in keywords:
                if keyword in href:
                    links.add(href)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return links

def save_to_file(links, output_file):
    with open(output_file, 'w') as file:
        for link in links:
            file.write(f"{link}\n")

def print_link_status(link, status_code):
    if status_code == 200:
        return f"\033[92m{link} - Status: {status_code}\033[0m"  # Green for 200
    elif status_code in [404, 403, 500]:
        return f"\033[91m{link} - Status: {status_code}\033[0m"  # Red for 404, 403, 500
    else:
        return f"{link} - Status: {status_code}"

def clean_url(url):
    """Remove any extraneous characters from URL."""
    return re.sub(r'^[\d]+:\s*', '', url).strip()

def check_urls_from_file(input_file, output_file):
    results = []
    with open(input_file, 'r') as file:
        urls = file.readlines()
    
    print(f"Checking URLs from {input_file}...")
    for url in urls:
        url = clean_url(url)
        if url:
            try:
                response = requests.head(url, allow_redirects=True)
                result = print_link_status(url, response.status_code)
                results.append(result)
            except requests.RequestException as e:
                results.append(f"\033[91m{url} - Error: {e}\033[0m")  # Red for errors
    
    if output_file:
        print(f"Saving results to {output_file}...")
        with open(output_file, 'w') as file:
            for result in results:
                file.write(f"{result}\n")
        print(f"Results saved to {output_file}")

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description='Extract, check URLs with specific parameters from a domain, or check URLs from a file.')
    parser.add_argument('-d', '--domain', type=str, help='The domain name to extract URLs from.')
    parser.add_argument('-o', '--output', type=str, help='The output file to save the results.')
    parser.add_argument('-f', '--file', type=str, help='The input file containing URLs to check.')
    args = parser.parse_args()

    if args.domain:
        keywords = ['page=', 'php?id=']
        print(f"Extracting links from {args.domain} with keywords {keywords}...")
        links = extract_links(args.domain, keywords)
        
        if args.output:
            print(f"Saving results to {args.output}...")
            save_to_file(links, args.output)
            print(f"Links saved to {args.output}")
        
        print(f"Found {len(links)} links. Checking statuses...")
        for link in links:
            try:
                response = requests.head(link, allow_redirects=True)
                print(print_link_status(link, response.status_code))
            except requests.RequestException as e:
                print(f"\033[91m{link} - Error: {e}\033[0m")  # Red for errors

    elif args.file:
        check_urls_from_file(args.file, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
