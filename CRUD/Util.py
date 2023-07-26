"""
This module will generate the primary key for the database
"""

import random
import string

def random_string(length):
    """
    Function for generate random string for PK
    """
    id = string.ascii_letters + string.digits
    out = ''.join(random.choice(id) for i in range(length))
    return out