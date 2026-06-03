import logging
import platform
import re
import subprocess
 
from pydantic import BaseModel, EmailStr
 
logger = logging.getLogger(__name__)
 
 
# partie 1 exo 1
 
def resoudre_ip(hote: str) -> str | None:
    os_name = platform.system()
 
    if os_name in ("Linux", "Darwin"):
        try:
            proc = subprocess.run(
                ["host", hote],
                capture_output=True,
                text=True,
                timeout=5.0,
            )
            if proc.returncode == 0:
                match = re.search(r"has address\s+((?:\d{1,3}\.){3}\d{1,3})", proc.stdout)
                if match:
                    return match.group(1)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
 
    try:
        proc = subprocess.run(
            ["nslookup", hote],
            capture_output=True,
            text=True,
            timeout=5.0,
        )
    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired:
        return None
 
    if proc.returncode != 0:
        return None
 
    output = proc.stdout
    non_auth = output.find("Non-authoritative answer")
    if non_auth != -1:
        output = output[non_auth:]
 
    match = re.search(r"Address:\s*((?:\d{1,3}\.){3}\d{1,3})", output)
    if match:
        return match.group(1)
 
    return None
 
 
# partie 1 exo 2
 
def interroger_whois(hote: str) -> tuple[str | None, str | None]:
    try:
        proc = subprocess.run(
            ["whois", hote],
            capture_output=True,
            text=True,
            timeout=10.0,
        )
    except FileNotFoundError:
        return None, None
    except subprocess.TimeoutExpired:
        return None, None
 
    if proc.returncode != 0:
        return None, None
 
    output = proc.stdout
 
    contact = None
    for pattern in (r"Registrant Name:\s*(.+)", r"Registrant:\s*(.+)"):
        match = re.search(pattern, output, re.IGNORECASE)
        if match:
            valeur = match.group(1).strip()
            if valeur:
                contact = valeur
                break
 
    email = None
    match = re.search(r"\S+@\S+", output)
    if match:
        email = match.group(0).rstrip(".,;)")
 
    return contact, email
 
 
# partie 1 exo 3
 
class Domaine(BaseModel):
    hote: str
    ip: str | None
    contact: str | None
    email: EmailStr | None
 
 
def collecter(hote: str) -> Domaine:
    ip = resoudre_ip(hote)
    contact, email = interroger_whois(hote)
    return Domaine(hote=hote, ip=ip, contact=contact, email=email)
 
 
if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    cible = sys.argv[1] if len(sys.argv) > 1 else "example.com"
    print(collecter(cible).model_dump_json(indent=2))
