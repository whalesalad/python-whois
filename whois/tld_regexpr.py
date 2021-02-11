import re

DOMAIN_NAME_RE = r'Domain Name:\s?(.+)'
REGISTRAR_RE = r'Registrar:\s?(.+)'
CREATION_DATE_RE = r'Creation Date:\s?(.+)'
EXPIRATION_DATE_RE = r'Registry Expiry Date:\s?(.+)'
STATUS_RE = r'[S|s]tatus:\s?(.+)'

TLD_COM = {
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                REGISTRAR_RE,
    'registrant':               r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',

    'nameservers':             r'Name Server:\s*(.+)\s*',
    'status':                   STATUS_RE,
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

TLD_NL = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'nameservers':             r'Domain nameservers:(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?\n?',
}

TLD_NET = {
    **TLD_COM,
}

TLD_ORG = {
    **TLD_COM,
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nLast Updated On:\s?(.+)',
    'nameservers':             r'Name Server:\s?(.+)\s*',
}

TLD_UK = {
    **TLD_COM,
    'registrant':               r'Registrant:\n\s*(.+)',
    'creation_date':            r'Registered on:\s*(.+)',
    'expiration_date':          r'Expiry date:\s*(.+)',
    'updated_date':             r'Last updated:\s*(.+)',
    'nameservers':             r'Name Servers:\s*(.+)\s*',
    'status':                   r'Registration status:\n\s*(.+)',
}

TLD_AC_UK = {
    **TLD_UK,
    'domain_name':              r'Domain:\n\s?(.+)',
    'owner':                    r'Domain Owner:\n\s?(.+)',
    'registrar':                r'Registered By:\n\s?(.+)',
    'registrant':               r'Registered Contact:\n\s*(.+)',
    'expiration_date':          r'Renewal date:\n\s*(.+)',
    'updated_date':             r'Entry updated:\n\s*(.+)',
    'nameservers':             r'Servers:\s*(.+)\t\n\s*(.+)\t\n',
    'creation_date':            r'Entry created:\n\s?(.+)'
}

TLD_PL = {
    **TLD_UK,
    'registrar':                r'\nREGISTRAR:\s*(.+)\n',
    'creation_date':            r'\ncreated:\s*(.+)\n',
    'updated_date':             r'\nlast modified:\s*(.+)\n',
    'expiration_date':          r'\noption expiration date:\s*(.+)\n',
    'nameservers':             r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status':                   r'\nStatus:\n\s*(.+)',
}

TLD_RU = {
    **TLD_COM,
    'domain_name':              r'\ndomain:\s*(.+)',
    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',
    'nameservers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',
}

TLD_RU_RF = {
    **TLD_COM,
    'domain_name':              r'\ndomain:\s*(.+)',
    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',
    'nameservers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',
}

TLD_UA = {
    **TLD_COM,
    'domain_name':              r'\ndomain:\s*(.+)',
    'registrar':                r'\nregistrar:\s*(.+)',
    'registrant_country':       r'\ncountry:\s*(.+)',
    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\nexpires:\s*(.+)',
    'updated_date':             r'\nmodified:\s*(.+)',
    'nameservers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstatus:\s*(.+)',
}

TLD_LT = {
    **TLD_COM,
    'status':                   r'\nStatus:\s?(.+)',
    'domain_name':              r'Domain:\s?(.+)',
    'creation_date':            r'Registered:\s?(.+)',
    'expiration_date':          r'Expires:\s?(.+)',
    'nameservers':             r'Nameserver:\s*(.+)\s*',
}

TLD_LV = {
    **TLD_RU,
    'creation_date':            r'Registered:\s*(.+)\n',
    'updated_date':             r'Changed:\s*(.+)\n',
    'status':                   STATUS_RE,
}

