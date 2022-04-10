# This also requires the R bin directory to be added to PATH, and R_HOME to be populated
# Used a personal library at C:\Users\KayAvila\Documents/R/win-library/4.1

import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

if __name__ == '__main__':
    base = importr('base')
    utils = importr('utils')
    stats = importr('stats')

    # Only needs to be done once to install the NEON R package
    #utils.install_packages('neonUtilities', repos='https://cran.rstudio.com/');
    neonUtilities = importr('neonUtilities')

    neonUtilities.stackByTable('../data/NEON_count-beetles.zip')

