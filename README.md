# On the uncertainty quantification of hyperelastic properties using precise and imprecise probabilities 
This study explores the critical role of uncertainty quantification (UQ) and propagation of hyperelastic properties within uterine tissue for simulating second-stage labor. The methodology employs the classical Monte Carlo method integrated into ABAQUS via Python scripting.

The soft tissues of the pelvis (PST) are characterized using both Neo-Hookean and Mooney Rivlin hyperelastic models. The UQ process focuses on the material properties (C10, D1, C01) of pelvis soft tissue, which are treated as uncertain inputs.
![image](https://github.com/NhatThanh92/Uncertainty-Quantification/assets/51020597/dff51206-3f0a-475c-9995-252deffc3ea7)
## 1.Precise Probability:
 - Based on a literature review, C10 is estimated at 0.05 ± 0.01 MPa and D1 at 24 ± 5 MPa-1.
 - The Quantities of Interest (QoI) are the maximal values of Von-Mises stresses (S).
![image](https://github.com/NhatThanh92/Uncertainty-Quantification/assets/51020597/7bb05470-2a80-45b1-a47f-512304d7304a)
**Fig 1. CDF of Max_stress from Mooney-Rivlin (a) and Neo-Hookean law (b)**
