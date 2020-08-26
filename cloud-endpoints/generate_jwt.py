import time
import google.auth.crypt
import google.auth.jwt

sa_keyfile = 'path_of_service_account'
iss = 'email_address_of_service_account'
aud = 'hostname_of_your_gateway'
iat = int(time.time())
exp = iat + 3600

def generate_jwt():
    """Generates a signed JSON Web Token using a Google API Service Account."""
    payload = {"iat": iat, "exp": exp, "iss": iss, "aud":  aud, "sub": iss, "email": iss}

    signer = google.auth.crypt.RSASigner.from_service_account_file(sa_keyfile)
    jwt = google.auth.jwt.encode(signer, payload)
    return jwt

if __name__ == '__main__':
    signed_jwt = generate_jwt()
    print(signed_jwt.decode()+'\n')
