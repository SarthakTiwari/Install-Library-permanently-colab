import os, sys
from google.colab import drive
drive.mount('/content/drive')
nb_path = '/content/notebooks'
os.symlink('/content/drive/My Drive/Colab Notebooks', nb_path)
sys.path.insert(5, nb_path)

!pip install --target=$nb_path pytorch_lightning #call only once

import pytorch_lightning
