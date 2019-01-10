from . import *
"""
@Infrastructure
  ↳   Permissions      - /tmp must be writable by user running the        - Required  : (Type)
                          - installation.
                       - User must be a part of the KVM group.
                       - [--disk path=...] directory must be owned by User.
@Documentation
  [To-Do]   - Change Preseed variable name to Injection.
  [To-Do]   - Change @property, command to different, more descriptive name.
  [To-Do]   - Change install() to vps()
"""

class VirtualInstaller(object):
  def __init__(self, Preseed, ram = 512, cpu = 1):
    self.Preseed = Preseed
    self.RAM = ram
    self.vCores = cpu

    self.VPS = VPS(Preseed.IP, Preseed.hostname, Preseed.user, Preseed.password)
    #self.JumpServer = self.jump_server()

  def install(self, type = None):
    file_script = "/tmp/create_VPS.sh"

    script = open(file_script, "w+")
    script.write(self.command)
    script.close()

    provision = textwrap.dedent(
    f"""
    ssh snow@localhost "bash -s" -- < {file_script}
    """.strip()
    )

    file_preseed = "/tmp/preseed.cfg"
    preseed = open(file_preseed, "w+")

    if type == "basic":
      print("Injecting Basic Payload")
      preseed.write(self.Preseed.preseed_basic)
      preseed.close()
    elif type == "lamp":
      print("Injecting LAMP Payload")
      preseed.write(self.Preseed.preseed_lamp)
      preseed.close()
    else:
      print("Injecting Minimal Payload")
      preseed.write(self.Preseed.preseed_minimal)
      preseed.close()

    time.sleep(1)

    subprocess.call([file_script])

  def ssh(self):
    pass


  @property
  def command(self):
    NAME = self.Preseed.hostname
    DISK = self.Preseed.hostname
    RAM = self.RAM
    CPU = self.vCores
    PRESEED = "/tmp/preseed.cfg"
    MIRROR = "http://mirrors.rit.edu/ubuntu/dists/bionic/main/installer-amd64/"
    ISO = os.path.dirname(os.path.realpath(__file__)) + "/_Images/" + "Bionic-Server.iso"
    PATH_DEFAULT = "/var/lib/libvirt/images/"

    slash = "\\"

    command = textwrap.dedent(
      f"""
      #!/bin/bash
      virt-install {slash}
      --nographics {slash}
      --noautoconsole {slash}
      --name {NAME} {slash}
      --ram {RAM} {slash}
      --disk path={PATH_DEFAULT}{DISK}.qcow2,size=50 {slash}
      --location "{ISO}" {slash}
      --initrd-inject={PRESEED} {slash}
      --vcpus {CPU} {slash}
      --os-type linux {slash}
      --os-variant ubuntu18.04 {slash}
      --autostart {slash}
      --extra-args="console=ttyS0"
      """
    ).strip()

    return command

  @property
  def ssh_setup(self):
    NAME = self.Preseed.hostname
    DISK = self.Preseed.hostname
    RAM = self.RAM
    CPU = self.vCores
    PRESEED = "/tmp/preseed.cfg"
    MIRROR = "http://mirrors.rit.edu/ubuntu/dists/bionic/main/installer-amd64/"
    ISO = os.path.dirname(os.path.realpath(__file__)) + "/_Images/" + "Bionic-Server.iso"
    PATH_DEFAULT = "/var/lib/libvirt/images/"

    slash = "\\"

    command = textwrap.dedent(
      f"""
      #!/bin/bash
      virt-install {slash}
      --nographics {slash}
      --noautoconsole {slash}
      --name {NAME} {slash}
      --ram {RAM} {slash}
      --disk path={PATH_DEFAULT}{DISK}.qcow2,size=50 {slash}
      --location "{ISO}" {slash}
      --initrd-inject={PRESEED} {slash}
      --vcpus {CPU} {slash}
      --os-type linux {slash}
      --os-variant ubuntu18.04 {slash}
      --autostart {slash}
      --extra-args="console=ttyS0"
      """
    ).strip()

    return command
