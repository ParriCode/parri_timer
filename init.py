import json
if __name__ == "__main__":
    with open("config.json","r") as jfile:
        jfile = json.load(jfile)
    if jfile["digital"] == False and jfile["show_installer"] == True:
        import  install_font
        install_font.ask()
    exec(open("main.py").read())