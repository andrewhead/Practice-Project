from writeleft import WriteLeft
from testpackage import functions


writeleft = WriteLeft({
    'owner': 'andrewhead',
    'repository': 'Practice-Project',
}, max_contributions=2)
writeleft.collect(functions)
