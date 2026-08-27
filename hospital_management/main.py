
from hospital import Hospital

h = Hospital()
h.visit(1, 'Emergency')
h.visit(2, 'Normal')
h.visit(3, 'Emergency')
h.visit(4, 'Normal')
h.details(4)
h.details(3)
h.visit(5, 'Normal')
h.cancel(2)
h.visit(6, 'Normal')
h.visit(7, 'Emergency')
h.treated(2)

