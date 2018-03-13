from skimage import feature
import numpy as np

class FeatureExtractor(object):
    # Construtor
    def __init__(self):
        pass
        
# Descritor de textura    HaralickExtractor     
class HaralickExtractor(FeatureExtractor):
    def __init__(self):
        pass
        
# Descritor de textura LBP 
class LBPExtractor(FeatureExtractor):
    def __init__(self):
        def __init__(self, numPoints=24, radius=8, method="uniform"):
		#  armazene o número de pontos e raio
		self.numPoints = numPoints
		self.radius = radius
		self.method = method
 
   def describe(self, image, eps=1e-7):
	    # computa a representação do padrão binário local
        # da imagem, e depois use a representação LBP
        # para construir o histograma de padrões
		lbp = feature.local_binary_pattern(image, self.numPoints, self.radius, method=self.method)
		
		#n_bins = int(lbp.max() + 1)
        #hist, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
		(hist, _) = np.histogram(lbp.ravel(),  bins=np.arange(0, self.numPoints + 3), range=(0, self.numPoints + 2))
		#(hist, _) = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
 	  
		
        # normalize o histograma
		hist = hist.astype("float")
		hist /= (hist.sum() + eps)
 
        # retorna o histograma de Padrões Binários Locais
		return hist
        
