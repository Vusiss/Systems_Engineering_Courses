import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rice, poisson, rayleigh
from IPython.display import Image



def salt_and_pepper_noise(image, amount=0.05):
    noisy_image = image.copy()
    

    num_salt = np.ceil(amount * image.size * 0.5)
    num_pepper = np.ceil(amount * image.size * 0.5)

    # Białe piksele
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape[:2]]
    noisy_image[coords[0], coords[1]] = 255

    # Czarne piksele
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape[:2]]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image

def update_noise(val):
    amount = val / 100
    noisy = salt_and_pepper_noise(image, amount)
    cv2.imshow('Noisy Image', noisy)

image = cv2.imread('/Users/vusis/Documents/Code/Studia/Sem IV/Przetwarzanie Strumieni Danych/Monet.jpeg')

cv2.namedWindow('Noisy Image')
cv2.createTrackbar('Noise level', 'Noisy Image', 0, 100, update_noise)

cv2.imshow('Noisy Image', image)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()