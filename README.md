# On the uncertainty quantification of hyperelastic properties using precise and imprecise probabilities 
This study explores the critical role of uncertainty quantification (UQ) and propagation of hyperelastic properties within uterine tissue for simulating second-stage labor. The methodology employs the classical Monte Carlo method integrated into ABAQUS via Python scripting.

The soft tissues of the pelvis are characterized using both Neo-Hookean and Mooney Rivlin hyperelastic models. The UQ process focuses on the material properties (C10, D1, C01) of pelvis soft tissue, which are treated as uncertain inputs.

![image](https://github.com/NhatThanh92/Uncertainty-Quantification/assets/51020597/d104422b-43e7-4ad9-9828-724087946e15).
 
  ![Media1-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/c313419b-3ca4-4319-a147-47174a8a50c3)
  
   **Fig 1. Simulation of the movement of the sphere out of the uterus, including analysis of implicit dynamics and damping coefficients.**
      
## 1.Precise Probability:
 - Based on a literature review, C10 is estimated at 0.05 ± 0.01 MPa and D1 at 24 ± 5 MPa-1.
 - The Quantities of Interest (QoI) are the maximal values of Von-Mises stresses (S).
![image](https://github.com/NhatThanh92/Uncertainty-Quantification/assets/51020597/2c2dd489-72b7-45f8-a93a-7ebc7f207f1b)
   **Fig 2. CDF of Max_stress from Mooney-Rivlin (a) and Neo-Hookean law (b).**
## 2.Imprecise Probability:

 - Epistemic uncertainties, arising from potential data and knowledge gaps in identifying variables C10 and D1, are managed using a probability-box (P-box) approach.
 - The P-box determines the unknown Cumulative Distribution Function (CDF) of random variable X by its lower and upper bound distributions.
   This approach aims to provide input data for simulation while disregarding any correlations between variables.

![image](https://github.com/NhatThanh92/Uncertainty-Quantification/assets/51020597/9fd6d024-9c99-4c4a-9ce0-b389cc76edd8)
 **Fig 3. The Horsetail plot generates 100 potential CDFs of normal distribution for C10 and D1 (following N(μ, σ)) to supply input data for Monte Carlo simulation.**
# References:
[1]. **Nguyen, Trieu-Nhat-Thanh**, Abbass Ballit, Pauline Lecomte-Grosbras, Jean-Baptiste Colliat, and Tien-Tuan Dao. "On the uncertainty quantification of hyperelastic properties using precise and imprecise probabilities toward reliable in silico simulation of the second-stage labor." Journal of Mechanics in Medicine and Biology (2023): 2350083. https://doi.org/10.1142/S0219519423500835

[2]. **Nguyen, Trieu-Nhat-Thanh**, Abbass Ballit, Pauline Lecomte-Grosbras, Jean-Baptiste Colliat, and Tien-Tuan Dao. "On the uncertainty quantification of the active uterine contraction during the second stage of labor simulation." Medical & Biological Engineering & Computing (2024): 1-20. https://doi.org/10.1007/s11517-024-03059-2  
