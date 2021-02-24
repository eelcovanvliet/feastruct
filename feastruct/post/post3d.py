import numpy as np

import feastruct.fea.bcs as bcs

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class PostProcessor3D:
    
    def __init__(self, analysis, n_subdiv=11):
    
        self.analysis = analysis
        self.n_subdiv = n_subdiv
    
    def plot_geom(self, analysis_case, ax=None, supports=True, loads=True, undeformed=True,
                  deformed=False, def_scale=1, dashed=False):
        

        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            # ax.plot_wireframe(X, Y, Z)


        for el in self.analysis.elements:
            if dashed:
                el.plot_element(ax=ax, linestyle='--', linewidth=1, marker='')
            else:
                el.plot_element(ax=ax)
            
        
        plt.box(on=None)
        plt.show()            
            
            

        # for el in self.analysis.elements:
        #     if deformed:
        #         el.plot_deformed_element(
        #             ax=ax, analysis_case=analysis_case, n=self.n_subdiv, def_scale=def_scale)
        #         if undeformed:
        #             el.plot_element(ax=ax, linestyle='--', linewidth=1, marker='')
        #     else:
        #         if dashed:
        #             el.plot_element(ax=ax, linestyle='--', linewidth=1, marker='')
        #         else:
        #             el.plot_element(ax=ax)

        # # set initial plot limits
        # (xmin, xmax, ymin, ymax, _, _) = self.analysis.get_node_lims()
        # ax.set_xlim(xmin-1e-12, xmax)
        # ax.set_ylim(ymin-1e-12, ymax)

        # # get 2% of the maxmimum dimension
        # small = 0.02 * max(xmax-xmin, ymax-ymin)
        
        # # plot layout
        # plt.axis('tight')
        # ax.set_xlim(self.wide_lim(ax.get_xlim()))
        # ax.set_ylim(self.wide_lim(ax.get_ylim()))

        # limratio = np.diff(ax.get_ylim())/np.diff(ax.get_xlim())

        # if limratio < 0.5:
        #     ymid = np.mean(ax.get_ylim())
        #     ax.set_ylim(ymid + (ax.get_ylim() - ymid) * 0.5 / limratio)
        # elif limratio > 1:
        #     xmid = np.mean(ax.get_xlim())
        #     ax.set_xlim(xmid + (ax.get_xlim() - xmid) * limratio)

        # ax.set_aspect(1)
        # plt.box(on=None)
        # plt.show()