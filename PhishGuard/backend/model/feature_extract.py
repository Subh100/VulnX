import re 
from urllib.parse import urlparse

def extract_features(url):

    features = []

    #1. Having IP Address
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(-1 if re.search(ip_pattern, url) else 1)

    #2. URL Length 
    features.append(1 if len(url) < 54 else -1)

    #3.SHoterning Service
    shortening = [
        "bit.ly",
        "tinyurl.com",
        "goo.gl",
        "t.co"
    ]

    features.append(
        -1 if any (service in url for service in shortening)
        else 1
    )

    #4. @S Symlbol
    features.append(-1 if "@" in url else 1)

    #5. Preffix-Suffix
    domain = urlparse(url).netloc
    features.append(-1 if "-" in domain else 1)

    #6. Double Slash Redirecting
    features.append(-1 if url.rfind("//")> 7 else 1)

    #7. Having SUb Domain
    domain = urlparse(url).netloc
    dots = domain.count(".")

    if dots == 1:
        features.append(1)
    elif dots == 2:
        features.append(0)
    else:
        features.append(-1)

    #8. HTTPS Token in Domain
    features.append(
        -1 if "https" in domain.replace("www.", "")
        else 1
    )

    #10. Special Character Count
    special_chars = len(re.findall(r'(\d{1,3}\.){3}\d{1,3}', url))
    features.append(
        1 if special_chars < 10
        else -1
    )

    #11. Slash Count
    features.append(
        1 if url.count("/") < 6
        else -1
    )

    #12. Equal (=) Count
    features.append(
        1 if url.count("=") < 2
        else -1
    )

    #13. Question Mark Count
    features.append(
        1 if url.count("?") < 1
        else -1
    )

    #14. Suspsicious Keywords
    suspicious_words = [
        "login",
        "verify",
        "account",
        "banking",
        "secure",
        "update",
        "signin",
        "confirm"
    ]

    features.append(
        -1 if any(word in url.lower() for word in suspicious_words)
        else 1
    )

    #15. Domain Length
    features.append(
        1 if len(domain) < 30
        else -1
    )
    
    #16. Dot Count 
    features.append(
        1 if url.count(".") < 4
        else -1
    )

    #17. Hyphen Count
    features.append(
        1 if url.count("-") < 2
        else -1
    )

    #18. Login Keywords
    login_keywords = [
        "login",
        "signin",
        "verify",
        "authenticate"
    ]

    features.append(
        -1 if any(word in url.lower() for word in login_keywords)
        else 1
    )

    #19. Financial Keywords
    financial_keywords = [
        "paypal",
        "bank",
        "credit",
        "payment",
        "wallet"
    ]

    features.append(
        -1 if any(word in url.lower() for word in financial_keywords)
        else 1
    )

    #20. Long Domain Name
    features.append(
        1 if len(domain) < 20
        else -1
    )

    #21. Underscore Count
    features.append(
        1 if url.count("_") == 0
        else -1 
    )

    #22. Encoded Characters
    features.append(
        -1 if "%" in url
        else 1
    )

    #23. Excessive Digits
    digit_count = sum(c.isdigit()for c in url)

    features.append(
        1 if digit_count < 8
        else -1
    )

    #24. Path Length
    path = urlparse(url).path

    features.append(
        1 if len(path) < 25
        else -1
    )

    #25. Query Parameters
    features.append(
        1 if url.count("&") < 3
        else -1
    )

    while len(features) < 30:
        features.append(0)


    return features



