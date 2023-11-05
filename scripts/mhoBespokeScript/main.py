import os
from splash import SplashScreen
from tagid import TagId
from gen_files import ContentMenu

# from mhoBespoke.templates.template_org_denote import WriteOrgFiles

if __name__ == "__main__":
    os.system("clear")
    SplashScreen().show_splash()
    TagId.genTagId()
    ContentMenu().show_menu()
