import re
from .exceptions import WHOISParsingFailed
from .tld_regexpr import TLD_RE


def do_parse(whois_str, tld):
    r = {}

    if whois_str.count('\n') < 5:
        s = whois_str.strip().lower()
        if s == 'not found':
            return
        if s.startswith('no such domain'):
            # could feed startswith a tuple of strings of expected reponses
            return
        if s.count('error'):
            return
        raise WHOISParsingFailed(whois_str)

    # check the status of DNSSEC
    r['DNSSEC'] = False

    whois_dnssec = whois_str.split("DNSSEC:")
    if len(whois_dnssec) >= 2:
        whois_dnssec = whois_dnssec[1].split("\n")[0]
        if whois_dnssec.strip() == "signedDelegation":
            r['DNSSEC'] = True

    # split whois_str to remove first IANA part showing info for TLD only
    whois_splitted = whois_str.split("source:       IANA")
    if len(whois_splitted) == 2:
        whois_str = whois_splitted[1]

    server_name = re.findall(r'Server Name:\s?(.+)', whois_str, re.IGNORECASE)
    if server_name:
        whois_str = whois_str[whois_str.find('Domain Name:'):]

    for key, expression in TLD_RE.get(tld, TLD_RE['com']).items():
        if expression is None:
            r[key] = ['']
        else:
            r[key] = expression.findall(whois_str) or ['']

    return r