TLD_JP = {
    'domain_name':              r'\[Domain Name\]\s?(.+)',
    'registrar':                None,
    'registrant':               r'\[Registrant\]\s?(.+)',
    'creation_date':            r'\[登録年月日\]\s?(.+)',
    'expiration_date':          r'\[有効期限\]\s?(.+)',
    'updated_date':             r'\[最終更新\]\s?(.+)',
    'nameservers':             r'\[Name Server\]\s*(.+)',
    'status':                   r'\[状態\]\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

TLD_CO_JP = {
    **TLD_JP,
    'domain_name':              r'\[ドメイン名\]\s?(.+)',
    'creation_date':            r'\[登録年月\]\s?(.+)',
    'expiration_date':          r'\[状態\].+\((.+)\)',
    'updated_date':             r'\[最終更新\]\s?(.+)',
}

TLD_DE = {
    **TLD_COM,
    'domain_name':              r'\ndomain:\s*(.+)',
    'updated_date':             r'\nChanged:\s?(.+)',
    'nameservers':             r'Nserver:\s*(.+)',
}

TLD_AT = {
    **TLD_COM,
    'domain_name':              r'domain:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',
    'nameservers':             r'nserver:\s*(.+)',
}

TLD_EU = {
    **TLD_COM,
    'domain_name':              r'\ndomain:\s*(.+)',
    'registrar':                r'Name:\s?(.+)',
}

TLD_BIZ = {
    **TLD_COM,
    'registrar':                REGISTRAR_RE,
    'registrant':               r'Registrant Organization:\s?(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    # 'status':                   None,
}

TLD_IN = {
    **TLD_COM,
}

TLD_INFO = {
    **TLD_COM
}

TLD_NAME = {
    **TLD_COM,
    'status':                   r'Domain Status:\s?(.+)',
}

TLD_US = {
    **TLD_NAME,
}

TLD_CO = {
    **TLD_BIZ,
    'status':                   STATUS_RE,
}

TLD_ME = {
    **TLD_BIZ,
    'creation_date':            r'Domain Create Date:\s?(.+)',
    'expiration_date':          r'Domain Expiration Date:\s?(.+)',
    'updated_date':             r'Domain Last Updated Date:\s?(.+)',
    'nameservers':             r'Nameservers:\s?(.+)',
    'status':                   r'Domain Status:\s?(.+)',
}

TLD_BE = {
    **TLD_PL,
    'domain_name':              r'\nDomain:\s*(.+)',
    'registrar':                r'Company Name:\n?(.+)',
    'creation_date':            r'Registered:\s*(.+)\n',
    'status':                   STATUS_RE,
}

TLD_NZ = {
    'domain_name':              r'domain_name:\s?(.+)',
    'registrar':                r'registrar_name:\s?(.+)',
    'registrant':               r'registrant_contact_name:\s?(.+)',
    'creation_date':            r'domain_dateregistered:\s?(.+)',
    'expiration_date':          r'domain_datebilleduntil:\s?(.+)',
    'updated_date':             r'domain_datelastmodified:\s?(.+)',
    'nameservers':             r'ns_name_[0-9]{2}:\s?(.+)',
    'status':                   r'query_status:\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

TLD_CZ = {
    **TLD_COM,

    'domain_name':              r'Domain:\s?(.+)',
    'registrar':                REGISTRAR_RE,
    'registrant':               r'registrant:\s?(.+)',

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'nameservers':             r'nserver:\s*(.+) ',
}

TLD_IT = {
    **TLD_COM,

    'domain_name':              r'Domain:\s?(.+)',
    'registrar':                r'Registrar:\s*Organization:\s*(.+)',
    'registrant':               r'Registrant:\s?Name:\s?(.+)',

    'creation_date':            r'Created:\s?(.+)',
    'expiration_date':          r'Expire Date:\s?(.+)',
    'updated_date':             r'Last Update:\s?(.+)',

    'nameservers':             r'Nameservers:\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_FR = {
    **TLD_COM,

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s*(.+)',
    'registrant':               r'contact:\s?(.+)',

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'Expiry Date:\s?(.+)',
    'updated_date':             r'last-update:\s?(.+)',

    'nameservers':             r'nserver:\s*(.+)',
    'status':                   STATUS_RE,
}

TLD_IO = {
    **TLD_COM,
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
}

TLD_BR = {
    **TLD_COM,
    'domain_name':              r'domain:\s?(.+)',
    'registrar':                'nic.br',
    'registrant':               None,
    'owner':                    r'owner:\s?(.+)',
    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',
    'nameservers':             r'nserver:\s*(.+)',
    'status':                   STATUS_RE,
}

TLD_MX = {
    'domain_name':              DOMAIN_NAME_RE,
    'registrant':               r'Registrant:\n\s*(.+)',
    'registrar':                REGISTRAR_RE,
    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)',
    'nameservers':             r'\sDNS:\s*(.+)',
}

TLD_SH = {
    **TLD_COM,
    'expiration_date':         r'\nRegistry Expiry Date:\s*(.+)',
    'registrant':              r'\nRegistrant Organization:\s?(.+)',
    'status':                  r'\nDomain Status:\s?(.+)',
}

TLD_VIDEO = {
    **TLD_COM,
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}

TLD_MOBI = {
    **TLD_COM,
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}

TLD_UZ = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_ID = {
    **TLD_COM,
    'registrar':                r'Sponsoring Registrar Organization:\s?(.+)',
    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)$',
}


