from . import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def main():
  # preseed = Preseed("snow", "Knowledge", "192.168.1.255", VPS().hostname)
  # vInstaller = VirtualInstaller(preseed)
  #
  # vInstaller.install()
  #
  # Display(1000).display()
  #
  # subprocess.run(f"virsh start {vInstaller.Preseed.hostname}", shell = True)


  """
                      Payload Injection Object

  @Arguments
    ↳ Preseed(vps_username, vps_password, [--VPS-IP {"0.0.0.0"}], [VPS().hostname])

  @Defaults
    ↳ Preseed("bionic", "bionic", "192.168.0.255", "VPS-Bionic")
  """

  injection = Preseed(input.VPS[0], input.VPS[1], input.VPS[2], VPS().hostname)

  """
                        Target Host Object

  @Arguments
    ↳ Host(host_ssh_ip, host_ssh_user)

  @Defaults
    ↳ Host("localhost", "snow")
  """

  server = Host(input.Host[0], input.Host[1])

  """
                      Update Host DNS Records

  @Arguments
    ↳ update_DNS(injection.IP, injection.hostname)
  """

  server.update_DNS(injection.IP, injection.hostname)



if __name__ == '__main__':
  parser = ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter,
    description = textwrap.indent(
      "Virtual Private Server Payload".center(os.get_terminal_size().columns)
      +
      "\n\n"
      +
      "Jacob B. Sanders | © Vault Cipher LLC. | developer.vault@gmail.com".center(os.get_terminal_size().columns)
      +
      "\n"
      +
      """
      Development:
        @Package(s)
          Payload                       - Package         : (Primary)
          | __init__.py                 - Initializer     : (File/.py)
          | __main__.py                 - Executable      : (File/.py)
          | ↳ --help                    - Command-Line    : (None)

        @Module(s)
          _Installation                 - Module          : (Module/Primary)
          | __init__.py                 - Initializer     : (File/.py)
          | __Installation.py           - Executable      : (File/.py)
          | ↳ --help                    - Command-Line    : (None)

          _Shell                        - Module          : (Module/Primary)
          | __init__.py                 - Initializer     : (File/.py)
          | ↳ --shell                   - Command-Line    : (Array/String)
          | ↳ --interactive             - Command-Line    : (Array/String)
          | ↳ --help                    - Command-Line    : (None)
      """,
      ""
    ),
    usage = textwrap.indent(
      """

      ----------------------------------------------------
      | --VPS [Username, Password, IP]                   |
      ----------------------------------------------------
      | --Host [IP, SSH-Username]                        |
      ----------------------------------------------------
      | --Proxy [TBD]                                    |
      ----------------------------------------------------
      | --Gateway [TBD]                                  |
      ----------------------------------------------------
      | --help || -h                                     |
      ----------------------------------------------------
      """,
      ""
    )
  )

  parser.add_argument(
    "--VPS",
    nargs = "+",
    type = str,
    default = ["snow", "Knowledge", "192.168.1.255"],
    required = False
  )

  parser.add_argument(
    "--Host",
    nargs = "+",
    type = str,
    default = ["localhost", "snow"],
    required = False
  )

  parser.add_argument(
    "--Proxy",
    nargs = "+",
    type = str,
    required = False
  )

  parser.add_argument(
    "--Gateway",
    nargs = "+",
    type = str,
    required = False
  )

  input = parser.parse_args()

  main()
