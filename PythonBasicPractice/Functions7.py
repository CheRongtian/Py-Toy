import Functions6
Functions6.make_pizza2('pepper', 'sausage')

import Functions6 as F
F.make_pizza2('pepper')

from Functions6 import make_pizza2
make_pizza2('extra cheese', 'chicken')

from Functions6 import make_pizza2 as mp2
mp2('lobster')

from Functions6 import * #import all functions in a module
make_pizza2('mushroom')