TLD_STORE = {
    **TLD_COM,
    'registrar':                REGISTRAR_RE,
    'registrant':               r'Registrant Organization:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'nameservers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)'
}

TLD_REST = {
    **TLD_STORE,
}

TLD_SECURITY = {
    **TLD_STORE,
}

TLD_SITE = {
    **TLD_STORE,
}

TLD_WEBSITE = {
    **TLD_STORE,
}

TLD_TICKETS = {
    **TLD_STORE,
}

TLD_THEATRE = {
    **TLD_STORE,
}

TLD_TECH = {
    **TLD_STORE,
}

TLD_SPACE = {
    **TLD_STORE,
}

TLD_DOWNLOAD = {
    **TLD_STORE,
    'nameservers':             r'Name Server:\s*(.+)\r',
    'status':                   r'Domain Status:\s*([a-zA-z]+)'
}

TLD_XYZ = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_TEL = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_TV = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_CC = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_NYC = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_PW = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_ONLINE = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_WIKI = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_PRESS = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_PHARMACY = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   STATUS_RE,
}

TLD_KR = {
    **TLD_COM,
    'domain_name':              r'Domain Name\s*:\s?(.+)',
    'registrar':                r'Authorized Agency\s*:\s*(.+)',
    'registrant':               r'Registrant\s*:\s*(.+)',
    'creation_date':            r'Registered Date\s*:\s?(.+)',
    'expiration_date':          r'Expiration Date\s*:\s?(.+)',
    'updated_date':             r'Last Updated Date\s*:\s?(.+)',
    'status':                   r'status\s*:\s?(.+)',
}

TLD_CN = {
    **TLD_COM,
    'registrar':                r'Sponsoring Registrar:\s?(.+)',
    'registrant':               r'Registrant:\s?(.+)',
    'creation_date':            r'Registration Time:\s?(.+)',
    'expiration_date':          r'Expiration Time:\s?(.+)'
}

TLD_EDU = {
    **TLD_COM,
    'registrant':               r'Registrant:\s*(.+)',
    'creation_date':            r'Domain record activated:\s?(.+)',
    'updated_date':             r'Domain record last updated:\s?(.+)',
    'expiration_date':          r'Domain expires:\s?(.+)',
    'nameservers':             r'Name Servers:\s?\t(.+)\n\t(.+)\n'
}


TLD_KZ = {
    'domain_name':              r'Domain name\.+:\s(.+)',
    'registrar':                r'Current Registar:\s(.+)',
    'expiration_date':          None,
    'nameservers':             r'server.*:\s(.+)',
    'creation_date':            r'Domain created:\s(.+)',
    'updated_date':             r'Last modified :\s(.+)'
}

TLD_CL = {
    **TLD_COM,
    'registrar':                'nic.cl',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'nameservers':             r'Name Server:\s*(.+)\s*',
}

TLD_AR = {
    **TLD_COM,
    'domain_name':              r'domain\s*:\s?(.+)',
    'registrar':                REGISTRAR_RE,
    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed\s*:\s?(.+)',
    'nameservers':             r'nserver:\s*(.+)\s*',
}

TLD_CLUB = {
    **TLD_COM
}

TLD_EDUCATION = {
    **TLD_COM,
    'registrant':               r'Registrant Organization:\s?(.+)',
    'expiration_date':          r'Registrar Registration Expiration Date:\s?(.+)',
    'status':                   r'Domain Status:\s?(.+)',
}

TLD_NINJA = {
    **TLD_EDUCATION
}

