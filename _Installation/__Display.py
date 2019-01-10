from . import *
class Display(object):
  """
  Argument(s):
  @Payload:
    __Payload       - Required  : (__init__)

    --proxy         - Required  : [server, hostname, location]
  """
  def __init__(self, executions, interactive = False, iteration = 0, total = None, prefix = '', suffix = '', decimals = 1, length = 30, fill = '█'):
    self.executions = executions
    self.interactive = interactive

    self.iteration = iteration
    self.prefix = prefix
    self.suffix = suffix
    self.decimals = decimals
    self.length = length
    self.fill = fill

    self.total = executions

  def display(self):
    print("╔═════════════╦═══════════════════════╗".center(os.get_terminal_size().columns))
    print("║             ║  © Vault Cipher LLC.  ║".center(os.get_terminal_size().columns))
    print("║   Payload   ╟───────────────────────╢".center(os.get_terminal_size().columns))
    print("║             ║   Jacob B. Sanders    ║".center(os.get_terminal_size().columns))
    print("╟─────────────╨───────────────────────╢".center(os.get_terminal_size().columns))
    print("║     developer.vault@gmail.com       ║".center(os.get_terminal_size().columns))
    print("╟───────────────────────────┬─────────╢".center(os.get_terminal_size().columns))
    print("║    git.vaultcipher.com    │  snow   ║".center(os.get_terminal_size().columns))
    print("╚═══════════════════════════╧═════════╝".center(os.get_terminal_size().columns))

    self.percent = ("{0:." + str(self.decimals) + "f}").format(100 * (self.iteration / float(self.total)))
    self.filled_length = int(self.length * self.iteration // self.total)
    self.bar = "┃" + self.fill * self.filled_length + '░' * (self.length - self.filled_length) + "┃" + " " + str(self.percent) + "%"

    print("Initializing Security Handshake".center(os.get_terminal_size().columns), end = "\r")
    time.sleep(1.5)

    print("Executing Network Payload".center(os.get_terminal_size().columns), end = "\r")
    time.sleep(1.5)

    print(self.bar.center(os.get_terminal_size().columns), end = "\r")
    time.sleep(0.5)

    for index in range(0, self.total):
      self.iteration += 1

      self.percent = ("{0:." + str(self.decimals) + "f}").format(100 * (self.iteration / float(self.total)))
      self.filled_length = int(self.length * self.iteration // self.total)
      self.bar = "┃" + self.fill * self.filled_length + '░' * (self.length - self.filled_length) + "┃" + " " + str(self.percent) + "%"

      sys.stdout.write(self.bar.center(os.get_terminal_size().columns) + "\r")
      sys.stdout.flush()

      time.sleep(0.225)

      if self.iteration == 1000:
        print()
