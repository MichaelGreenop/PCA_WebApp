# PCA_WebApp

Provides a step by step using principal component analysis of vibrational spectroscopy datasets

Pages
1) (Note: Need to add some more here!)
2) Cumulative explained variance
3) Principal component selection
4) Score plot 
5) Loading plot

Method (breif):

- Use the cumulative explained variance plot (page 2) to see which PCs contain the majority of the dataset variance
- From the PCs identified in page 2, use a decision tree to determine which seperate your classes best (page 3)
- Compare the seperation of the classes in a score plot (page 4)
- Visulaise the features (wavelengths) with the greatest contribution to the PC varience (page 5)

Data format:
The GUI takes three inputs, the data matrix (X), labels (y), and wavelength range (w)
All three can be entered in csv format.

Data matrix: A matrix of the spectra, where every row is a spectrum

Labels: A column of labels, which aligns with the spectra in the data matrix 
e.g. If the top 500 spectra are class A and the bottom 500 class B in the data matrix, the fist 500 labels will relate to class A and the second 500 class B
The labels must be the same size as a column in the data matrix

Wavelengths: Is a row of wavelengths, allowing the loading for each wavelength to be shown in page 5
The length of the wavelengths must match the width of the data matrix
