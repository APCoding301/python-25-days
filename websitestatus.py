import requests
from requests import Response

def normalize_url(url: str) -> str:
    """Ensure the URL starts with http:// or https://"""
    return url if url.startswith(('http://', 'https://')) else f'https://{url}'


def print_website_status(*values: any, sep: str | None = " ", end: str | None = "\n") -> None:
    """Custom print function to print values with custom separators and end characters"""
    print(f'=== Website diagnostics for {values[0]} ===')
    print(*values, sep=sep, end=end)


def check_website(url: str, timeout: int = 10) -> list[any]:
    """Check the status of a website and return the data"""
    url = normalize_url(url)

    #print(f'=== Website diagnostics for {url} ===')

    try:
        response: Response = requests.get(url, timeout=timeout)
    except Exception as e:
        print(f"ERROR: {e}")
        return
    
    list_stat_codes: list[Any] = []

    list_stat_codes.append(f"URL            : {url}")
    # FIRST item in the list is always the URL, i.e. the website being checked.
    status_code: int = response.status_code
    elapsed_time: float = response.elapsed.total_seconds()
    reason: str = response.reason
    content_type: str = response.headers.get('Content-Type', 'unknown')
    encoding: str | None = response.encoding
    headers: dict[str, str] = dict(response.headers)


    # print(f"Status Code    : {status_code} ({reason})")
    # print(f"Elapsed Time   : {elapsed_time:.2f}s")
    # print(f"Content Type   : {content_type}")
    # print(f"Encoding       : {encoding or 'n/a'}")
    # print("Headers         :")
    # for key, value in headers.items():
    #     print(f"    - {key}: {value}")

    list_stat_codes.append(f"Status Code    : {status_code} ({reason})")
    list_stat_codes.append(f"Elapsed Time   : {elapsed_time:.2f}s")
    list_stat_codes.append(f"Content Type   : {content_type}")
    list_stat_codes.append(f"Encoding       : {encoding or 'n/a'}")
    list_stat_codes.append(f"Headers        : ")
    for key, value in headers.items():
        list_stat_codes.append(f"    - {key}: {value}")
        
    return list_stat_codes


website_values: list[any] = []
website_values = check_website("www.jabberwocky.com")
print_website_status(*website_values, sep='\n')
#website_values = check_website("www.cnn.com")
#print_website_status(*website_values, sep='\n')

