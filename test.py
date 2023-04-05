import numpy2mcpl
import numpy as np

l1 = np.linalg.norm( (4,5,6,) )
l2 = np.linalg.norm( (6,3,5,) )

system_p = np.array([[1., 2., 3.,   4./l1, 5./l1, 6./l1,    7., 9., 4., 0.,1.,0. ],
                     [3., 2., 5.,   6./l2, 3./l2, 5./l2,    6., 3., 5., 1.,0.,0.]])

numpy2mcpl.numpy2mcpl_dump("thefile",system_p)

