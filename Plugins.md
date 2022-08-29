# Follow this format to make your own plugin for THANOSPRO.

```python3
"""
A sample code to display rishuo without taking input.
"""
# this is a mandatory import
from . import *

# assigning command
@rishu_cmd(pattern="hii$")
async def hi(event):
    # command body
    await eor(event, "rishuo!")


# to display in help menu
CmdHelp("hii").add_command(
  "hii", None, "Says rishuo!"
).add()
```

```python3
"""
A sample code to display rishuo with input.
"""
# this is a mandatory import
from . import *

# assigning command
@rishu_cmd(pattern="hii(?:\s|$)([\s\S]*)")
async def hi(event):
    # command body
    _input = event.pattern_match.group(1)
    if _input:
        await eor(event, f"rishuo! {_input}")
    else:
        await eor(event, "rishuo!")


# to display in help menu
CmdHelp("hii").add_command(
    "hii", "<text>", "Display rishuo with a input!"
).add()
```


## To get more functions read codes in repo.
