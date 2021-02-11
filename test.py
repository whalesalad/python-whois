import sys
import whois

DOMAINS = '''
    netsec.ninja
    test.education
    doramy.club
    google.cl
    google.in
    google.com.ar
    google.com.co
    google.pl
    google.com.br
    www.google.com
    www.fsdfsdfsdfsd.google.com
    digg.com
    imdb.com
    microsoft.com
    www.google.org
    ddarko.org
    google.net
    www.asp.net
    www.ddarko.pl
    google.co.uk
    google.jp
    www.google.co.jp
    google.io
    google.co
    google.de
    yandex.ru
    google.us
    google.eu
    google.me
    google.be
    google.lt
    google.biz
    google.info
    google.name
    google.it
    google.cz
    google.fr
    dfsdfsfsdf
    test.ez.lv
    google.store
    kono.store
    wonder.store
    viacom.tech
    google.tech
    google.space
    loop.space
    bloom.space
    invr.space
    buzzi.space
    theobservatory.space
    google.security
    pep.security
    token.security
    juniper.security
    ci.security
    in.security
    autobuyer.site
    emeralds.site
    darkops.site
    google.site
    manniswindows.site
    google.website
    discjockey.website
    anthropology.website
    livechat.website
    google.tickets
    google.theatre
    google.xyz
    google.tel
    google.tv
    google.cc
    google.nyc
    google.pw
    google.online
    google.wiki
    google.press
    google.se
    google.nu
    google.fi
    google.is
    afilias.com.au
    jisc.ac.uk
    google.com.au
    register.bank
    yandex.ua
    google.ca
    google.mu
    google.rw
    bit.ly
    gopro.com
'''

def test_domain(domain):
    print('-'*80)
    print(domain)

    w = whois.query(domain, ignore_returncode=1)

    if w:
        for k, v in w.__dict__.items():
            print('%20s\t%s' % (k, v))

    else:
        print('no result')


def do_complete_test():
    failures = list()

    all_domains = sorted(filter(None, {d.strip() for d in DOMAINS.split('\n')}))

    for d in all_domains:
        try:
            test_domain(d)

        except whois.WHOISException as e:
            failures.append(d)
            print(f"""
            Error : {e},
            Domain: {d}
            """)

    report_str = f"""
    Failures: {len(failures)}
    Domains : {failures}
    """

    print('\033[91m' + report_str + '\x1b[0m')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        domain = sys.argv[1]
        test_domain(domain)
    else:
        do_complete_test()
