# figletgw

A CLI for [FIGlet][figlet]

### Purpose

This is a CLI that can be used for making large letters out of ordinary text through a program called FIGlet.

It uses gopher://gopher.floodgap.com:70/1/fun/figletgw to fetch results.

### Installation

If you've cloned this project, and want to install the library (*and all
development dependencies*), the command you'll want to run is:
```sh
    $ pip install -e .[test]
```

### Usage
```sh
figlet [-f | --font <font_name>] <text>
figlet -h | --help
figlet --version
figlet -l | --list-font
```

### Options
```
-h --help                       Show this screen.
--version                       Show version.
-l --list-font                  List supported fonts
-f --font                       Font to be used for formatting (default='small')
```

### Example
```sh
figletgw -f colossal "hello"

FFFFFFFFFFFFFFFFFFFFFFIIIIIIIIII      GGGGGGGGGGGGG
F::::::::::::::::::::FI::::::::I   GGG::::::::::::G
F::::::::::::::::::::FI::::::::I GG:::::::::::::::G
FF::::::FFFFFFFFF::::FII::::::IIG:::::GGGGGGGG::::G
  F:::::F       FFFFFF  I::::I G:::::G       GGGGGG
  F:::::F               I::::IG:::::G              
  F::::::FFFFFFFFFF     I::::IG:::::G              
  F:::::::::::::::F     I::::IG:::::G    GGGGGGGGGG
  F:::::::::::::::F     I::::IG:::::G    G::::::::G
  F::::::FFFFFFFFFF     I::::IG:::::G    GGGGG::::G
  F:::::F               I::::IG:::::G        G::::G
  F:::::F               I::::I G:::::G       G::::G
FF:::::::FF           II::::::IIG:::::GGGGGGGG::::G
F::::::::FF           I::::::::I GG:::::::::::::::G
F::::::::FF           I::::::::I   GGG::::::GGG:::G
FFFFFFFFFFF           IIIIIIIIII      GGGGGG   GGGG
```

[figlet]: http://www.figlet.org/
