
from skimage import data
import matplotlib.pyplot as plt


class Filter(object):
    def __init__(self):
        pass
        
class Operation(object):
    def __init__(self):
        pass

class Crop(Operation):
    def __init__(self):
        pass


class Gaussian(Filter):
    __all__ = ['gaussian']
    def _convert_input(image, preserve_range):
    if preserve_range:
        image = image.astype(np.double)
    else:
        image = img_as_float(image)
    return image

    def gaussian(image, sigma=1, output=None, mode='nearest', cval=0,
             multichannel=None, preserve_range=False, truncate=4.0):

             spatial_dims = guess_spatial_dimensions(image)
    if spatial_dims is None and multichannel is None:
        msg = ("Images with dimensions (M, N, 3) are interpreted as 2D+RGB "
               "by default. Use `multichannel=False` to interpret as "
               "3D image with last dimension of length 3.")
        warn(RuntimeWarning(msg))
        multichannel = True
    if np.any(np.asarray(sigma) < 0.0):
        raise ValueError("Sigma Valores inferiores a Zero não são Válidos")
    if multichannel:
        # Não Filtra por Canais
        if not isinstance(sigma, coll.Iterable):
            sigma = [sigma] * (image.ndim - 1)
        if len(sigma) != image.ndim:
            sigma = np.concatenate((np.asarray(sigma), [0]))
    image = convert_to_float(image, preserve_range)
    return ndi.gaussian_filter(image, sigma, mode=mode, cval=cval,
truncate=truncate)

        pass
        
class Color(Filter):
    def __init__(self):
        pass
