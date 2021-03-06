from . import *
class VPS(object):
  """
  @Infrastructure
    ↳   SSH-Keys    - SSH keys must be set from the         - Required  : (RSA-Key)
                    | - host --> client if the
                    | - host server is different.
  @Parameters
    ↳   IP          - The IP address of the VPS.            - Required  : (Command-Line)
                    | - @To-Do: Get IP from SQL,
                    |   - and create error when
                    |   - subnet is full.
                    | - Defaults to NAT.
  @Documentation
    [Note]    - "VPS().hostname" will print out the actual function return hostname.
              - The @property returns a true object property, but is not static.
  """
  def __init__(self):
    pass
    
  @property
  def hostname(self):
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode('utf-8'))
    hash_decoded = hash.hexdigest()
    hash_decoded = hash.hexdigest()[:-30]

    hostname = ("vault-" + hash_decoded + ".vps.vaultcipher.com")
    return hostname
