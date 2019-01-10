from . import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def main():
  v = Host("True", "localhost", "File txt")
  v.update_DNS()

if __name__ == '__main__':
  # parser = ArgumentParser(
  #   formatter_class = argparse.RawDescriptionHelpFormatter,
  #   description = textwrap.indent(
  #     "Virtual Private Server Payload".center(os.get_terminal_size().columns)
  #     +
  #     "\n\n"
  #     +
  #     "Jacob B. Sanders | © Vault Cipher LLC. | developer.vault@gmail.com".center(os.get_terminal_size().columns)
  #     +
  #     "\n"
  #     +
  #     """
  #     Development:
  #       @Package(s)
  #         Payload                       - Package         : (Primary)
  #         | __init__.py                 - Initializer     : (File/.py)
  #         | __main__.py                 - Executable      : (File/.py)
  #         | ↳ --help                    - Command-Line    : (None)
  #
  #       @Module(s)
  #         _Installation                 - Module          : (Module/Primary)
  #         | __init__.py                 - Initializer     : (File/.py)
  #         | __Installation.py           - Executable      : (File/.py)
  #         | ↳ --help                    - Command-Line    : (None)
  #
  #         _Shell                        - Module          : (Module/Primary)
  #         | __init__.py                 - Initializer     : (File/.py)
  #         | ↳ --shell                   - Command-Line    : (Array/String)
  #         | ↳ --interactive             - Command-Line    : (Array/String)
  #         | ↳ --help                    - Command-Line    : (None)
  #     """,
  #     ""
  #   ),
  #   usage = textwrap.dedent(
  #     "| --shell | --interactive | --help |"
  #   )
  #   # epilog = "Jacob B. Sanders | © Vault Cipher LLC. | developer.vault@gmail.com".center(os.get_terminal_size().columns)
  # )
  #
  # parser.add_argument(
  #   "--shell",
  #   nargs = "+",
  #   type = str,
  #   required = True
  # )
  #
  # parser.add_argument(
  #   "--interactive",
  #   type = str,
  #   default = "False",
  #   required = False
  # )
  #
  # arguments = parser.parse_args()

  main()
