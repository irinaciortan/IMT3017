
import numpy as np 
from histogram import imhist

def cumsum(h):
    # finds cumulative sum of a numpy array
    return [sum(h[:i+1]) for i in range(len(h))]



def histeq(im):
    #calculate Histogram
    m,n = im.shape
    #normalize the histogram
    NormalizedHist = imhist(im)/(m*n)
    cdf = np.array(cumsum(NormalizedHist)) #cumulative distribution function
    TransferFunction = np.uint8(255 * cdf) #finding transfer function values
   
    OutputImage = np.zeros_like(im)
    #Compute the histogram of the output image
    
    '''
    Write a code for histogram equalization here
    '''
        
        
        
    
    Outhist = imhist(OutputImage)/(m*n)
    #return transformed OutputImage, original and output image histogram, 
    # and transform function
    return OutputImage,NormalizedHist, Outhist, TransferFunction