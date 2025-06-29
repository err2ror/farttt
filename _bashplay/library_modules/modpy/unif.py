class HexError(Exception):
    def __init__(self, message):        
        self.message = message
    def __str__(self):
        return self.message
def uhex(he):
    try:
        return chr(int(f"0x{he}",16))
    except:
        raise HexError("No hexadecimal value found.")
newline="\u000A"

