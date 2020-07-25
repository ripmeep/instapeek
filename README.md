# instapeek
An Instagram information discovery tool which shows information about an Instagram user and their posts

_____________________________________________

# Installation

    # git clone https://github.com/ripmeep/instapeek
    # cd instapeek
    # sudo chmod +x install.sh
    # sudo bash install.sh
   
______________________________________________

# Usage

    # instapeek --help
```
usage: instapeek [-h] -U USERNAME [--get-posts] [-O OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -U USERNAME, --username USERNAME
                        Username to peek [example: --username/-U johndoe]
  --get-posts           Get information on the users posts (MUST BE PUBLIC ACCOUNT)
  -O OUTPUT, --output OUTPUT
                        Output information to file [example: --output/-O username.txt]
```

______________________________________________

# Example

    # instapeek  --username yourusername
 
 
______________________________________________

# Example To Get Posts Information

    # instapeek  --username yourusername  --get-posts
    
______________________________________________

# Output To File

    # instapeek  --username yourusername  --get-posts  --output yourusername.txt
