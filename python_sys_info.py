#Hi i am YHI547
import sys
from colorama import Fore, Style

python_version = sys.version
platform = sys.platform
execuntable_path = sys.executable
flags = sys.flags

sty = Style.RESET_ALL
red = Fore.RED
gr = Fore.GREEN
 
def main():
    print(
        f"""
{red}your version python  : {sty}{gr}{python_version}{sty}
--------------------->
{red}your platform : {sty}{gr}{platform}{sty}
--------------------->
{red}the exact path to your executable file : {sty}{gr}{execuntable_path}{sty}
--------------------->
{red}your systems active flags : {sty}{gr}{flags}{sty}
        """
    )
if __name__ == "__main__":
    main()
    

