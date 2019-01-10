"""
@Infrastructure
  ↳   SSH-Keys    - SSH keys must be set from the         - Required  : (RSA-Key)
                  | - host --> client.
                  | - For testing purposes, add SSH
                  | - keys to and from localhost.
@Parameters
  ↳   Server      - The IP address or verified hostname   - Required  : (Command-Line)
                  | - of the target server hosting the
                  | - VPS. Defaults to localhost.
@Documentation
  [Note]    - When packaging the program, {script} may not work correct. The path relative
            - to its execution potentially could be the problem.
  [To-Do]   - Update @Parameters

"""

from . import *
from Payload._Shell.__Shell import Shell

class Host(object):
  def __init__(self, server = "localhost", user = "snow"):
    self.server = server
    self.user = user

  def update_DNS(self, vps_ip, vps_hostname):
    script = "/tmp/update_DNS.sh"

    script_file = open(script, "w+")
    script_file.write(self.dns_script(vps_ip, vps_hostname))
    script_file.close()

    command = textwrap.dedent(
    f"""
    ssh {self.user}@{self.server} "bash -s" -- < {script}
    """.strip()
    )

    time.sleep(1)

    Shell(command).execute()

  @staticmethod
  def dns_script(vps_ip, vps_hostname):
    open = "{"
    close = "}"
    tab = "\t"

    dns = "/etc/hosts"

    script = textwrap.dedent(
      f"""
      #!/bin/bash
      {open}
        echo -e "{vps_ip}{tab}{vps_hostname}" >> {dns}
      {close} || {open}
        echo "Target Server does not have ownership of file {dns}"
      {close}
      """
    ).strip()

    return script
