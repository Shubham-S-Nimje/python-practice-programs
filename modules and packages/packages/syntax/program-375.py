# Write a program to test package, create a module or program outside the 
# package

# ptest1.py
import package1.module1
import package1.module2

package1.module1.fun1()
package1.module1.fun2()
package1.module1.fun3()
package1.module2.f1()
package1.module2.f2()

# Output
# fun1 of module1 of package1
# fun2 of module1 of package1
# fun3 of module1 of package1
# f1 of module2 of package1
# f2 of module2 of package1

# ptest2.py
from package1 import module1
from package1 import module2

module1.fun1()
module1.fun2()
module2.f1()
module2.f2()

# Output
# fun1 of module1 of package1
# fun2 of module1 of package1
# f1 of module2 of package1
# f2 of module2 of package1


# Ptest3.py
from package1.module1 import *
from package1.module2 import *
fun1()
fun2()
f1()
f2()

# Output
# fun1 of module1 of package1
# fun2 of module1 of package1
# f1 of module2 of package1
# f2 of module2 of package1


