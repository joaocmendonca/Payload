from . import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def main():
  # injection = Preseed(input.VPS[0], input.VPS[1], input.VPS[2], VPS().hostname)
  #
  # server = Host(input.Host[0], input.Host[1])
  # server.update_DNS(injection.IP, injection.hostname)

  Gateway("192.168.0.1", "snow").debug()

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
      "\n\n"
      +
      "--VPS [Username, Password, IP]".center(os.get_terminal_size().columns)
      +
      "\n"
      +
      "--Host [IP, SSH-Username]".center(os.get_terminal_size().columns)
      +
      "\n"
      +
      "--Proxy [TBD]".center(os.get_terminal_size().columns)
      +
      "\n"
      +
      "--Gateway [TBD]".center(os.get_terminal_size().columns)
      +
      "\n"
      ,""
    ),
    usage = """ --VPS, --Host, --Proxy, --Gateway """
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