TLD_IS_IS = {
    'domain_name':                         r'domain:\s?(.+)',
    'registrar':                           None,
    'registrant':                          r'registrant:\s?(.+)',
    'creation_date':                       r'created:\s?(.+)',
    'expiration_date':                     r'expires:\s?(.+)',
    'updated_date':                        None,
    'nameservers':                        r'nserver:\s?(.+)',
    'status':                              None,
    'emails':                              r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

TLD_IR = {
    'registrar': 'nic.ir',
    'creation_date': None,
    'status': None,
    'domain_name':                      r'domain:\s?(.+)',
    'expiration_date':                  r'expire-date:\s?(.+)',
    'updated_date':                     r'last-updated:\s?(.+)',
    'nameservers':                     r'nserver:\s*(.+)\s*',
}

TLD_SE = {
    'domain_name':              r'domain:\s?(.+)',
    'registrar':                REGISTRAR_RE,
    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'modified:\s?(.+)',
    'nameservers':             r'nserver:\s*(.+)',
    'status':                   STATUS_RE,
}

TLD_NU = {
    **TLD_SE
}

TLD_FI = {
    'domain_name':              r'domain\.+:\s?(.+)',
    'registrar':                r'registrar\.+:\s?(.+)',
    'creation_date':            r'created\.+:\s?(.+)',
    'expiration_date':          r'expires\.+:\s?(.+)',
    'updated_date':             r'modified\.+:\s?(.+)',
    'nameservers':             r'nserver\.+:\s*(.+)',
    'status':                   r'status\.+:\s?(.+)',
}

TLD_AU = {
    **TLD_COM,
    'registrar':                r'Registrar Name:\s?(.+)',
    'updated_date':             r'Last Modified:\s?(.+)'
}

TLD_COM_AU = {
    **TLD_AU
}

TLD_WORK = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
}

TLD_BANK = {
    **TLD_COM,
    'domain_name':              DOMAIN_NAME_RE,
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            CREATION_DATE_RE,
    'expiration_date':          EXPIRATION_DATE_RE,
    'updated_date':             r'Updated Date:\s?(.+)',
}

TLD_CA = {
    **TLD_COM,
}
# TLD_CA = {
#     **TLD_BANK,
# }

TLD_RW = {
    **TLD_BANK,
}

TLD_MU = {
    **TLD_BANK,
}

UNCOMPILED_TLD_RE = {
  'ac_uk': TLD_AC_UK,
  'ar': TLD_AR,
  'at': TLD_AT,
  'au': TLD_AU,
  'bank': TLD_BANK,
  'be': TLD_BE,
  'biz': TLD_BIZ,
  'br': TLD_BR,
  'ca': TLD_CA,
  'cc': TLD_CC,
  'cl': TLD_CL,
  'club': TLD_CLUB,
  'cn': TLD_CN,
  'co': TLD_CO,
  'co_jp': TLD_CO_JP,
  'com': TLD_COM,
  'com_au': TLD_COM_AU,
  'cz': TLD_CZ,
  'de': TLD_DE,
  'download': TLD_DOWNLOAD,
  'edu': TLD_EDU,
  'education': TLD_EDUCATION,
  'eu': TLD_EU,
  'fi': TLD_FI,
  'fr': TLD_FR,
  'id': TLD_ID,
  'in': TLD_IN,
  'info': TLD_INFO,
  'io': TLD_IO,
  'ir': TLD_IR,
  'is_is': TLD_IS_IS,
  'it': TLD_IT,
  'jp': TLD_JP,
  'kr': TLD_KR,
  'kz': TLD_KZ,
  'lt': TLD_LT,
  'lv': TLD_LV,
  'me': TLD_ME,
  'mobi': TLD_MOBI,
  'mu': TLD_MU,
  'mx': TLD_MX,
  'name': TLD_NAME,
  'net': TLD_NET,
  'ninja': TLD_NINJA,
  'nl': TLD_NL,
  'nu': TLD_NU,
  'nyc': TLD_NYC,
  'nz': TLD_NZ,
  'online': TLD_ONLINE,
  'org': TLD_ORG,
  'pharmacy': TLD_PHARMACY,
  'pl': TLD_PL,
  'press': TLD_PRESS,
  'pw': TLD_PW,
  'rest': TLD_REST,
  'ru': TLD_RU,
  'ru_rf': TLD_RU_RF,
  'rw': TLD_RW,
  'se': TLD_SE,
  'security': TLD_SECURITY,
  'sh': TLD_SH,
  'site': TLD_SITE,
  'space': TLD_SPACE,
  'store': TLD_STORE,
  'tech': TLD_TECH,
  'tel': TLD_TEL,
  'theatre': TLD_THEATRE,
  'tickets': TLD_TICKETS,
  'tv': TLD_TV,
  'ua': TLD_UA,
  'uk': TLD_UK,
  'us': TLD_US,
  'uz': TLD_UZ,
  'video': TLD_VIDEO,
  'website': TLD_WEBSITE,
  'wiki': TLD_WIKI,
  'work': TLD_WORK,
  'xyz': TLD_XYZ
}

TLD_RE = {
    tld: dict(
        (k, re.compile(v, re.IGNORECASE) if isinstance(v, str) else v)
        for k, v in mapping.items()
    )

    for tld, mapping in UNCOMPILED_TLD_RE.items()
}
