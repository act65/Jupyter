# Gaussians

$f\left(x\right) = a e^{- { \frac{(x-b)^2 }{ 2 c^2} } }$

Normalized Gaussian curves with expected value μ and variance $\sigma^2$. The corresponding parameters are $a = \tfrac{1}{\sigma\sqrt{2\pi}}$, $b = \mu$, and $c = \sigma$.

Therefore $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^{2}}{(2\sigma)^2}}$


```python
import numpy as np
import matplotlib.pyplot as plt

#Gaussian
plt.figure()
x = np.linspace(-10,10,100)
n = 6; mu = 0;
sigma = np.linspace(0,5,n)
for s in sigma:
	y = (1/s*np.sqrt(2*np.pi)) * np.exp(-((x - mu)**2)/((2*s)**2))
	plt.plot(x, y, label = 'sigma = ' + str(s))
plt.legend()

```
Am I sure that this is right? what is the $k \neq i$ all about?


Surely for MNSIT we are uninterested at the lowest level of local structure? As pixels are normally next to other pixels, we already know this... What we want to correlate is ???


### So how does this relate to t-SNE?
* This is the distribution that the probabilities are taken from. 
* High variance preserves global structure and low variance preserves local structure
	* hmm, it would be nice if we could avoid this dichotomy
* Preferable we would have a distrubution with a long tail? this could help preserve global structure as the sum of all forces over the data points would help shape this
	* however, doesnt t-SNE repel some datapoints? need to look into this
*  Why gaussians? It seems like a big assumption that the relationship between data points is gaussian.
	* What other options are there? 
	* Gaussians give us? p(x), and symmetry. chi squared is more like two interacting forces? 

$p_{j\mid i} = \frac{\exp(-\lVert\mathbf{x}_i - \mathbf{x}_j\rVert^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-\lVert\mathbf{x}_i - \mathbf{x}_k\rVert^2 / 2\sigma_i^2)}$

Hmm, that looks familiar.


```python
#Gaussian with softmax
plt.figure()
m = 100
x_i = np.random.random(m)
x_j = np.random.random(m)
n = 6; mu = 0;
sigma = np.linspace(0,5,n)
for s in sigma:
	y = np.exp(-((x_i - x_j)**2)/((2*s)**2))
	plt.scatter(x, y/(np.sum(y), label = 'sigma = ' + str(s))
plt.legend()
```
If we consider a simple example in 3d. We have two points, A and B. A = (3,4,10000) and B = (3,4,0). Now these two points are quite similar, except for the third dimension, z. If we took the euclidean distance between them it would equal

$$ \sqrt{3^2 + 4^2 + 10000^2} - \sqrt{3^2 + 4^2 + 10000^2}  = ???$$

which is not representative of their similairty. We needa better norm? What are the alternatives and how do we want it to behave?
