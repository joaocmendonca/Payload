from . import *
from Payload._Network.__VPS import VPS
class Host(object):
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
  def __init__(self, debugger = "False", server = "localhost", dns = ""):
    self.server = server
    self.update_DNS_arguments = dns

    self.VPS = VPS()

    self.update_DNS_script = os.path.dirname(os.path.realpath(__file__)) + "/" + "__example.remote_ssh_script.sh"

    self.update_DNS_command = textwrap.dedent(
      f"""
      ssh localhost "bash -s" -- < {self.update_DNS_script} {str(self.update_DNS_arguments)}
      """.strip()
    )

    if debugger is not "False":
      print(Host.debugger.__get__(self))

  def update_DNS(self):
    subprocess.run(self.update_DNS_command, shell = True)

  @property
  def debugger(self):
    result = textwrap.dedent(
      f"""
      @Attributes
        ↳ {self.server}
        ↳ {self.VPS}
        ↳ {self.update_DNS_script}
        ↳ {self.update_DNS_command}
      """.strip()
    )
    return result
