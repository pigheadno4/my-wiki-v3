<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/forward-api/cryptography -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Cryptography
slug: /docs/guides/extend/forward-api/cryptography/
createTime: '2025-04-02T01:57:47.516Z'
updateTime: '2025-04-02T01:57:47.802Z'
---



# Cryptography

**AVAILABILITY**
 **Use of the production**  [**Forward API**](/braintree/docs/reference/forward-api/overview/)  **is subject to eligibility.**   Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact).


## Overview

The Forward API contains a cryptographic toolkit that allows you to encrypt or sign parts of the outgoing request.     All card data emitted by the Forward API is already encrypted by industry-standard [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) so it is fully secured without using these cryptographic functions. However some destination APIs may require further security, necessitating the use of the below features.


## AES

**IMPORTANT**
 **AES keys are sensitive information and should always be transmitted securely.**   You should use the Forward API's [PGP public key](/braintree/docs/guides/extend/forward-api/pgp-key) to encrypt these keys before submitting them for use with Forward API configs.

 The Forward API supports encrypting data using AES in Galois Counter Mode (GCM). Taking advantage of this support requires using two functions, [aes-gcm](/braintree/docs/reference/forward-api/functions#aes-gcm) and [aes-gcm-nonce](/braintree/docs/reference/forward-api/functions#aes-gcm-nonce), and adding an array of keys to the config under [keys](/braintree/docs/reference/forward-api/config#keys).


### Steps


- Generate an AES nonce to encrypt with, usingaes-gcm-nonce. You will probably want to save it in a local variable ($/var/aes-noncein this example).
- Encrypt your data usingaes-gcm.
- Include the nonce somewhere in the request (so that the destination endpoint can decrypt).


### Example partial config

### JSON
```json
{
    "keys": [
        "0e42519c0eda67c22c52b605ff41fde395880ebf6ed40a560b5f5ecc8183d26a"
    ],
    "transformations": [
        {
            "path": "/var/aes-nonce",
            "value": ["aes-gcm-nonce"]
        },
        {
            "path": "/body/aes-nonce",
            "value": ["hex", "$/var/aes-nonce"]
        },
        {
            "path": "/body/payment_method/encrypted-pan",
            "value": ["hex", ["aes-gcm", 0, "$/var/aes-nonce", "$number"]]
        }
    ]
}
```


## RSA

The Forward API supports RSA public key encryption. Taking advantage of this support requires using two functions: [rsa-public-key](/braintree/docs/reference/forward-api/functions#rsa-public-key) and any one amongst [rsa-pkcs1](/braintree/docs/reference/forward-api/functions#rsa-pkcs1), [rsa-oaep-sha1](/braintree/docs/reference/forward-api/functions#rsa-oaep-sha1) or [rsa-oaep-sha256](/braintree/docs/reference/forward-api/functions#rsa-oaep-sha256).


### Steps


- Send a[PEM-encoded](https://en.wikipedia.org/wiki/Privacy-enhanced_Electronic_Mail)RSA public key on the request.
- Encrypt your data usingrsa-pkcs1,rsa-oaep-sha1orrsa-oaep-sha256.


### Example

### bash
```bash
curl -i https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
  -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-nonce",
    "debug_transformations": true,
    "url": "https://httpbin.org/post",
    "method": "POST",
    "data": {"public_key": "-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4c/yKBAkD8wbX7nNfDXL
hL9pMKwBZhEnbPprRjeAX/lelso424gFSZtq4X3LFamrDN59cN2RHqj7so/aK7rW
JJzj9y+lYxocJaNbyFXlZ9ctC0OcoqyqaTlKT0VmAa7EyQXtOsUy0r3nT1emdKTs
vpz/3sFZPyWVIQ2oG/ea+QjzQvUTt8njp3l7D1txGJ+XdtGKrxJ0EuhLJNirDjlY
et33agZOQJTnUzhYA2TJsZNo9zCj9b6DyIfNVeCN0o00r/Hm5d6zlKemKbOKWtSS
dY0wGqSZB+sew+tMZaWfSzij1FzGsfkVaG/VEeMgxZq7fYu+hCcFDDQlElwf1SwJ
qwIDAQAB
-----END PUBLIC KEY-----"},
    "config": {
      "name": "rsa_example",
      "methods": ["POST"],
      "url": "^https://httpbin\.org/post$",
      "request_format": {"/body": "json"},
      "types": ["CreditCard"],
      "transformations": [
        {"path": "/body/card/encrypted_number", "value": ["hex", ["rsa-pkcs1", ["rsa-public-key", "$public_key"], "$number"]]},
      ]
    }
  }'
```
 Note that the result of RSA encryption is non-deterministic.


## TLS mutual authentication

**IMPORTANT**
 **Mutual TLS private keys are sensitive information and should always be transmitted securely.**   You should use the Forward API's [PGP public key](/braintree/docs/guides/extend/forward-api/pgp-key) to encrypt these certificates before submitting them for use with Forward API configs.

 The Forward API supports certificate-based TLS [mutual authentication](https://en.wikipedia.org/wiki/Mutual_authentication), commonly referred to as "client certificate authentication". In sandbox, a PEM-encoded [client_cert](/braintree/docs/reference/forward-api/forward#client_cert) and [client_key](/braintree/docs/reference/forward-api/forward#client_key) may be passed per-request. In production, a certificate and key will be loaded with the config if necessary.


### Example

### bash
```bash
curl -i https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
  -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-nonce",
    "url": "https://httpbin.org/post",
    "method": "POST",
    "client_cert": "-----BEGIN CERTIFICATE-----
MIIEOTCCAiECCQCbbZRf/pKiyzANBgkqhkiG9w0BAQsFADBgMQswCQYDVQQGEwJV
UzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzES
MBAGA1UECgwJQnJhaW50cmVlMRAwDgYDVQQDDAdFeGFtcGxlMB4XDTE3MDkyMTIx
NDcwNloXDTE3MTAyMTIxNDcwNlowXTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNh
bGlmb3JuaWExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xITAfBgNVBAoMGEludGVy
bmV0IFdpZGdpdHMgUHR5IEx0ZDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
ggEBAM/D2UzYUYVtyzrI+4SmqW45HBmd6BYsS4RZ6qL40GLSba79H9Yw/Mmg4BZz
IaNDJBW+iuJRbRFUzpO+2FPBQ3kbaEMK8pKUiNsYbt+IhrodA9e/d36VMbjl0Ahe
XMuL+qfSTLlYBv9CpmeyoIcLiJ94QJL03A3dZ2IHs3qHm73oYcJ0WlOe1zwMF+Lb
Q//7kkzSPlQWgvBTCpADgKBZ9WSZtbzC4DSRMSytATFUOL6UvZhkLVCGyF4wAf6Z
Yqs5R4Tt/BEVsaPee4ZBLnpiRzevoP8lySMao6aGauN/xFNKkzDPARJXfkeP3BOr
Kzz351TYFE0ajF8bKxueHuTG3qsCAwEAATANBgkqhkiG9w0BAQsFAAOCAgEAcB/Z
wlI9fBT1h9MbyUj3d0J5YQUN9+YdyAXKXVNXDMixsGt7V+b/1rtYOtHEl6vpp2wy
U6Yf0/Qxd/Zt5pYwqaz7vYB8sKQTUw/YTY5JMDcPsytdhRtHVKfI38VyUbO3g0RA
kZ+Vr5175z1pXKDn3HtI96t0fjWV7YrCIW+YdD7+8XG4Wsmn5Oh5KeGsM8v2f6Fb
IrP1eT8h7OGnQFrlXr3QnPJzjBwiKcZCU1LE0fJI9KxYOXDj8KmuAPLjC+ZxD5SZ
HdOawRJJ8J2mdvnAEdXEOCwQHOiZ2AYHVR7v5MwdCFCg7TIKoYM7o/WWkURiLXmG
W92H0T6jV/Xc4agQEHX7SCOk3zFlcBwT3JNkizYnrI3X6T7OQcoeQWrmjGLAPlqt
mmjaUQc29hEbEVFeprHFCBHd1B3DMuMnVrxadO+ObBoQ3yd36+Puc09fyLd/u4Wq
Yc+s7qxZyaiBfh0S2vxvBQwqhBt8fmy36zMpGyjeia4nMtLGkqlys8ycX4RqX2op
m4q1wQ4gmxQHhfgDeAjX/pZ5uODFIZphsCWQZPNu5mt7kLzKBPRQMAnNxrntIpDI
D1Hh3lXUA7QNCxQKu4ZpnZPrb4Ag4/003yXUjuzEF7SP++dMz3r0B92UI3WcVwdO
wH6gK4IjPxv+quPBsDJdg5tJ6dtoMkOxklsB9MM=
-----END CERTIFICATE-----
",
    "client_key": "-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAz8PZTNhRhW3LOsj7hKapbjkcGZ3oFixLhFnqovjQYtJtrv0f
1jD8yaDgFnMho0MkFb6K4lFtEVTOk77YU8FDeRtoQwrykpSI2xhu34iGuh0D1793
fpUxuOXQCF5cy4v6p9JMuVgG/0KmZ7KghwuIn3hAkvTcDd1nYgezeoebvehhwnRa
U57XPAwX4ttD//uSTNI+VBaC8FMKkAOAoFn1ZJm1vMLgNJExLK0BMVQ4vpS9mGQt
UIbIXjAB/pliqzlHhO38ERWxo957hkEuemJHN6+g/yXJIxqjpoZq43/EU0qTMM8B
Eld+R4/cE6srPPfnVNgUTRqMXxsrG54e5MbeqwIDAQABAoIBAEFP9e2cSvRA8ZRH
PhoTMkv+FAFRjHX78rlmcsZMpWWLdQN/exSgTbcspYUpKDfkkWFshshihIDgQhhb
9DFQHd/iZ8I7nMnLe8I0ShZnGsNC/8RA4lWenQTc6arXzyAFnwRGrevN6lUwJJOQ
qboKPCa1bMdFxi9tnGRKu3cXTjRCWf4mKi2zI6qwQuCQvw2CdtpF+sCaPCOtcMI3
IkpAxc7lOBTZCdSnZ+EtO/Cs2Y/TSGCCCy/GWuJWUbWqY1fKVY9DJoJkupfGp7Gg
zRk4ZuXv+0EN74P3N36NjoOYVUPCp2NJBZCZ4snBQVbEkuvcSetxNmx1Ym7/cHKS
Zzt0ShECgYEA7FKWSyU6Uru6pOc6Gwdux38yk4tSzI/nWgc2tfUWmTNcRApoBjH4
6d42xENLRe/n1AdaoztS7477E5IaIN9Rzxsxa3gAToIYvlKAuWTOsPix/1ge5Y1F
Rzhpnjza2tEMHCstM8l72SA3ZDpXrkZVXeEn/l2U6UsbK82QfpA2/10CgYEA4RCI
iiZ/ih6zWK3ltNwARlVHumissLYj6WZhn67HZdbKfd+SUA+NXKWnToaw0gtHY73K
WDtn2pcTeuMjnYXZvD0xa+wS3WwQc10MsbKsA9Bp2M+YajwCZkY8pXhPQvmCchPE
iMwbpYGOwY8+V83pkQj7/DfLPHwIJ9aaqeAP3acCgYEAzlMkiKMOEqF4SPTgFC0f
GOoCvDKNra+N61oU+DPs8QCYc4cqXw5OJdEuu5eNJphYLRPmnFD1DdYle2a5jS2s
fUdelFeG3QRUmgXqAPL0Sio3LZpAD2aRr6ae/9pdsWGGUymXI3mruVuZQNZ3Kt6Z
NYeYpUoK8svyAwJMP1Ol0LkCgYAnzivH+00dWZawvXjeBvcJeXXJM1AvpNcvJYto
mZnsmhOQNaWEAWwoEahIjCvjylji/CM4fbE9iPDKEDgxWQYMc+o0wzkG7mDudmuT
Vh10Qz0lOnojd9+YxR1eyquCFe0LThG5fBf7qrFb7IDDOMjxfNxMXHXWib1Lhnou
R1GnCwKBgFmy+CJ/ZwanFHB7mGOP1es/zhqd/8P+Wlki/qwguzbowyZFuEKlsTVx
WY0ONVNZMft1u+wxm7lOgQXCqqjR58YsGx1eBaWWIXI+xpkRBv3hl7aApzoIJlQG
GlfIPxgoVjvXXRYLNj0Rw9xlF8T63NkQDa24StnYzeHM1oGCCcOz
-----END RSA PRIVATE KEY-----
",
    "config": {
      "name": "tls_mutual_auth_example",
      "methods": ["POST"],
      "url": "^https://httpbin\.org/post$",
      "request_format": {"/body": "json"},
      "types": ["CreditCard"],
      "transformations": []
    }
  }'
```


## Additional Features

You can find additional signing and encryption features in the [functions](/braintree/docs/reference/forward-api/functions) reference.



[Next Page:PGP Public Key→](/braintree/docs/guides/extend/forward-api/pgp-key)

