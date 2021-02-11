import subprocess

from .exceptions import WHOISCommandFailed, WHOISCommandTimeout


DEFAULT_TIMEOUT = 10


def do_query(dl, ignore_returncode=False, timeout=None):
    """
    Linux 'whois' command wrapper

    """
    cmd = ['whois', dl]

    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env={"LANG": "ja"}
    )

    try:
        r = p.communicate(timeout=timeout or DEFAULT_TIMEOUT)[0]
    except subprocess.TimeoutExpired as e:
        raise WHOISCommandTimeout('Timeout') from e

    r = r.decode()

    if not ignore_returncode and p.returncode != 0 and p.returncode != 1:
        raise WHOISCommandFailed(r)

    return r
